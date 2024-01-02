from django.contrib import admin

# Register your models here.


class MyModelAdmin(admin.ModelAdmin):
    readonly_fields = ()
