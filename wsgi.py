"""WSGI entry point for production servers (Gunicorn/uWSGI)."""

from src.api.app import app


if __name__ == "__main__":
    app.run()
