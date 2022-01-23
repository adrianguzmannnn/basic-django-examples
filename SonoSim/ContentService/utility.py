"""A utility file to handle the auto-registering of Admin pages."""
from django.contrib import admin


def get_fields(table):
    """Return the fields of a model."""
    # Not ideal to access a protected member.
    return [field.name for field in set(table._meta.fields)] 


def register_table(table):
    """Perform the registering of tables in the Admin page."""
    class Admin(admin.ModelAdmin):
        """A default class for each model."""
        list_display = get_fields(table)
    try:
        admin.site.register(table, Admin)
    except admin.sites.AlreadyRegistered:
        # Perform logging here.
        pass
