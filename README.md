# 🚀 LearnHub – Online Course Platform API

A complete backend project built using **FastAPI** that simulates a real-world online course platform. This API supports course browsing, enrollments, wishlist management, filtering, sorting, and pagination.

---

## 📌 Features

### 🎯 Course Management

* Get all courses with summary
* Get course by ID
* Create, update, and delete courses
* Prevent deletion if students are enrolled

### 🔍 Search, Filter, Sort

* Search courses by keyword (title, instructor, category)
* Filter by category, level, price, and seat availability
* Sort by price, title, or seats
* Combined advanced browsing endpoint (`/courses/browse`)

### 🎓 Enrollment System

* Enroll in courses
* Dynamic pricing with discounts
* Coupon support
* Gift enrollments

### ❤️ Wishlist

* Add/remove courses from wishlist
* Bulk enroll from wishlist
* Calculate total wishlist value

### 📄 Pagination

* Paginate courses and enrollments
* Metadata included (`page`, `total_pages`, `total`)

---

## 🛠️ Tech Stack

* Python 3.10+
* FastAPI
* Pydantic
* Uvicorn

---

## 📂 Project Structure

```
learnhub/
│── main.py
│── requirements.txt
│── README.md
```

---

## ⚙️ How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/saisandeep1912/Fastapi_Online_Course_Platform.git
cd Fastapi_Online_Course_Platform
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the server

```bash
uvicorn main:app --reload
```

### 5️⃣ Open in browser

```
http://127.0.0.1:8000/docs
```

---

## 🌐 API Documentation

* Swagger UI → http://127.0.0.1:8000/docs
* ReDoc → http://127.0.0.1:8000/redoc

---

## 🌍 Live Demo (Optional but Recommended)

(Add after deployment)

```
https://your-app-name.onrender.com/docs
```

---

## 🧪 Sample Endpoints

### Search Courses

```
GET /courses/search?keyword=python
```

### Sort Courses

```
GET /courses/sort?sort_by=price&order=desc
```

### Browse Courses (Advanced)

```
GET /courses/browse?keyword=dev&category=Web Dev&level=Beginner&max_price=2000&page=1&limit=2
```

---

## ⚠️ Key Learnings

* Handling route conflicts in FastAPI (`/courses/{id}` vs `/courses/search`)
* Designing consistent data structures
* Implementing real-world API features
* Debugging validation and runtime errors

---

## 📸 Screenshots
<img width="1366" height="691" alt="Swagger1" src="https://github.com/user-attachments/assets/350f8079-8bb3-47f6-a0d2-d2db00f0a5d4" />
<img width="1366" height="689" alt="Swagger2" src="https://github.com/user-attachments/assets/932afd3e-21d1-48a5-a644-eb10f123d3a1" />


---

## 👨‍💻 Author

**Sai Sandeep**

* LinkedIn: https://www.linkedin.com/in/saisandeep1912/
* GitHub: https://github.com/saisandeep1912

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
