# 🚀 LearnHub – Online Course Platform API

A complete backend project built using **FastAPI** that simulates a real-world online course platform. This API supports course browsing, enrollments, wishlist management, filtering, sorting, and pagination.

---

## 📌 Features

### 🎯 Course Management

* Get all courses with summary
* Get course by ID
* Create, update, delete courses
* Prevent deletion if students are enrolled

### 🔍 Search, Filter, Sort

* Search courses by keyword (title, instructor, category)
* Filter by category, level, price, seat availability
* Sort by price, title, or seats
* Combined browsing endpoint (`/courses/browse`)

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
* Metadata included (page, total_pages, total)

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



## ⚠️ Key Learnings

* Handling route conflicts in FastAPI (`/courses/{id}` vs `/courses/search`)
* Designing consistent data structures
* Implementing real-world API features
* Debugging validation and runtime errors

---

## 👨‍💻 Author

**Sai Sandeep**

* LinkedIn: https://www.linkedin.com/in/saisandeep1912/
* GitHub: https://github.com/saisandeep1912

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
