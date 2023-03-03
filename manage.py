#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # Set the DJANGO_SETTINGS_MODULE environment variable to your project's settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoBazar.settings')
    try:
        # Try to import the execute_from_command_line function from Django's management package
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # If the import fails, raise an ImportError with an informative error message
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Call the execute_from_command_line function with the command-line arguments
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
