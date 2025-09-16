# Flask User Management REST API

A simple yet comprehensive REST API built with Flask for managing user data. This project demonstrates fundamental API development concepts including CRUD operations, input validation, error handling, and proper HTTP status codes.

## 🚀 Features

- **Complete CRUD Operations** - Create, Read, Update, Delete users
- **Input Validation** - Validates required fields and email format
- **Duplicate Prevention** - Prevents duplicate email addresses
- **Error Handling** - Comprehensive error responses with meaningful messages
- **In-Memory Storage** - Uses dictionary for data persistence (development purposes)
- **Auto-Incrementing IDs** - Automatic user ID assignment
- **Timestamps** - Tracks creation and update times
- **Health Check** - API status monitoring endpoint
- **Sample Data** - Includes test users for immediate experimentation

## 🛠️ Technologies Used

- **Python 3.7+**
- **Flask** - Web framework
- **JSON** - Data exchange format
- **Datetime** - Timestamp management

## 📋 Prerequisites

- Python 3.7 or higher
- pip package manager

## ⚡ Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/flask-user-api.git
   cd flask-user-api
   ```

2. **Install dependencies**
   ```bash
   pip install flask
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the API**
   ```
   http://localhost:5000
   ```

## 📚 API Endpoints

| Method | Endpoint | Description | Request Body |
|--------|----------|-------------|--------------|
| `GET` | `/` | API information and documentation | - |
| `GET` | `/health` | Health check status | - |
| `GET` | `/users` | Retrieve all users | - |
| `GET` | `/users/{id}` | Retrieve specific user | - |
| `POST` | `/users` | Create new user | JSON |
| `PUT` | `/users/{id}` | Update entire user record | JSON |
| `PATCH` | `/users/{id}` | Partially update user | JSON |
| `DELETE` | `/users/{id}` | Delete user | - |

## 🔧 API Usage Examples

### Get All Users
```bash
curl -X GET http://localhost:5000/users
```

### Create New User
```bash
curl -X POST http://localhost:5000/users \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Alice Johnson",
    "email": "alice@example.com",
    "age": 28,
    "phone": "+1122334455"
  }'
```

### Update User
```bash
curl -X PUT http://localhost:5000/users/1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Smith",
    "email": "johnsmith@example.com",
    "age": 31,
    "phone": "+1234567899"
  }'
```

### Partial Update
```bash
curl -X PATCH http://localhost:5000/users/1 \
  -H "Content-Type: application/json" \
  -d '{"age": 32}'
```

### Delete User
```bash
curl -X DELETE http://localhost:5000/users/1
```

## 📊 Request/Response Examples

### Create User Request
```json
{
  "name": "Alice Johnson",
  "email": "alice@example.com",
  "age": 28,
  "phone": "+1122334455"
}
```

### Successful Response (201 Created)
```json
{
  "id": 3,
  "name": "Alice Johnson",
  "email": "alice@example.com",
  "age": 28,
  "phone": "+1122334455",
  "created_at": "2025-01-15T10:30:00.123456",
  "updated_at": "2025-01-15T10:30:00.123456"
}
```

### Error Response (400 Bad Request)
```json
{
  "error": "Missing required field: email"
}
```

## ✅ Data Validation Rules

- **Required Fields**: `name`, `email`
- **Optional Fields**: `age`, `phone`
- **Email Format**: Must contain '@' symbol
- **Unique Constraint**: Email addresses must be unique
- **Data Types**: 
  - `name`: string
  - `email`: string (valid email format)
  - `age`: integer (optional)
  - `phone`: string (optional)

## 🔍 HTTP Status Codes

| Code | Description | When Used |
|------|-------------|-----------|
| `200` | OK | Successful GET, PUT, PATCH operations |
| `201` | Created | Successful user creation |
| `400` | Bad Request | Invalid input data or missing fields |
| `404` | Not Found | User not found |
| `500` | Internal Server Error | Server-side errors |

## 🧪 Testing

### Using Postman
1. Import the collection using the provided examples
2. Set base URL: `http://localhost:5000`
3. Test all endpoints with sample data

### Using curl
All curl commands are provided in the examples above. Test the complete workflow:
1. Health check → Get users → Create user → Update user → Delete user

### Sample Test Data
The application starts with two sample users:
- **John Doe** (john@example.com)
- **Jane Smith** (jane@example.com)

## 📁 Project Structure

```
flask-user-api/
├── app.py              # Main application file
├── README.md           # Project documentation

```

## 🔄 Development Workflow

1. **Development Mode**: The app runs in debug mode by default
2. **Hot Reload**: Changes automatically reload the server
3. **Error Logging**: Detailed error messages in development
4. **CORS**: Configure for frontend integration if needed

## 🚧 Future Enhancements

- [ ] Database integration (SQLite, PostgreSQL)
- [ ] User authentication and authorization
- [ ] Input sanitization and advanced validation
- [ ] Pagination for user lists
- [ ] Search and filtering capabilities
- [ ] Unit tests and integration tests
- [ ] Docker containerization
- [ ] API documentation with Swagger/OpenAPI
- [ ] Rate limiting and security headers
- [ ] Logging and monitoring

---

**⭐ If this project helped you, please give it a star on GitHub!**
