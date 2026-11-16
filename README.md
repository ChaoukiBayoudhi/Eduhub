# Eduhub

Eduhub Django project.

## Tech stack

- Python 3
- Django
- Django REST Framework
- django-cors-headers
- Pillow
- Database: PostgreSQL

## Project structure

- `eduhub_project/eduhub_project/`: project settings and root URLs
- `eduhub_project/assignments_app/`: Django app
- `eduhub_project/course_app/`: Django app
- `eduhub_project/enrollments_app/`: Django app
- `eduhub_project/user_app/`: Django app
- Tests: `eduhub_project/assignments_app/tests.py`, `eduhub_project/course_app/tests.py`, `eduhub_project/enrollments_app/tests.py`, `eduhub_project/user_app/tests.py`

## Data model

| Model | App | Fields |
|---|---|---|
| `Assignment` | `eduhub_project/assignments_app` | id, lesson, student, assignment_date, status, created_at, updated_at |
| `Course` | `eduhub_project/course_app` | id, title, slug, description, status, price, created_at, updated_at, instructor |
| `Lesson` | `eduhub_project/course_app` | id, title, description, video_url, course, duration, order, content, created_at |
| `Enrollment` | `eduhub_project/enrollments_app` | id, student, course, enrollment_date, completion_date, status, created_at, updated_at |
| `User` | `eduhub_project/user_app` | id, username, email, password, birth_date, gender, user_type, bio, profile_picture, date_joined |
| `Instructor` | `eduhub_project/user_app` | grade_level |
| `Student` | `eduhub_project/user_app` | level, score |

## URL routes

Declared in `urls.py`:

- `/blog/`
- `/api/`
- `/courses/ (router)`
- `/lessons/ (router)`
- `/instructors/ (router)`
- `/students/ (router)`
- `/enrollments/ (router)`
- `/assignments/ (router)`

## How to run

```bash
cd eduhub_project
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r ../requirements.txt
python manage.py migrate
python manage.py runserver
```

`settings.py` is configured for PostgreSQL: create the database and use your own credentials before running `migrate`.

Then open `http://127.0.0.1:8000/`.

---

Author: [Chaouki Bayoudhi](https://github.com/ChaoukiBayoudhi)
