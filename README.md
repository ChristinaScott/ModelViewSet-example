# ModelViewSet Example

## 📌 Overview
This project demonstrates how to use **Django REST Framework (DRF) ModelViewSet** to build a simple API. A **ModelViewSet** is a shortcut that provides CRUD (Create, Read, Update, Delete) operations for a model **without writing separate view functions**.

## 🚀 What This Project Does
- Defines a **database model** (e.g., `Employee`, `Product`, etc.).
- Uses Django REST Framework to create an **API** that interacts with the model.
- Implements a **ModelViewSet** to automate API functionality.
- Provides RESTful API endpoints for **listing, retrieving, creating, updating, and deleting** records.

## 📂 Project Structure
```
/ModelViewSet-example
│── app/
│   ├── models.py         # Defines the database model
│   ├── serializers.py    # Converts model data to JSON format
│   ├── views.py         # Implements ModelViewSet
│   ├── urls.py          # Connects API endpoints
│── project/
│   ├── settings.py       # Django settings
│   ├── urls.py           # Main URL configuration
│── requirements.txt      # Dependencies (install with pip)
│── manage.py             # Django management script
```

## 🛠️ Setup & Installation
### 1️⃣ **Clone the Repository**
```sh
git clone <repo-url>
cd ModelViewSet-example
```

### 2️⃣ **Create and Activate a Virtual Environment**
```sh
python -m venv venv  # Create virtual environment
source venv/bin/activate  # Activate (Mac/Linux)
venv\Scripts\activate  # Activate (Windows)
```

### 3️⃣ **Install Dependencies**
```sh
pip install -r requirements.txt
```

### 4️⃣ **Apply Migrations** (Set up the database)
```sh
python manage.py migrate
```

### 5️⃣ **Run the Development Server**
```sh
python manage.py runserver
```

Now, your API is available at `http://127.0.0.1:8000/`

## 🔗 API Endpoints (Example: Employee Model)
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/employees/` | Get a list of employees |
| POST | `/employees/` | Create a new employee |
| GET | `/employees/{id}/` | Retrieve a specific employee |
| PUT | `/employees/{id}/` | Update an employee |
| DELETE | `/employees/{id}/` | Delete an employee |

## 📌 How It Works
### **1. Models** (`models.py`)
Defines the database structure. Example:
```python
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=50)
```

### **2. Serializers** (`serializers.py`)
Converts model data into JSON for API responses.
```python
from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
```

### **3. Views (ModelViewSet)** (`views.py`)
Handles API logic **without manually writing CRUD functions**.
```python
from rest_framework.viewsets import ModelViewSet
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
```

### **4. URL Configuration** (`urls.py`)
Uses Django **routers** to automatically generate API URLs.
```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

## 🎯 Summary
- **ModelViewSet** automates CRUD operations for a Django model.
- **DRF Serializers** help convert model data into JSON.
- **Routers** automatically generate API endpoints.
- Running the Django server allows API testing via Postman or the browser.

Now you have a fully functional **REST API** with minimal code! 🚀


