# 📚 Bookstore Management System

A Django-based full stack web application that allows users to browse and purchase books. Admins can manage the book inventory via a custom-built admin panel. The project strictly follows Class-Based Views (CBV), uses Django sessions for cart management, and avoids Django forms and admin.

---

## 🔧 Tech Stack

- Backend: Django (Python)
- Frontend: HTML, CSS, avaScript

- DevOps: Docker, Docker Compose, Jenkins (CI/CD)

---

## 🚀 Features

### 🔐 Authentication
- User Registration (manual form handling)
- User Login/Logout

### 🛍️ User Functionality
- Browse all available books
- View individual book details
- Add books to cart (session-based)

### 🛠️ Admin Panel
- Custom admin dashboard (no Django admin)
- Add/Edit/Delete books
- Inventory management

---

## 🐳 Docker & Jenkins

### Docker
- `Dockerfile` included for app containerization
- `docker-compose.yml` for simplified local setup

### Jenkins
- `Jenkinsfile` included for automated build, test, and deploy pipeline

---

## 🛠️ Setup Instructions

```bash
# Clone the repository
git clone https://github.com/nilam-10/book-store-final
cd bookstore

# Run using Docker
docker-compose up --build
open at http://localhost:8000/

## Project Structure
![image](https://github.com/user-attachments/assets/454ccb69-1fe4-4337-be3d-140201187584)

