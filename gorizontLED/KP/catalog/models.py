from django.contrib.auth.models import User, Group

from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances


class Genre(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Book(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file.
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN',max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title


    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('book-detail', args=[str(self.id)])
    
    def display_genre(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
    display_genre.short_description = 'Genre'

class BookInstance(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be borrowed from the library).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')

    class Meta:
        ordering = ["due_back"]


    def __str__(self):
        """
        String for representing the Model object
        """
        return '%s (%s)' % (self.id,self.book.title)

class Author(models.Model):
    """
    Model representing an author.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])


    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.last_name, self.first_name)
# моё.
class Meneger(models.Model):
    """
    Model representing an meneger.
    """
    first_name = models.CharField(max_length=100)
    patronymic_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)

    def get_absolute_url(self):
        """
        Returns the url to access a particular meneger instance.
        """
        return reverse('meneger-detail', args=[str(self.id)])


    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s, %s' % (self.last_name, self.first_name, self.patronymic_name)
    
    class Meta:
        ordering = ["last_name", "first_name"]

class LedDisplayModule(models.Model):
    name = models.CharField(max_length=200, help_text="Название модуля")
    manufacturer = models.CharField(max_length=200, help_text="Производитель")
    ENVIRONMENT_STATUS = (
        ('i', 'Indoor'),
        ('o', 'Outdoor'),
        ('f', 'Flexible'),
    )
    operationEnvironment = models.CharField(max_length=10, choices=ENVIRONMENT_STATUS, blank=True, default='i', help_text='Рабочая среда')
    pixelPitch = models.FloatField(help_text='Шаг пикселя')
    width = models.IntegerField(help_text='Ширина модуля в мм.')
    height = models.IntegerField(help_text='Высота модуля в мм.')
    depth = models.FloatField(help_text='Глубина модуля в мм.')
    horizontalViewingAngle = models.IntegerField(help_text='Горизонтальный угол обзора')
    verticalViewingAngle = models.IntegerField(help_text='Вертикальный угол обзора')
    bestViewingDistance = models.IntegerField(help_text='Лучшее расстояние для просмотра в м')
    ledLamp = models.CharField(max_length=20, blank=True, help_text='Тип светодиода')
    refreshFrequency = models.IntegerField(help_text='Частота обновления')
    brightness = models.IntegerField(help_text='Яркость cd/㎡')
    drivingMethod = models.CharField(max_length=10, blank=True, help_text='Режим сканирования')
    lifeSpan = models.IntegerField(help_text='Срок службы в часах')
    powerConsumption = models.IntegerField(help_text='Мощность модуля в Вт.')


    def __str__(self):
        return self.name

    class Meta:
        ordering = ["pixelPitch", "operationEnvironment"]

class komPr(models.Model):
    id = models.IntegerField(help_text='Id', primary_key=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)