# main_django.py

import os
import sys
from django.core.management import execute_from_command_line

# Set up the Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
try:
    import django
    django.setup()
except ImportError:
    print("Django is not installed. Please install it using 'pip install django'")
    sys.exit(1)

# Basic Django app setup
if __name__ == '__main__':
    execute_from_command_line(sys.argv)