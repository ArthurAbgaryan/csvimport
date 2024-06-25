from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=150)
    author = models.CharField(max_length = 150,null=True)
    date_published = models.DateTimeField(auto_now_add=True)

class BookImport(models.Model):
    csv_file = models.FileField(upload_to = 'uploads/')
    date_added = models.DateTimeField(auto_now_add=True)

class Catalog(models.Model):
    title = models.CharField(max_length=250,blank=True,verbose_name='Название')
    parent_id = models.PositiveIntegerField(null=True,
                                            help_text='Идентификатор родительской категории')
    lft = models.PositiveIntegerField(null=True,
                                      help_text='Параметр lft (хранение деревьев nested set). Может быть использовано для простой сортировки.')
    rgt = models.PositiveIntegerField(null=True,
                                      help_text='Параметр rgt (хранение деревьев nested set)')
    class Meta:
        def __str__(self):
            return self.title
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'

class CatalogImport(models.Model):
    json_file = models.FileField(upload_to='uploads/')
    date_published = models.DateTimeField(auto_now_add=True)

class color_group(models.Model):
    title = models.CharField(max_length=250,blank=True,help_text='Название')
    position = models.IntegerField(null=True, help_text='Позиция сортировки')

    class Meta:
        def __str__(self):
            return self.title
        verbose_name = 'Группа цветов'
        verbose_name_plural = 'Группы цветов'

class color(models.Model):
    color_group_id = models.PositiveIntegerField(null=True, verbose_name='Идентификатор группы цветов')
    title = models.CharField(max_length=250, blank=True, verbose_name='Название')
    picture = models.URLField(null=True, verbose_name='картинка' ,help_text = 'url изображения')
    position = models.PositiveIntegerField(null=True, help_text='Позиция сортировки', verbose_name='Позиция')

class glass(models.Model):
    title = models.CharField(max_length=250, verbose_name='Стекло', blank=True)
    class Meta:
        verbose_name = 'Стекло'
        verbose_name_plural = 'Стёкла'


class accessory_group(models.Model):
    title = models.CharField(max_length=250, blank=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Группа комплектующих'
        verbose_name_plural = 'Группы комплектующих'

class accessory(models.Model):
    accessory_group_id = models.PositiveIntegerField(null=True,
                                                     verbose_name = 'Идентификатор группы аксессуаров')
    title = models.CharField(max_length=250, null=True, verbose_name='Название')
    quantity = models.IntegerField(null=True, verbose_name='Количество в базовом комплекте')
    price = models.PositiveIntegerField(null = True, verbose_name='Розничная цена')
    price_dealer = models.PositiveIntegerField(null = True, verbose_name='Дилерская цена')
    discount = models.PositiveIntegerField(null=True, verbose_name='Рознична скидка')
    discount_dealer = models.PositiveIntegerField(null=True,verbose_name='Дилерская скидка')
    label = models.CharField(max_length=250, null=True,verbose_name='Лейбл (статус)')
    vendor_code = models.CharField(max_length=250,null=True, verbose_name='Артикул')
    position = models.PositiveIntegerField(null=True, verbose_name='Позиция внутри группы аксессуаров')

    class Meta:
        verbose_name = 'Комплектующие'
        verbose_name_plural = 'Комплектующие'

class property(models.Model):
    title = models.CharField(max_length=250, null=True)
    is_accessory = models.BooleanField(null=True,
                                       help_text='Используется во вкладке Фурнитура у входных дверей')
    position = models.PositiveIntegerField(null=True, verbose_name='Позиция')

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'
class property_value(models.Model):
    property_id = models.PositiveIntegerField(verbose_name='Идентификатор характеристики',null = True)
    product_id = models.PositiveIntegerField(verbose_name='Идентификатор товара',null=True)
    title = models.CharField(max_length=250, null= True, verbose_name='Название')

    class Meta:
        verbose_name='Значение характеристик'
        verbose_name_plural = 'Значение характеристик'

class attribute(models.Model):
    title = models.CharField(max_length=250,verbose_name='Название')
    position = models.PositiveIntegerField(verbose_name='Позиция в карточке товара',null=True)
    class Meta:
        verbose_name = 'Атрибут'
        verbose_name_plural = 'Атрибуты'

class attribute_value(models.Model):
    product_attribute_id = models.PositiveIntegerField(verbose_name='Идентификатор атрибута',null=True)
    title = models.CharField(null=True, verbose_name='Название',max_length=250)
    generation_title = models.CharField(max_length=250,help_text='Название для генерации названия опции (если не задано, берётся из title)',null=True)
    is_generation_hidden = models.BooleanField()
    description = models.CharField(max_length=250,verbose_name='Описание (подсказка)', null=True)
    position =models.PositiveIntegerField(null=True, verbose_name='Позиция в карточке товара')
    class Meta:
        verbose_name = 'Значение атрибута'
        verbose_name_plural = 'Значение атрибутов'

class trademark(models.Model):
    title = models.CharField(max_length=250, null=True,verbose_name='Название')
    picture = models.URLField(null=True, verbose_name='url изображения')
    class Meta:
        verbose_name = 'Торговая марка'
        verbose_name_plural = 'Торговые марки'



# class product_test(models.Model):
#      title = models.CharField(max_length=250,null=True)
#      picture= models.JSONField(null=True)

class product_test_1(models.Model):
    title = models.CharField(max_length=250,blank=True)
    # picture = models.JSONField()