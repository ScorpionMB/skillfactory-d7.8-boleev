from django.contrib import admin
from .models import Book, Author, Publisher, Friend, BookInstance, UserProfile  

@admin.register(UserProfile)  
class ProfileAdmin(admin.ModelAdmin):  
    pass

# Register your models here.
class BookInstanceInline(admin.TabularInline):
    extra=0
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    inlines = [BookInstanceInline]
    list_display = ('title', 'description', 'author', 'year_release', 'publisher', 'copy_count', 'price')
    list_display_links = ('title', 'author', 'publisher')
    search_fields = ('title', 'description')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_year', 'country')
    list_display_links = ('full_name', 'birth_year')
    search_fields = ('full_name', 'birth_year', 'country')

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('title', 'country')
    list_display_links = ('title', 'country')
    search_fields = ('title', 'country')

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'email')

@admin.register(BookInstance)
class BookBookInstanceAdmin(admin.ModelAdmin):
    list_display = ('instance', 'friend', 'data')





    
