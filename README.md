# Login

- username: aliahadmd3
- password: aliahadmd3

please don't delete any data from the admin.


# Django Newsletter Management System

A robust and user-friendly newsletter management system built with Django. This application allows you to create, manage, and send newsletters to subscribers, with features like rich text editing, subscriber management, and email tracking.

## Features

- User-friendly subscriber management
- Rich text newsletter creation and editing using Summernote
- Secure token-based unsubscribe mechanism
- Email tracking (sent and opened status)
- Responsive design using Django Widget Tweaks
- Admin interface for easy management

## Technologies Used

- Django 5.0.6
- Python 3.x
- django-environ for environment variable management
- django-summernote for rich text editing
- django-widget-tweaks for form rendering
- SQLite for development and testing
- PostgreSQL/MySQL for production

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/django-newsletter-system.git
   cd django-newsletter-system
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your environment variables:
   ```
   DEBUG=True
   SECRET_KEY=your_secret_key
   EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
   EMAIL_HOST=your_smtp_host
   EMAIL_PORT=587
   EMAIL_USE_TLS=True
   EMAIL_HOST_USER=your_email@example.com
   EMAIL_HOST_PASSWORD=your_email_password
   DEFAULT_FROM_EMAIL=your_email@example.com
   ```

5. Run migrations:
   ```
   python manage.py migrate
   ```

6. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```

8. Visit `http://127.0.0.1:8000/admin/` to access the admin panel and start managing your newsletters.

## Usage

1. Create newsletters using the admin interface or the provided views.
2. Manage subscribers through the admin panel or the subscription form.
3. Send newsletters to all active subscribers.
4. Track sent newsletters and open rates.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

