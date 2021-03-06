from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    class Ara:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
class Products(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(null=True,blank=True,verbose_name="Описание")
    price = models.FloatField(verbose_name="Цена")
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,verbose_name="Категория")

    class Ara:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.title

class Reciew(models.Model):
    text = models.TextField(verbose_name="Текст")
    product = models.ForeignKey(Products,
                                on_delete=models.CASCADE, verbose_name="Продукт")
    class Ara:
        verbose_name = "Обзор"
        verbose_name_plural = "Обзоры"

    def __str__(self):
        return self.text

