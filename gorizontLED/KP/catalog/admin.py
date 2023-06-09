from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Meneger, LedDisplayModule, komPr


# admin.site.register(Author)
# admin.site.register(Book)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Meneger)
admin.site.register(LedDisplayModule)
admin.site.register(komPr)

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')


# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# admin.site.register(Book, BookAdmin)

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

# Register the Admin classes for BookInstance using the decorator

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass

