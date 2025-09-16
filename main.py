from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

users = {}
user_id_counter = 1

def validate_user_data(data, required_fields=None):
    if required_fields is None:
        required_fields = ['name', 'email']
    if not data:
        return False, "No data provided"
    for field in required_fields:
        if field not in data or not data[field]:
            return False, f"Missing required field: {field}"
    if 'email' in data and '@' not in data['email']:
        return False, "Invalid email format"
    return True, "Valid"

@app.route('/users', methods=['GET'])
def get_all_users():
    return jsonify({
        'users': list(users.values()),
        'count': len(users)
    }), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(users[user_id]), 200

@app.route('/users', methods=['POST'])
def create_user():
    global user_id_counter
    data = request.get_json()
    is_valid, message = validate_user_data(data)
    if not is_valid:
        return jsonify({'error': message}), 400
    for user in users.values():
        if user['email'] == data['email']:
            return jsonify({'error': 'Email already exists'}), 400
    new_user = {
        'id': user_id_counter,
        'name': data['name'],
        'email': data['email'],
        'age': data.get('age'),
        'phone': data.get('phone'),
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat()
    }
    users[user_id_counter] = new_user
    user_id_counter += 1
    return jsonify(new_user), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    data = request.get_json()
    is_valid, message = validate_user_data(data)
    if not is_valid:
        return jsonify({'error': message}), 400
    for uid, user in users.items():
        if uid != user_id and user['email'] == data['email']:
            return jsonify({'error': 'Email already exists'}), 400
    users[user_id].update({
        'name': data['name'],
        'email': data['email'],
        'age': data.get('age'),
        'phone': data.get('phone'),
        'updated_at': datetime.now().isoformat()
    })
    return jsonify(users[user_id]), 200

@app.route('/users/<int:user_id>', methods=['PATCH'])
def patch_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    if 'email' in data:
        if '@' not in data['email']:
            return jsonify({'error': 'Invalid email format'}), 400
        for uid, user in users.items():
            if uid != user_id and user['email'] == data['email']:
                return jsonify({'error': 'Email already exists'}), 400
    allowed_fields = ['name', 'email', 'age', 'phone']
    for field in allowed_fields:
        if field in data:
            users[user_id][field] = data[field]
    users[user_id]['updated_at'] = datetime.now().isoformat()
    return jsonify(users[user_id]), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    deleted_user = users.pop(user_id)
    return jsonify({
        'message': 'User deleted successfully',
        'deleted_user': deleted_user
    }), 200

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'total_users': len(users)
    }), 200

@app.route('/', methods=['GET'])
def root():
    return jsonify({
        'message': 'Flask User Management API',
        'version': '1.0.0',
        'endpoints': {
            'GET /users': 'Get all users',
            'GET /users/<id>': 'Get specific user',
            'POST /users': 'Create new user',
            'PUT /users/<id>': 'Update entire user',
            'PATCH /users/<id>': 'Partially update user',
            'DELETE /users/<id>': 'Delete user',
            'GET /health': 'Health check'
        }
    }), 200

if __name__ == '__main__':
    users[1] = {
        'id': 1,
        'name': 'John Doe',
        'email': 'john@example.com',
        'age': 30,
        'phone': '+1234567890',
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat()
    }
    users[2] = {
        'id': 2,
        'name': 'Jane Smith',
        'email': 'jane@example.com',
        'age': 25,
        'phone': '+0987654321',
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat()
    }
    user_id_counter = 3
    app.run(debug=True, host='0.0.0.0', port=5000)
