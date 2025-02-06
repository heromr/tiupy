# TIUPY

A Python library for interacting with Tishk International University's student portal. This library provides a comprehensive interface for accessing student information, course data, and personal details through TIU's web portal.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

## Features

- **Authentication**
  - Login with username/password
  - Session-based authentication (SID)
  - Secure logout functionality

- **Profile Information**
  - Basic user details (name, department, etc.)
  - Academic information (GPA, grade, curriculum)
  - Personal information (contact details, registration data)
  - Profile image URL retrieval

- **Course Management**
  - Course listings with detailed information
  - Grade information
  - Credit hours tracking
  - JSON export capabilities

## Installation

Install the package using pip:

```bash
pip install tiupy
```

Or install from source:

```bash
git clone https://github.com/yourusername/tiupy.git
cd tiupy
pip install -e .
```

## Quick Start

```python
from tiupy import Tiu

# Initialize client
tiu = Tiu()

# Login
tiu.login("username", "password")

# Get profile information
print(f"Welcome, {tiu.profile.name}")
print(f"Department: {tiu.profile.department}")
print(f"GPA: {tiu.profile.gpa}")

# Get course data
courses = tiu.get_courses_data()
for course in courses.courses:
    print(f"{course.course_code}: {course.grade}")

# Cleanup
tiu.logout()
```

## Detailed Usage

### Authentication

```python
from tiupy import Tiu

# Standard login
tiu = Tiu()
tiu.login("username", "password")

# Session ID login
tiu.sid_login("existing_session_id")

# Configure with proxy and custom timeout
tiu = Tiu(
    proxies={"http": "http://proxy.example.com:8080"},
    request_timeout=30
)
```

### Profile Information

```python
# Basic profile information
profile = tiu.profile
print(f"Name: {profile.name}")
print(f"Department: {profile.department}")
print(f"Student ID: {profile.student_id}")
print(f"GPA: {profile.gpa}")

# Detailed personal information
personal_info = tiu.get_personal_info()
print(f"Gender: {personal_info.gender}")
print(f"Status: {personal_info.status}")
print(f"Registration Date: {personal_info.registration_date}")

# Phone numbers
print("Student Phones:", personal_info.phones)
print("Father's Phone:", personal_info.father_phone)
print("Mother's Phone:", personal_info.mother_phone)
```

### Course Data

```python
# Get course information
courses = tiu.get_courses_data()

# Access as Python objects
for course in courses.courses:
    print(f"Course: {course.course_name}")
    print(f"Code: {course.course_code}")
    print(f"Credits: {course.credits}")
    print(f"Grade: {course.grade}")
    print("---")

# Export to JSON
json_data = courses.to_json()
print(json_data)

# Get as list of dictionaries
dict_list = courses.to_dict_list()
```

## Error Handling

```python
from tiupy import Tiu

try:
    tiu = Tiu()
    tiu.login("username", "password")
    profile = tiu.profile
except Exception as e:
    print(f"Error occurred: {e}")
finally:
    if tiu.sid:  # Check if login was successful
        tiu.logout()
```

## Data Models

### UserProfile

```python
class UserProfile:
    image: str                # Profile image URL
    name: str                 # Full name
    curriculum: str           # Study curriculum
    department: str           # Department name
    student_id: str          # Student ID number
    grade: str               # Current grade
    email: str               # Email address
    mobile: str              # Mobile number
    gpa: str                 # Grade Point Average
    year: str                # Academic year
    term: str                # Current term
    personal_info: PersonalInfo  # Detailed personal information
```

### PersonalInfo

```python
class PersonalInfo:
    gender: str              # Student's gender
    status: str             # Academic status
    tuition_type: str       # Tuition/Scholarship status
    registration_date: str   # Registration date
    father_name: str        # Father's name
    mother_name: str        # Mother's name
    phones: List[str]       # List of phone numbers
    father_phone: str       # Father's phone number
    mother_phone: str       # Mother's phone number
```

### Course

```python
class Course:
    course_code: str        # Course code
    course_name: str        # Course name
    credits: str           # Credit hours
    grade: str            # Achieved grade
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Tishk International University for providing the student portal
- Contributors who have helped improve this library

## Disclaimer

This library is not officially associated with Tishk International University. Use it responsibly and in accordance with the university's terms of service and policies.
