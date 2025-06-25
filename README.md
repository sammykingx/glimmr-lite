# 🧼 Glimmr Lite – Cleaning Service Booking MVP

**Glimmr Lite** is the minimal yet powerful MVP of the Glimmr App — a modern, tech-forward web application for booking professional cleaning services. This version focuses on **streamlining client bookings** and syncing them to **Google Calendar**, ensuring both clients and service providers stay aligned in real-time.

> This MVP is crafted for early validation, rapid deployment, and client interaction, a crucial foundation for Glimmr’s full-featured Django application.

---

## 🚀 Key Features

- ✅ **Client Booking Portal** – Seamless, mobile-friendly form for customers to request cleaning services.
- 📅 **Google Calendar Integration** – Automatically adds confirmed bookings to both client and provider calendars.
- ⚡️ **Real-time Interactions** – Powered by [HTMX](https://htmx.org) for fast, dynamic UX without page reloads.
- 🎨 **Tailwind CSS UI** – Clean, modern design system with minimal custom CSS.
- 🌐 **HTML-first Architecture** – Simple, maintainable, and production-ready.

---

## 🛠️ Technology Stack

| Tech         | Purpose                                 |
|--------------|-----------------------------------------|
| **Flask**    | Lightweight backend and routing         |
| **HTMX**     | Frontend interactivity without JS-heavy SPA frameworks |
| **Tailwind CSS** | Utility-first styling for clean, responsive UI |
| **HTML5**    | Semantically structured markup          |
| **Google Calendar API** | Two-way scheduling integration |

---


---

## 🌟 Vision Behind Glimmr

Glimmr is not just a booking platform — it’s a scalable **service operations engine** for modern home and office cleaning providers. Glimmr Lite serves as a tactical MVP to:

- Validate user workflows
- Simplify the client-provider relationship
- Build a tech-first foundation for automation and smart scheduling

> This MVP captures the *essence* of Glimmr’s operational goals while preparing for its migration to a **robust Django-based platform**.

---

## 🔐 Google Calendar Integration (Overview)

This MVP leverages the **Google Calendar API** to:

- 📩 Create calendar events upon booking submission
- ⏰ Set automated reminders for both clients and organization
- 🔁 Avoid double-booking and scheduling conflicts

---

## 🧪 Running Locally

- **Clone the repo**
```bash
git clone https://github.com/sammykingx/glimmr-lite.git
cd glimmr-lite
```

- **Setting up environments**
1. using **PIP** as package manager
  - Create virtual environments
```bash
python3 -m venv venv
source venv/bin/activate
```
- Install project Dependencies
```bash
pip install -r requirements.txt
```
- Run the app
```bash
# using python
python main.py

# using flask management command
flask run
```

2. Using UV
- Install dependencies
```bash
uv sync
```
- Run app
```bash
uv run main.py
```

## 🧱 MVP Roadmap

- Booking form UI & validation
- Basic calendar integration
- Confirmation emails
- Transition logic to Django-based core
