from django.db import models

from config.settings import AUTH_USER_MODEL
from store.models import Book


class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='client')
    create_date = models.DateTimeField(blank=True, null=True, verbose_name='Date de création')

    class Meta:
        verbose_name = 'Panier'

    def __str__(self):
        return f'Panier de {self.user}'


class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Client')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Livre')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='Panier')
    quantity = models.IntegerField(default=1, verbose_name='Quantité')
    ordered = models.BooleanField(default=False, verbose_name='Commandée')
    ordered_date = models.DateTimeField(blank=True, null=True, verbose_name='Date commande')

    class Meta:
        verbose_name = 'Commande'

    def __str__(self):
        return f'{self.user} : {self.book.title} ({self.quantity})'


class Wish(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Client')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Livre')
    add_date = models.DateTimeField(blank=True, null=True, verbose_name="Date d'ajout")

    class Meta:
        verbose_name = 'Souhait'

    def __str__(self):
        return f'{self.user} : {self.book.title}'
