from django.db import models


class Pizza(models.Model):
    name = models.CharField(
        max_length=80,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Pizza'
        verbose_name_plural = 'Pizzas'


class Topping(models.Model):
    pizza = models.ForeignKey(
        'pizzeria.Pizza',
        on_delete=models.CASCADE,
        related_name='toppings',
    )

    name = models.CharField(
        max_length=80,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Topping'
        verbose_name_plural = 'Toppings'
