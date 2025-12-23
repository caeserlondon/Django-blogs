# My Django Blog

A simple, feature-rich blog application built with **Django 5**. Supports user authentication, draft posts, publishing, comments, and Bootstrap-based responsive design.

## ✨ Features

- User registration & login (via Django’s built-in auth system)
- Create, edit, view, and delete blog posts
- Save posts as **drafts** (unpublished) or **publish** them
- Comment system with moderation (approve/remove comments)
- Responsive UI with Bootstrap 5 and Bootstrap Icons
- Clean URL routing with namespaced app URLs

## 🛠️ Technologies Used

- **Backend**: Python 3.14, Django 5.2
- **Frontend**: HTML5, CSS3, Bootstrap 5, Bootstrap Icons
- **Database**: SQLite (default – suitable for development)

## 🚀 Getting Started

### 🗂️ Project Structure

mysite/ – Main Django project settings and root URLs
blog/ – Django app containing models, views, and templates
templates/ – Not used (templates are inside blog/templates/)
blog/templates/blog/ – All HTML templates for the blog

###  🔐 Authentication

Login: /login/
Logout: /logout/ (uses GET for simplicity in development)
Only authenticated users can:
Create new posts
View drafts
Publish or edit their posts

###  📝 License

This project is for educational and personal use. No license specified — feel free to modify and learn!

Made with ❤️ by Caeser Ibrahim
