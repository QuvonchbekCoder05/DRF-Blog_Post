# UZ(Uzbekcha)
# Blog API with Django Rest Framework and JWT

Bu loyiha Django Rest Framework (DRF) va JWT (JSON Web Token) yordamida foydalanuvchi autentifikatsiyasi va bloglarni boshqarish imkonini beradi. API orqali foydalanuvchilar ro'yxatdan o'tish, tizimga kirish, blog yaratish, bloglarni tahrirlash, o'chirish va ularga kommentariya qoldirish imkoniyatiga ega bo'ladi.

## Texnologiyalar
- **Django** - Web dasturlash uchun asosiy framework.
- **Django Rest Framework (DRF)** - API yaratish va boshqarish uchun vosita.
- **Simple JWT** - JSON Web Token orqali autentifikatsiya.
- **SQLite** - Standart yengil ma'lumotlar bazasi.
- **Pillow** - Foydalanuvchi profiliga rasm yuklash uchun kutubxona.

## API Funktsiyalari:
1. **User Registration (Ro'yxatdan o'tish)**: Foydalanuvchi JWT token orqali tizimga kiradi.
2. **User Login (Tizimga kirish)**: Foydalanuvchilar JWT token orqali tizimga kirib, bloglarni boshqarishi mumkin.
3. **Blog CRUD**: Foydalanuvchilar blog yaratishi, ko'rishi, yangilashi va o'chirishi mumkin.
4. **Commenting System (Kommentariya qo'shish)**: Foydalanuvchilar bloglarga kommentariya qoldirish imkoniyatiga ega.
5. **Blog Likes (Layklar)**: Har bir blog uchun layklar soni qayd etiladi.
6. **My Blogs (Mening Bloglarim)**: Foydalanuvchilar faqat o'z bloglarini `/my-blogs/` orqali boshqaradi.

## Kutubxonalar
Loyihada ishlatilgan kutubxonalar:
- **djangorestframework**: `pip install djangorestframework`
- **djangorestframework-simplejwt**: `pip install djangorestframework-simplejwt`
- **Pillow**: `pip install Pillow`

## API Endpoints

### 1. Autentifikatsiya:
- **Sign Up**: `POST /api/signup/`
  - Kiritiladigan ma'lumotlar: `username`, `password`, `email`, `profile_image`, `bio`, `phone_number`.
- **Login**: `POST /api/token/`
  - Kiritiladigan ma'lumotlar: `username`, `password`.
  - Javob: JWT token.
- **Tokenni yangilash**: `POST /api/token/refresh/`.

### 2. Blog CRUD:
- **Bloglar ro'yxati va yaratish**: `GET /api/blogs/` va `POST /api/blogs/`.
- **Blog tafsilotlari, yangilash va o'chirish**: `GET /api/blogs/<id>/`, `PUT /api/blogs/<id>/`, `DELETE /api/blogs/<id>/`.

### 3. Kommentariya:
- **Komment qo'shish**: `POST /api/blogs/<id>/comment/`
  - Blogga kommentariya qo'shish uchun.

### 4. Mening Bloglarim:
- **Foydalanuvchining bloglari**: `GET /api/my-blogs/`
  - Foydalanuvchi faqat o'z bloglarini ko'rishi mumkin.

## Ma'lumotlar Bazasi
Ma'lumotlar SQLite'da saqlanadi va foydalanuvchilar, bloglar, kommentariyalar va layklar bilan bog'liq ma'lumotlarni saqlaydi.

## Misollar
API'ni **Postman** yoki **cURL** yordamida test qilish mumkin.

1. **Ro'yxatdan o'tish (Sign Up)**:
   ```bash
   POST /api/signup/
   Body:
   {
       "username": "newuser",
       "password": "password123",
       "email": "newuser@example.com",
       "phone_number": "+123456789",
       "bio": "This is my bio."
   }

# ENG(Inglizcha)

# Blog API with Django Rest Framework and JWT

This project provides a Blog API using Django Rest Framework (DRF) and JSON Web Token (JWT) authentication. It allows users to register, log in, create, update, delete blogs, and leave comments on blogs. Only authenticated users can manage their blogs.

## Technologies Used
- **Django** - Main web framework.
- **Django Rest Framework (DRF)** - Used to create and manage APIs.
- **Simple JWT** - Used for JSON Web Token authentication.
- **SQLite** - Default lightweight database.
- **Pillow** - Library for handling image uploads (used for profile images).

## API Features:
1. **User Registration**: Users register and log in using JWT tokens.
2. **User Login**: Users can log in with JWT and manage their blogs.
3. **Blog CRUD**: Users can create, view, update, and delete blogs.
4. **Commenting System**: Users can leave comments on blogs.
5. **Blog Likes**: Each blog can have a number of likes.
6. **My Blogs**: Authenticated users can manage their blogs via `/my-blogs/` endpoint.

## Installed Libraries
- **djangorestframework**: `pip install djangorestframework`
- **djangorestframework-simplejwt**: `pip install djangorestframework-simplejwt`
- **Pillow**: `pip install Pillow`

## API Endpoints

### 1. Authentication:
- **Sign Up**: `POST /api/signup/`
  - Required fields: `username`, `password`, `email`, `profile_image`, `bio`, `phone_number`.
- **Login**: `POST /api/token/`
  - Required fields: `username`, `password`.
  - Response: JWT token.
- **Token Refresh**: `POST /api/token/refresh/`.

### 2. Blog CRUD:
- **List and Create Blogs**: `GET /api/blogs/` and `POST /api/blogs/`.
  - Authenticated users can create a blog and view the list of blogs.
- **Blog Detail, Update, and Delete**: `GET /api/blogs/<id>/`, `PUT /api/blogs/<id>/`, `DELETE /api/blogs/<id>/`.
  - View, update, or delete a specific blog.

### 3. Comments:
- **Add Comment**: `POST /api/blogs/<id>/comment/`
  - Authenticated users can leave a comment on blogs.

### 4. My Blogs:
- **User's Blogs**: `GET /api/my-blogs/`
  - Authenticated users can view and manage only their own blogs.

## Database
The project uses **SQLite** to store user, blog, comments, and like-related data.

## Examples
You can test the API using **Postman** or **cURL**.

1. **Sign Up**:
   ```bash
   POST /api/signup/
   Body:
   {
       "username": "newuser",
       "password": "password123",
       "email": "newuser@example.com",
       "phone_number": "+123456789",
       "bio": "This is my bio."
   }

  
