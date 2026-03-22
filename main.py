from fastapi import FastAPI, HTTPException, Query, status
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

# DATA

courses = [
    {"id": 1, "title": "Python Programming", "instructor": "Sai", "category": "Data Science", "level": "Beginner", "price": 0, "seats_left": 30},
    {"id": 2, "title": "Machine Learning", "instructor": "Sandeep", "category": "Data Science", "level": "Advanced", "price": 5000, "seats_left": 10},
    {"id": 3, "title": "Web Development", "instructor": "Arjun", "category": "Web Dev", "level": "Intermediate", "price": 3000, "seats_left": 20},
    {"id": 4, "title": "UI UX Design", "instructor": "Virat", "category": "Design", "level": "Beginner", "price": 2000, "seats_left": 25},
    {"id": 5, "title": "DevOps", "instructor": "Jaya", "category": "DevOps", "level": "Advanced", "price": 4000, "seats_left": 15},
    {"id": 6, "title": "React", "instructor": "Sree", "category": "Web Dev", "level": "Beginner", "price": 1500, "seats_left": 35},
]

# Q4
enrollments = []
enrollment_counter = 1

# Q14
wishlist = []

# MODELS

# Q6 & Q9
class EnrollRequest(BaseModel):
    student_name: str = Field(..., min_length=2)
    course_id: int = Field(..., gt=0)
    email: str = Field(..., min_length=5)
    payment_method: str = "card"
    coupon_code: str = ""
    gift_enrollment: bool = False
    recipient_name: str = ""

# Q11
class NewCourse(BaseModel):
    title: str = Field(..., min_length=2)
    instructor: str = Field(..., min_length=2)
    category: str = Field(..., min_length=2)
    level: str = Field(..., min_length=2)
    price: int = Field(..., ge=0)
    seats_left: int = Field(..., gt=0)

# HELPERS

# Q7
def find_course(course_id: int):
    for c in courses:
        if c["id"] == course_id:
            return c
    return None

# Q7
def calculate_enrollment_fee(price, seats_left, coupon_code):
    discounts = []

    if seats_left > 5:
        discount = price * 0.10
        price -= discount
        discounts.append(f"10% early bird (-{int(discount)})")

    if coupon_code == "STUDENT20":
        discount = price * 0.20
        price -= discount
        discounts.append(f"20% coupon (-{int(discount)})")

    elif coupon_code == "FLAT500":
        price -= 500
        discounts.append("Flat ₹500 off")

    return max(0, int(price)), discounts

# Q10
def filter_courses_logic(category=None, level=None, max_price=None, has_seats=None):
    result = courses

    if category is not None:
        result = [c for c in result if c["category"].lower() == category.lower()]

    if level is not None:
        result = [c for c in result if c["level"].lower() == level.lower()]

    if max_price is not None:
        result = [c for c in result if c["price"] <= max_price]

    if has_seats is not None:
        result = [c for c in result if (c["seats_left"] > 0 if has_seats else c["seats_left"] == 0)]

    return result

# DAY 1 

# Q1
@app.get("/")
def home():
    return {"message": "Welcome to LearnHub Online Courses"}

# Q2
@app.get("/courses")
def get_courses():
    return {
        "courses": courses,
        "total": len(courses),
        "total_seats_available": sum(c["seats_left"] for c in courses)
    }

# Q5
@app.get("/courses/summary")
def summary():
    return {
        "total_courses": len(courses),
        "free_courses": len([c for c in courses if c["price"] == 0]),
        "most_expensive": max(courses, key=lambda x: x["price"]),
        "total_seats": sum(c["seats_left"] for c in courses),
        "by_category": {cat: len([c for c in courses if c["category"] == cat]) for cat in set(c["category"] for c in courses)}
    }
# Q10
@app.get("/courses/filter")
def filter_courses(category: str = None, level: str = None, max_price: int = None, has_seats: bool = None):
    data = filter_courses_logic(category, level, max_price, has_seats)
    return {"results": data, "total": len(data)}

# Q16
@app.get("/courses/search")
def search(keyword: str):
    res = [c for c in courses if keyword.lower() in c["title"].lower() or keyword.lower() in c["instructor"].lower() or keyword.lower() in c["category"].lower()]
    return {"results": res, "total_found": len(res)}
# Q17
@app.get("/courses/sort")
def sort_courses(sort_by: str = "price", order: str = "asc"):
    if sort_by not in ["price", "title", "seats_left"]:
        raise HTTPException(400, "Invalid sort field")

    reverse = True if order == "desc" else False
    sorted_data = sorted(courses, key=lambda x: x[sort_by], reverse=reverse)

    return {"sorted": sorted_data}

# Q18
@app.get("/courses/page")
def paginate(page: int = 1, limit: int = 3):
    start = (page - 1) * limit
    end = start + limit
    total_pages = (len(courses) + limit - 1) // limit

    return {
        "page": page,
        "total_pages": total_pages,
        "data": courses[start:end]
    }

# Q20
@app.get("/courses/browse")
def browse(
    keyword: str = None,
    category: str = None,
    level: str = None,
    max_price: int = None,
    sort_by: str = "price",
    order: str = "asc",
    page: int = 1,
    limit: int = 3
):
    data = courses

    if keyword:
        data = [c for c in data if keyword.lower() in c["title"].lower()]

    if category:
        data = [c for c in data if c["category"].lower() == category.lower()]

    if level:
        data = [c for c in data if c["level"].lower() == level.lower()]

    if max_price:
        data = [c for c in data if c["price"] <= max_price]

    reverse = True if order == "desc" else False
    data = sorted(data, key=lambda x: x.get(sort_by, 0), reverse=reverse)

    start = (page - 1) * limit
    end = start + limit

    return {
        "results": data[start:end],
        "total": len(data),
        "page": page
    }


# Q3
@app.get("/courses/{course_id}")
def get_course(course_id: int):
    course = find_course(course_id)
    if not course:
        raise HTTPException(404, "Course not found")
    return course

# Q4
@app.get("/enrollments")
def get_enrollments():
    return {"data": enrollments, "total": len(enrollments)}

#  DAY 2 & 3 

# Q8 & Q9
@app.post("/enrollments")
def enroll(req: EnrollRequest):
    global enrollment_counter

    # Find course
    course = find_course(req.course_id)
    if not course:
        raise HTTPException(404, "Course not found")

    # Check seats
    if course["seats_left"] <= 0:
        raise HTTPException(400, "No seats available")

    # Gift validation
    if req.gift_enrollment and not req.recipient_name:
        raise HTTPException(400, "Recipient name required for gift enrollment")

    # Calculate fee
    final_fee, discounts = calculate_enrollment_fee(
        course["price"],
        course["seats_left"],
        req.coupon_code
    )

    # Reduce seat
    course["seats_left"] -= 1

    # Create record (FULL FORMAT)
    record = {
        "enrollment_id": enrollment_counter,
        "student_name": req.student_name,
        "course_title": course["title"],
        "instructor": course["instructor"],
        "original_price": course["price"],
        "discounts_applied": discounts,
        "final_fee": final_fee,
        "gift_enrollment": req.gift_enrollment,
        "recipient_name": req.recipient_name if req.gift_enrollment else None
    }

    enrollments.append(record)
    enrollment_counter += 1

    return record



# DAY 4

# Q11
@app.post("/courses", status_code=201)
def create_course(course: NewCourse):
    for c in courses:
        if c["title"].lower() == course.title.lower():
            raise HTTPException(400, "Duplicate title")

    new = course.dict()
    new["id"] = len(courses) + 1
    courses.append(new)
    return new

# Q12
@app.put("/courses/{course_id}")
def update_course(course_id: int, price: Optional[int] = None, seats_left: Optional[int] = None):
    course = find_course(course_id)
    if not course:
        raise HTTPException(404, "Not found")

    if price is not None:
        course["price"] = price
    if seats_left is not None:
        course["seats_left"] = seats_left

    return course

# Q13
@app.delete("/courses/{course_id}")
def delete_course(course_id: int):
    course = find_course(course_id)
    if not course:
        raise HTTPException(404, "Not found")

    for e in enrollments:
        
        if (
            ("course_title" in e and e["course_title"] == course["title"]) or
            ("course" in e and e["course"] == course["title"])
        ):
            raise HTTPException(400, "Cannot delete, students enrolled")

    courses.remove(course)
    return {"message": "Deleted successfully"}

# DAY 5

# Q14
@app.post("/wishlist/add")
def add_wishlist(student_name: str, course_id: int):
    course = find_course(course_id)
    if not course:
        raise HTTPException(404, "Course not found")

    for w in wishlist:
        if w["student"] == student_name and w["course_id"] == course_id:
            raise HTTPException(400, "Already exists")

    wishlist.append({"student": student_name, "course_id": course_id, "price": course["price"]})
    return {"message": "Added"}

# Q14
@app.get("/wishlist")
def get_wishlist():
    total = sum(w["price"] for w in wishlist)
    return {"wishlist": wishlist, "total_value": total}

# Q15
@app.delete("/wishlist/remove/{course_id}")
def remove_wishlist(course_id: int, student_name: str):
    for w in wishlist:
        if w["course_id"] == course_id and w["student"] == student_name:
            wishlist.remove(w)
            return {"message": "Removed"}
    raise HTTPException(404, "Not found")

# Q15
@app.post("/wishlist/enroll-all")
def enroll_all(student_name: str, payment_method: str):
    global enrollment_counter

    user_items = [w for w in wishlist if w["student"] == student_name]

    results = []
    total_fee = 0

    for item in user_items:
        course = find_course(item["course_id"])
        if course and course["seats_left"] > 0:
            fee, _ = calculate_enrollment_fee(course["price"], course["seats_left"], "")

            course["seats_left"] -= 1

            record = {
                "id": enrollment_counter,
                "student": student_name,
                "course": course["title"],
                "final_fee": fee
            }

            enrollments.append(record)
            results.append(record)
            total_fee += fee
            enrollment_counter += 1

            wishlist.remove(item)

    return {"enrolled": len(results), "total_fee": total_fee, "details": results}

# DAY 6 

# Q19
@app.get("/enrollments/search")
def search_enrollments(student_name: str):
    return [
        e for e in enrollments
        if student_name.lower() in e["student_name"].lower()
    ]
# Q19
@app.get("/enrollments/sort")
def sort_enrollments():
    return sorted(enrollments, key=lambda x: x.get("final_fee", 0))

# Q19
@app.get("/enrollments/page")
def paginate_enrollments(page: int = 1, limit: int = 3):
    total = len(enrollments)
    total_pages = (total + limit - 1) // limit

    if page > total_pages and total != 0:
        raise HTTPException(404, "Page not found")

    start = (page - 1) * limit
    end = start + limit

    return {
        "page": page,
        "total_pages": total_pages,
        "total": total,
        "data": enrollments[start:end]
    }

