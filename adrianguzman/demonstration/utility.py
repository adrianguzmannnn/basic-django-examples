from django.contrib import admin


def get_fields(table):
    return [field.name for field in set(table._meta.fields)]


def register_table(table):

    class Admin(admin.ModelAdmin):

        list_display = get_fields(table)

    try:
        admin.site.register(table, Admin)
    except admin.sites.AlreadyRegistered:
        pass
