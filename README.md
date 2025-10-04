# E-commerce Product API (Django + DRF)

This is a backend **E-commerce Product API** built with **Django** and **Django REST Framework (DRF)**.  
It provides endpoints for **user authentication, product management (CRUD), and search/filtering**.  

The project mimics a real-world backend developer workflow, including **JWT authentication, product categories, search functionality, and deployment**.

---

## Features
- User Registration & Authentication (JWT).
- CRUD operations for products:
  - Name, Description, Price, Category, Stock Quantity, Image URL, Created Date.
- Product search by **name** or **category** (partial matches supported).
- Product filtering by **category, price range, stock availability**.
- Pagination for large product lists.
- Admin-only access for product creation, updates, and deletion.
- API documentation with Swagger/OpenAPI.

---

## Tech Stack
- [Django](https://www.djangoproject.com/) (Backend Framework)
- [Django REST Framework](https://www.django-rest-framework.org/) (API Layer)
- [SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) (Authentication)
- [PostgreSQL](https://www.postgresql.org/) (Database – recommended for production)
- [Heroku](https://www.heroku.com/) or [Render](https://render.com/) (Deployment)

---

