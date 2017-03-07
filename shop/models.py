from django.db import models

# Create your models here.


class LookBookPage(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='lookbook_item/', blank=True, verbose_name="Изображение для лукбука")
    type = models.CharField(max_length=100, db_index=True, default='portrait')

    class Meta:
        ordering = ['name']
        verbose_name = 'LookBook Item'
        verbose_name_plural = 'LookBook Items'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', verbose_name='Категории')
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название товара')
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name='Изображение товара')
    image2 = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name='Изображение товара 2')
    characteristic = models.TextField(blank=True, verbose_name='Состав')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    stock = models.PositiveIntegerField(verbose_name='На складе')
    available = models.BooleanField(default=True, verbose_name='Доступен')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]

    def __str__(self):
        return self.name


class SoonProduct(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(blank=True, verbose_name='Изображение товара')
    text = models.TextField(blank=True, verbose_name='Описание')

    class Meta:
        ordering = ['name']
        verbose_name = 'Soon product'
        verbose_name_plural = 'Soon products'

    def __str__(self):
        return self.name
