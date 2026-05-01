 Social Canvas

A command-line event management system built with Python and MySQL. 

Social Canvas allows users to create, view, update, and delete events — with data persisted in a real MySQL database.

 Features

- Add Events — create new events with name, date, type, location, and budget
- View Events — list all events sorted by date with full details
- Update Event Status — track progress from planning through to completion
- Delete Events — remove events with a confirmation prompt
- MySQL Integration — all data stored persistently in `social_canvas_db`
- Secure Config — database credentials managed via `.env` file

Tech Stack

- Language: Python 3
- Database: MySQL
- Libraries: `mysql-connector-python`, `python-dotenv`

---

Getting Started

Prerequisites

- Python 3.x
- MySQL (with `social_canvas_db` database set up)
- pip

Installation

```bash
git clone https://github.com/Francesscodes/Social-Canvas-.git
cd Social-Canvas-
```

Install dependencies

```bash
pip install mysql-connector-python python-dotenv
```

 Configure your `.env` file

Create a `.env` file in the root of the project:

```env
DB_HOST=127.0.0.1
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_NAME=social_canvas_db
```

Run the app

```bash
python socialcanvas.py
```

---

Usage

```
--- Social Canvas: Event Management ---
1. Add Event
2. View Events
3. Update Event Status
4. Delete Event
5. Exit
```

 Adding an event

```
Enter event name: Lagos Tech Summit 2026
Enter event date (YYYY-MM-DD): 2026-07-25
Event types: wedding, corporate, birthday
Enter event type: corporate
Enter location: Ikoyi, Lagos
Enter budget (or press Enter to skip): 5000000
Enter user ID: 1
```

Event types supported

| Type | Description |
|---|---|
| `wedding` | Wedding ceremonies and receptions |
| `corporate` | Business events, conferences, summits |
| `birthday` | Birthday parties and celebrations |

 Event statuses

| Status | Description |
|---|---|
| `planning` | Default status on creation |
| `ongoing` | Event is currently in progress |
| `completed` | Event has ended |
| `cancelled` | Event was cancelled |

---

 Database Schema

The app connects to the `events` table in `social_canvas_db`:

| Column | Type | Description |
|---|---|---|
| `event_id` | INT | Primary key, auto-increment |
| `user_id` | INT | Foreign key referencing `users` |
| `event_name` | VARCHAR(255) | Name of the event |
| `event_type` | ENUM | wedding, corporate, birthday |
| `event_date` | DATE | Date of the event |
| `location` | VARCHAR(255) | Venue or location |
| `budget` | DECIMAL(10,2) | Estimated budget (optional) |
| `status` | ENUM | planning, ongoing, completed, cancelled |
| `created_at` | TIMESTAMP | Auto-generated on insert |

---

 Project Structure

```
Social-Canvas-/
├── socialcanvas.py      # Main application
├── socialcanvasdb.py    # Database helper
├── insert_user.py       # Script to seed a test user
├── .gitignore           # Excludes .env and sensitive files
├── .env                 # Your local credentials (not committed)
└── README.md
```

Security

- Database credentials are stored in `.env` and never committed to GitHub
- `.gitignore` is configured to exclude `.env` and other sensitive files

 Author 
 Francess Ekezie

Built by [Francesscodes](https://github.com/Francesscodes)

---

## License

MIT License — free to use and modify.
