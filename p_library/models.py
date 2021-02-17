from django.db import models
from django.contrib.auth.models import User  

# Create your models here.
class Author(models.Model):  
    full_name = models.TextField(verbose_name='Автор')  
    birth_year = models.SmallIntegerField(verbose_name='Год рождения')  
    country = models.CharField(max_length=2, verbose_name='Страна')

    class Meta:
        verbose_name_plural = 'Авторы'
        verbose_name = 'автор'
        ordering = [ 'full_name' ]

    def __str__(self):
        return self.full_name


class Book(models.Model):  
    ISBN = models.CharField(max_length=13, verbose_name='Междунар. код')  
    title = models.TextField(verbose_name='Наименование')  
    description = models.TextField(verbose_name='Аннотация')  
    year_release = models.SmallIntegerField(verbose_name='Издание')  
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, verbose_name='Автор', related_name='books_author')
    copy_count = models.SmallIntegerField(default=1, verbose_name='Экз')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')
    publisher = models.ForeignKey('Publisher', on_delete=models.SET_NULL, null=True, verbose_name='Издательство', related_name='books_publisher')
    cover_art = models.ImageField(upload_to='cover_book', blank=True, verbose_name='Обложка')

    class Meta:
        verbose_name_plural = 'Книги'
        verbose_name = 'книга'
        ordering = [ 'publisher' ]

    def __str__(self):
        return self.title

class Publisher(models.Model):
    title = models.CharField(max_length=20, verbose_name='Издательство')
    country = models.CharField(max_length=2, verbose_name='Страна')

    class Meta:
        verbose_name_plural = 'Издательства'
        verbose_name = 'издательство'
        ordering = [ 'title' ]

    def __str__(self):
        return self.title

class Friend(models.Model):
    full_name = models.CharField(max_length=30, verbose_name="Имя")
    phone = models.CharField(max_length=16, blank=True, verbose_name="Телефон")
    email = models.EmailField(blank=True, verbose_name="Email")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'Друзья'
        verbose_name = 'друг'
        ordering = [ 'full_name' ]

import uuid

class BookInstance(models.Model):
    """
    Копии книг
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Уникальный номер книги")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True, verbose_name="Книга")
    friend = models.ForeignKey('Friend', on_delete=models.SET_NULL, null=True, verbose_name="У кого", related_name='books')
    data = models.DateField(null=True, blank=True, verbose_name="Дата")

    class Meta:
        verbose_name_plural = 'Экземпляры'
        verbose_name = 'экземпляр'
        ordering = ["book"]

    def __str__(self):
        return '%s (%s)' % (self.id, self.book.title)
    
    def instance(self):
        return '%s (%s)' % (self.book.title, self.id)
    instance.short_description = 'Экземпляр'

    def book_list(self):
        return '%s, %s' % (self.friend, self.data)
    book_list.short_description = 'У кого на руках'  

  
class UserProfile(models.Model):  
    age = models.IntegerField()  
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')    


    
      