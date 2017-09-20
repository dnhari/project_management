from django.contrib import admin

# Register your models here.
from .models import Book,MultipleBooks,MultiAuthoeBooks,User_extra

admin.site.register(Book)
admin.site.register(MultipleBooks)
admin.site.register(MultiAuthoeBooks)
admin.site.register(User_extra)