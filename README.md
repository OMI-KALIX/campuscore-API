# 🎓 CampusCore API

![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?logo=postgresql)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![Pydantic](https://img.shields.io/badge/Pydantic-Validation-E92063)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)
![Render](https://img.shields.io/badge/Render-Deployed-46E3B7?logo=render)
![License](https://img.shields.io/badge/License-MIT-green)
[![Docker Pulls](https://img.shields.io/docker/pulls/omikalix/campuscore-api?style=flat-square&logo=docker&label=Docker%20Pulls)](https://hub.docker.com/r/omikalix/campuscore-api)
[![Docker Image Size](https://img.shields.io/docker/image-size/omikalix/campuscore-api/latest?style=flat-square&logo=docker&label=Image%20Size)](https://hub.docker.com/r/omikalix/campuscore-api)

A lightweight Student Management REST API built with FastAPI, PostgreSQL, SQLAlchemy, and Pydantic.

This project demonstrates modern backend development practices by implementing a fully functional CRUD-based Student Management System with PostgreSQL database integration, SQLAlchemy ORM, and robust request validation using Pydantic. The application follows a clean and modular architecture, supports containerized deployment with Docker, and can be deployed to cloud platforms such as Render. Designed as a learning and portfolio project, it provides a scalable foundation for building larger backend services while showcasing industry-standard tools and development workflows.

---

## 🔗 Links

* 🌐 Live API: https://your-app.onrender.com
* 📚 Swagger UI: https://your-app.onrender.com/docs
* 📖 ReDoc: https://your-app.onrender.com/redoc
* 🐳 Docker Hub: https://hub.docker.com/r/omikalix/campuscore-api
  
---

## ✨ Features

* ➕ Create Student
* 📖 Get All Students
* 🔍 Get Student By ID
* ✏️ Update Student
* 🩹 Partial Update Student
* 🗑️ Delete Student
* 🌱 Seed Sample Data
* 📚 Interactive API Documentation
* 🐘 PostgreSQL Integration
* 🏗️ SQLAlchemy ORM
* 🐳 Docker Support
* ☁️ Render Deployment

---

## 📸 Screenshots

### API Endpoints

![Endpoints](students/docs/endpoints.png)

### PostgreSQL Database

![PostgreSQL](students/docs/postgresql.png)

---

## 🏗️ Project Structure

```text
students/
│
├── .env
├── .gitignore
├── Dockerfile
├── requirements.txt
├── README.md
├── LICENSE
│
├── main.py
├── database.py
├── models.py
├── schemas.py
└── students.py
```

---

## ⚙️ Quick Start

### Clone Repository

```bash
git clone <repository-url>
cd students
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment

```env
DATABASE_URL=postgresql://username:password@localhost:5432/students1
```

### Run

```bash
uvicorn main:app --reload
```

---

## 🐳 Docker

### Pull Image

```bash
docker pull omikalix/campuscore-api
```

### Run with Local PostgreSQL

```bash
docker run -p 8000:8000 -e DATABASE_URL="postgresql://username:password@host.docker.internal:5432/students1" omikalix/campuscore-api
```

### Run with Render PostgreSQL

```bash
docker run -p 8000:8000 -e DATABASE_URL="<your_render_postgresql_connection_string>" omikalix/campuscore-api
```

### Access API

```text
http://localhost:8000
```

### Swagger UI

```text
http://localhost:8000/docs
```

### ReDoc


```text
http://localhost:8000/redoc
```

---

## 🚀 Render Deployment

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

### Environment Variable

```env
DATABASE_URL=<render_postgresql_connection_string>
```

---

## 📌 Endpoints

| Method | Endpoint       |
| ------ | -------------- |
| GET    | /              |
| GET    | /health        |
| POST   | /seed          |
| POST   | /students      |
| GET    | /students      |
| GET    | /students/{id} |
| PUT    | /students/{id} |
| PATCH  | /students/{id} |
| DELETE | /students/{id} |

---

## 📝 Notes

### Docker + Local PostgreSQL

When running PostgreSQL locally and FastAPI inside Docker, use:

```text
host.docker.internal
```

instead of:

```text
localhost
```

because `localhost` inside a container refers to the container itself.

### Dynamic Database Configuration

The application reads the database connection string from:

```env
DATABASE_URL
```

This allows the same codebase and Docker image to work with:

* Local PostgreSQL
* Render PostgreSQL
* Railway PostgreSQL
* AWS RDS
* Azure PostgreSQL

without code changes.

---

## 🔮 Future Enhancements

* 🔐 Authentication & Authorization
* 📦 Alembic Migrations
* 📄 Pagination
* 🔍 Search & Filtering

---

## 📜 License

This project is licensed under the MIT License.
