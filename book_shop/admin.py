from django.contrib import admin

# Register your models here.
from book_shop.models import Role


class RoleAdmin(admin.ModelAdmin):
    fields = ['role_name', 'role_code']


admin.site.register(Role, RoleAdmin)
