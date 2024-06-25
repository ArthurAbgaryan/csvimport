# Generated by Django 3.2.24 on 2024-06-23 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='accessory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accessory_group_id', models.PositiveIntegerField(null=True, verbose_name='Идентификатор группы аксессуаров')),
                ('title', models.CharField(max_length=250, null=True, verbose_name='Название')),
                ('quantity', models.IntegerField(null=True, verbose_name='Количество в базовом комплекте')),
                ('price', models.PositiveIntegerField(null=True, verbose_name='Розничная цена')),
                ('price_dealer', models.PositiveIntegerField(null=True, verbose_name='Дилерская цена')),
                ('discount', models.PositiveIntegerField(null=True, verbose_name='Рознична скидка')),
                ('discount_dealer', models.PositiveIntegerField(null=True, verbose_name='Дилерская скидка')),
                ('label', models.CharField(max_length=250, null=True, verbose_name='Лейбл (статус)')),
                ('vendor_code', models.CharField(max_length=250, null=True, verbose_name='Артикул')),
                ('position', models.PositiveIntegerField(null=True, verbose_name='Позиция внутри группы аксессуаров')),
            ],
            options={
                'verbose_name': 'Комплектующие',
                'verbose_name_plural': 'Комплектующие',
            },
        ),
        migrations.CreateModel(
            name='accessory_group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Группа комплектующих',
                'verbose_name_plural': 'Группы комплектующих',
            },
        ),
        migrations.CreateModel(
            name='attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('position', models.PositiveIntegerField(null=True, verbose_name='Позиция в карточке товара')),
            ],
            options={
                'verbose_name': 'Атрибут',
                'verbose_name_plural': 'Атрибуты',
            },
        ),
        migrations.CreateModel(
            name='attribute_value',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_attribute_id', models.PositiveIntegerField(null=True, verbose_name='Идентификатор атрибута')),
                ('title', models.CharField(max_length=250, null=True, verbose_name='Название')),
                ('generation_title', models.CharField(help_text='Название для генерации названия опции (если не задано, берётся из title)', max_length=250, null=True)),
                ('is_generation_hidden', models.BooleanField()),
                ('description', models.CharField(max_length=250, null=True, verbose_name='Описание (подсказка)')),
                ('position', models.PositiveIntegerField(null=True, verbose_name='Позиция в карточке товара')),
            ],
            options={
                'verbose_name': 'Значение атрибута',
                'verbose_name_plural': 'Значение атрибутов',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=150, null=True)),
                ('date_published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookImport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv_file', models.FileField(upload_to='uploads/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, verbose_name='Название')),
                ('parent_id', models.PositiveIntegerField(help_text='Идентификатор родительской категории', null=True)),
                ('lft', models.PositiveIntegerField(help_text='Параметр lft (хранение деревьев nested set). Может быть использовано для простой сортировки.', null=True)),
                ('rgt', models.PositiveIntegerField(help_text='Параметр rgt (хранение деревьев nested set)', null=True)),
            ],
            options={
                'verbose_name': 'Каталог',
                'verbose_name_plural': 'Каталоги',
            },
        ),
        migrations.CreateModel(
            name='CatalogImport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('json_file', models.FileField(upload_to='uploads/')),
                ('date_published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_group_id', models.PositiveIntegerField(null=True, verbose_name='Идентификатор группы цветов')),
                ('title', models.CharField(blank=True, max_length=250, verbose_name='Название')),
                ('picture', models.URLField(help_text='url изображения', null=True, verbose_name='картинка')),
                ('position', models.PositiveIntegerField(help_text='Позиция сортировки', null=True, verbose_name='Позиция')),
            ],
        ),
        migrations.CreateModel(
            name='color_group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='Название', max_length=250)),
                ('position', models.IntegerField(help_text='Позиция сортировки', null=True)),
            ],
            options={
                'verbose_name': 'Группа цветов',
                'verbose_name_plural': 'Группы цветов',
            },
        ),
        migrations.CreateModel(
            name='glass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, verbose_name='Стекло')),
            ],
            options={
                'verbose_name': 'Стекло',
                'verbose_name_plural': 'Стёкла',
            },
        ),
        migrations.CreateModel(
            name='product_test_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, null=True)),
                ('is_accessory', models.BooleanField(help_text='Используется во вкладке Фурнитура у входных дверей', null=True)),
                ('position', models.PositiveIntegerField(null=True, verbose_name='Позиция')),
            ],
            options={
                'verbose_name': 'Характеристика',
                'verbose_name_plural': 'Характеристики',
            },
        ),
        migrations.CreateModel(
            name='property_value',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_id', models.PositiveIntegerField(null=True, verbose_name='Идентификатор характеристики')),
                ('product_id', models.PositiveIntegerField(null=True, verbose_name='Идентификатор товара')),
                ('title', models.CharField(max_length=250, null=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Значение характеристик',
                'verbose_name_plural': 'Значение характеристик',
            },
        ),
        migrations.CreateModel(
            name='trademark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, null=True, verbose_name='Название')),
                ('picture', models.URLField(null=True, verbose_name='url изображения')),
            ],
            options={
                'verbose_name': 'Торговая марка',
                'verbose_name_plural': 'Торговые марки',
            },
        ),
    ]
