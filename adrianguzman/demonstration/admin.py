from .utility import register_table
import django.apps

# Obtain a list of unique tables in `models.py`
tables = set(django.apps.apps.get_models())

# Iterate through each table and register it to the admin page.
for table in tables:
    register_table(table)

