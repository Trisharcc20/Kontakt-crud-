# Kontakt — Contacts Manager

A lightweight full-stack CRUD web application for managing contacts, built with **Flask**, **SQLAlchemy**, and vanilla **JavaScript**.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the App](#running-the-app)
- [API Reference](#api-reference)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

Kontakt is a single-page contacts management app with a clean sidebar layout. It lets you create, view, edit, and delete contact records — complete with live search, status toggling, and toast notifications — all backed by a RESTful Flask API and a SQLite database.

---

## Features

- ✅ **Full CRUD** — Create, Read, Update, and Delete contacts
- 🔍 **Live search** — Filter contacts by name, email, or role in real time
- 🟢 **Status management** — Toggle contacts between Active and Inactive
- 📊 **Dashboard stats** — Sidebar displays total and active contact counts
- 🔔 **Toast notifications** — Instant feedback on every action
- 🪪 **Avatar initials** — Auto-generated color-coded avatars per contact
- 🗄️ **Persistent storage** — SQLite database via Flask-SQLAlchemy
- 🌱 **Seed data** — Sample contacts loaded automatically on first run

---

## Tech Stack

| Layer    | Technology                  |
|----------|-----------------------------|
| Backend  | Python 3, Flask             |
| ORM      | Flask-SQLAlchemy            |
| Database | SQLite                      |
| Frontend | HTML5, CSS3, Vanilla JS     |
| Fonts    | Google Fonts (Syne, DM Sans)|

---

## Project Structure

```
crud_app/
├── app.py                  # Flask app, routes, and database models
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html          # Single-page HTML template
└── static/
    ├── css/
    │   └── style.css       # App styles
    └── js/
        └── app.js          # Frontend logic (fetch API, DOM updates)
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- `pip` (Python package manager)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/crud_app.git
   cd crud_app
   ```

2. **Create and activate a virtual environment** (recommended)

   ```bash
   python -m venv venv

   # macOS / Linux
   source venv/bin/activate

   # Windows
   venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

### Running the App

```bash
python app.py
```

The app will start in debug mode. Open your browser and navigate to:

```
http://127.0.0.1:5000
```

The SQLite database (`contacts.db`) is created automatically on first run, and three sample contacts are seeded if the database is empty.

---

## API Reference

All endpoints are prefixed with `/api`.

| Method   | Endpoint                    | Description                  |
|----------|-----------------------------|------------------------------|
| `GET`    | `/api/contacts`             | Get all contacts (supports `?search=` query param) |
| `POST`   | `/api/contacts`             | Create a new contact         |
| `GET`    | `/api/contacts/<id>`        | Get a single contact by ID   |
| `PUT`    | `/api/contacts/<id>`        | Update a contact by ID       |
| `DELETE` | `/api/contacts/<id>`        | Delete a contact by ID       |

### Contact Schema

```json
{
  "id": 1,
  "name": "Arjun Sharma",
  "email": "arjun.sharma@example.com",
  "phone": "+91 98765 43210",
  "role": "Developer",
  "status": "Active",
  "created_at": "Jun 07, 2026"
}
```

> **Required fields:** `name`, `email`  
> `email` must be unique across all contacts.

---

## Usage

- Click **Add Contact** to open the creation modal.
- Fill in the name (required), email (required), phone, role, and status.
- Click the **edit icon** on any row to update a contact.
- Click the **trash icon** to delete a contact (with confirmation).
- Use the **search bar** to filter contacts by name, email, or role.

---

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## License

This project is open source and available under the [MIT License](LICENSE).

