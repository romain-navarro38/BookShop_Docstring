from django.db import models
from django.utils.text import slugify

from store.validators import validate_isbn, clean_isbn_code


def get_default_author():
    return Author.objects.get_or_create(name='Inconnu')[0]


def get_default_publisher():
    return Publisher.objects.get_or_create(name='Inconnu')[0]


class Author(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Nom complet')
    slug = models.SlugField(max_length=150, blank=True)

    class Meta:
        verbose_name = "Auteur"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.name)
        super().save(*args, **kwargs)


class Publisher(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Maison d'édition")
    slug = models.SlugField(max_length=150, blank=True)

    class Meta:
        verbose_name = "Editeur"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.name)
        super().save(*args, **kwargs)


class Book(models.Model):
    author = models.ForeignKey(Author,
                               on_delete=models.SET(get_default_author),
                               null=True,
                               blank=True,
                               verbose_name='Auteur')
    publisher = models.ForeignKey(Publisher,
                                  on_delete=models.SET(get_default_publisher),
                                  null=True,
                                  blank=True,
                                  verbose_name="Maison d'édition")
    title = models.CharField(max_length=150, verbose_name='Titre')
    slug = models.SlugField(max_length=150, blank=True)
    isbn = models.CharField(max_length=17,
                            unique=True,
                            blank=True,
                            null=True,
                            verbose_name='N° ISBN',
                            validators=[validate_isbn])
    resume = models.TextField(blank=True, verbose_name='Résumé')
    pages = models.IntegerField(default=0, verbose_name='Nombre de pages')
    publication_date = models.DateField(blank=True, null=True, verbose_name="Paru le")
    price = models.FloatField(default=0.0, verbose_name='Prix')
    quantity = models.IntegerField(default=0, verbose_name='Quantité')

    class Meta:
        verbose_name = "Livre"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.author = self.author or get_default_author()
        self.publisher = self.publisher or get_default_publisher()
        self.slug = self.slug or slugify(self.title)
        self.isbn = clean_isbn_code(self.isbn)

        super().save(*args, **kwargs)


class Category(models.Model):
    books = models.ManyToManyField(Book, verbose_name="Classements")
    name = models.CharField(max_length=100, verbose_name="Nom")

    class Meta:
        verbose_name = "Catégorie"

    def __str__(self):
        return self.name


class Thumbnail(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Livre")
    thumbnail = models.ImageField(upload_to='books', blank=True, null=True, verbose_name='Chemin')

    class Meta:
        verbose_name = 'Image'

    def __str__(self):
        return f"{self.book.title} ({self.thumbnail.url})"
