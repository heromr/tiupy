# TIUPY 

A Python library for interacting with Tishk International University's student portal. It provides features such as user authentication, profile information retrieval, and course data extraction.

---

## **Features**
- Login using username and password or an existing session SID.
- Retrieve user profile information.
- Fetch and parse course data.

---

## **Installation**
To use this library, clone or download the repository. Or install the required using `pip`:

```bash
pip install tiupy
```

---

## **Usage Examples**

### **1. Login and Fetch Profile Information**

```python
from tiupy import Tiu

# Initialize the client
tiu_client = Tiu()

try:
    # Login with username and password
    tiu_client.login("your_username", "your_password")

    # Get profile information
    profile = tiu_client.profile
    print(f"Student Name: {profile.name}")
    print(f"GPA: {profile.gpa}")

finally:
    # Logout from the session
    tiu_client.logout()
```

---

### **2. Login with Session SID**

```python
from tiupy import Tiu

tiu_client = Tiu()

try:
    # Login with an existing SID
    tiu_client.sid_login("your_existing_sid")

    # Get profile information
    print("Logged in with SID successfully.")
finally:
    tiu_client.logout()
```

---

### **3. Fetch Course Data**

```python
from tiupy import Tiu

tiu_client = Tiu()

try:
    # Login first
    tiu_client.login("your_username", "your_password")

    # Get course data
    courses = tiu_client.get_courses_data()

    # Print as JSON
    print("Courses JSON:\n", courses.to_json())
finally:
    tiu_client.logout()
```

---

### **4. Profile Data Attributes**
After login, access the `profile` object for user information:

```python
profile = tiu_client.profile
print("Name:", profile.name)
print("Email:", profile.email)
print("Department:", profile.department)
print("Mobile:", profile.mobile)
```

---

### **5. Course Data Attributes**
Access the list of courses using the `courses` object:

```python
for course in courses.courses:
    print(f"{course.course_code} - {course.course_name}: {course.grade}")
```

---

## **Error Handling**
The library raises exceptions when requests fail. Always handle potential errors:

```python
from tiupy import Tiu

try:
    tiu_client = Tiu()
    tiu_client.login("wrong_user", "wrong_password")
except Exception as e:
    print(f"An error occurred: {e}")
```

---

## **Example Scripts**

### **1. Login Example (`example_login.py`)**

```python
from tiupy import Tiu

def main():
    tiu_client = Tiu()
    
    try:
        tiu_client.login("your_username", "your_password")
        profile = tiu_client.profile
        print("Login successful.")
        print("Student Name:", profile.name)
    except Exception as e:
        print("Error:", e)
    finally:
        tiu_client.logout()

if __name__ == "__main__":
    main()
```

### **2. Fetch Course Data Example (`example_courses.py`)**

```python
from tiupy import Tiu

def main():
    tiu_client = Tiu()

    try:
        tiu_client.login("your_username", "your_password")
        courses = tiu_client.get_courses_data()
        
        print("Courses Data:")
        for course in courses.courses:
            print(f"{course.course_code} - {course.course_name}: {course.grade}")
    except Exception as e:
        print("Error:", e)
    finally:
        tiu_client.logout()

if __name__ == "__main__":
    main()
```

---

## **Contributing**
Pull requests are welcome. For significant changes, please open an issue first to discuss your ideas.

---

## **License**
This project is licensed under the MIT License.

