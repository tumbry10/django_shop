# 🛍️ Mhamha's Cosmetic Shop Inventory System

A Django-based inventory and sales management system built for a small backyard cosmetic shop.  
This system handles stock management, sales tracking, invoicing, and user role management with a clean backend structure.

---

## 📌 Features

### ✅ User Management (`accounts` app)
- Custom user model extending Django’s `AbstractUser`
- Two user roles:
  - **SystemAdmin** (superuser)
  - **SalesRep** (normal user)
- Separate profile models for SystemAdmin and SalesRep linked via one-to-one relationship
- Role-based dashboard views
- User registration via a web form for SalesReps

---

### ✅ Product & Brand Management (`my_shop` app)
- Products are categorized by **Brand**
- CRUD functionality for both Brands and Products
- Product image uploads (brand logos)
- Admin can manage product and brand records via the system

---

### ✅ Stock Receiving
- SalesReps can record stock-in transactions
- Multiple products can be received at once via formsets
- Automatically updates product in-house stock quantities
- Generates a stock-in receipt/summary after each stock receiving

---

### ✅ Sales Management
- SalesReps can record sales transactions with multiple items per sale
- Automatically reduces in-house stock quantities for each sale
- Prevents selling out-of-stock products
- Generates a printable sales invoice for each sale

---

### ✅ Low Stock Alert System
- Products with stock levels below a set threshold appear in a dashboard alert section
- Threshold value set per product (default: 5 units)
- Visible on both SystemAdmin and SalesRep dashboards

---

## 📊 Dashboards

### 📌 SystemAdmin Dashboard
- Total products
- Total brands
- Total users
- Total stock-ins
- Total sales made
- Low stock product alerts

### 📌 SalesRep Dashboard
- Total sales made by this SalesRep
- Total stock-ins done by this SalesRep
- Number of product types available
- Latest 5 sales made by this SalesRep
- Low stock product alerts

---

## 📦 Tech Stack

- **Backend:** Django 5.2.4
- **Database:** MySQL
- **Authentication:** Django’s custom `AbstractUser` model
- **Frontend (current):** Django templates  
- **Planned UI:** Bootstrap 5 + Vanilla JS (no frontend frameworks yet)

---

## 📌 Next Steps (Planned)

- 🎨 Build out the UI using **Bootstrap 5**
- ✨ Add dynamic interactivity with **Vanilla JS**
- 📊 Add charts for sales summaries (possibly Chart.js)
- 📑 Implement PDF generation for invoices
- 📄 Add CSV/Excel export for sales and stock reports
- 📧 (Optional) Email notifications for low stock alerts
- 🖥️ Deploy to a live server (Heroku, PythonAnywhere, or Render)

---

## 📚 Requirements

- Python 3.13+
- Django 5.2.4+
- Pillow (for image uploads)

**Install dependencies:**
```bash
pip install -r requirements.txt
