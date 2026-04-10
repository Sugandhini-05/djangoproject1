from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'age')   # columns shown in admin
    search_fields = ('name', 'email')              # search bar
    list_filter = ('age',)                         # filter sidebar
    ordering = ('id',)                             # default ordering