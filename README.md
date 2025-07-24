# Library Management System

A Django REST API for managing a library's book collection.

## Features

- **Book Management**: Create, read, update, and delete books
- **REST API**: Full RESTful API with Django REST Framework
- **Custom Fields**: Automatically calculated fields like "days since created"
- **Data Validation**: ISBN validation, date validation, and more
- **Browsable API**: Interactive API documentation

## Technologies Used

- Django 5.2
- Django REST Framework
- SQLite (default database)
- Python 3.12

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/library-management-system.git
   cd library-management-system
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**
   ```bash
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install django djangorestframework
   ```

5. **Navigate to project directory**
   ```bash
   cd my_library
   ```

6. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

8. **Start development server**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Books API

- **GET /api/v2/books/** - List all books
- **POST /api/v2/books/** - Create a new book
- **GET /api/v2/books/{id}/** - Retrieve a specific book
- **PUT /api/v2/books/{id}/** - Update a book
- **PATCH /api/v2/books/{id}/** - Partially update a book
- **DELETE /api/v2/books/{id}/** - Delete a book

### Custom Endpoints

- **GET /api/v2/books/recent/** - Get recently added books
- **POST /api/v2/books/{id}/mark_favorite/** - Mark book as favorite

### Query Parameters

- `?author=name` - Filter books by author
- `?title=name` - Filter books by title

## Book Model

```json
{
  "id": 1,
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "published_date": "1925-04-10",
  "isbn": "9780743273565",
  "pages": 180,
  "created_at": "2025-07-25T10:30:00Z",
  "updated_at": "2025-07-25T10:30:00Z",
  "days_since_created": 5
}
```

## Testing the API

### Using the Browsable API
1. Visit `http://127.0.0.1:8000/api/v2/books/`
2. Use the web interface to test endpoints

### Using curl
```bash
# Get all books
curl http://127.0.0.1:8000/api/v2/books/

# Create a new book
curl -X POST http://127.0.0.1:8000/api/v2/books/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "1984",
    "author": "George Orwell",
    "published_date": "1949-06-08",
    "isbn": "9780451524935",
    "pages": 328
  }'
```

## Development

### Project Structure
```
library/
├── my_library/          # Django project
│   ├── manage.py
│   ├── my_library/      # Settings and URLs
│   └── library_app/     # Main application
│       ├── models.py    # Book model
│       ├── serializers.py # API serializers
│       ├── views.py     # API views
│       └── ...
├── venv/               # Virtual environment
├── .gitignore
└── README.md
```

### Key Features Implemented

1. **Custom Serializer Fields**
   - `days_since_created`: Automatically calculated field

2. **Data Validation**
   - ISBN format validation (10 or 13 digits)
   - Future date validation for published_date
   - Cross-field validation

3. **ViewSets and Generic Views**
   - Both approaches demonstrated
   - Custom actions for extended functionality

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is for educational purposes.