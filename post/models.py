from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, 
                                 related_name='posts', related_query_name='posts')
    title = models.CharField(max_length=100, null=True, blank=True)
    body = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.category:
            return f'{self.category.title}>{self.title}>{self.body}'
        else:
            return self.title


# Charfield - для стороковых значений(обязательно указывать
# max-length
# TextField  - для хранения текста
# DecimalField- для дробных/float чисел(max_digits количество цифр целой части,
# decimal_places - количество цифр дробной части)
# IntegerField- для чисел
# BooleanField- для bool значений
# Datefield- для дат (в питоне datetime.date) auto_now - обновляется каждый раз
# приобновлении записи auto_now_add- заадется при создании обекта
# TimeField - для времени(также может принимать auto_now and auto_now_add)
# DateTimeField - для дат и времени(также может принимать auto_now and auto_now_add)
# DurationField - для периодов времени
# EmailField - for email (имеет встроенную проверку, является ли дуйствительным адресом электронной почты)
# FileField - лдя загрузки файлов (upload_to - для указания директории, где будет хранится лишь путь до файла)
# ImageField - для загрузки фотографий (то же самое, что и FileField, но требуется библиотека Pillow)
# JSONField - для строк в формате JSON

# null - если TRUE, , будет ставить в бд обьект null, если данные не переданы
# blank(больше идет для строковых полей) если True, будет ставить пустую строку если данные не переданы)

# choices - позволяют ограничить варианты записей в это поле


# class MyModel(models.Model):
#     COLOR_CHOICES = (
#         ('R', 'RED'),
#         ('B', 'BLUE'),
#         ('G', 'GREEN')
#     )
#     color = models.CharField(max_length=255, choices=COLOR_CHOICES)


# default - значение по умолчанию для поля, добавляет значения если данные не переданы
# editable - если false то запись нельзя поменять
# unique - если True, будет вызываться ошибка при попытке создать запись которая уже имеется в таблице
# primary_key - если True, т это поле станет первичным ключем в таблице(по дефолту стоит у поля id)
# primary_key - null = False unique = True

from django.core.validators import MaxValueValidator


# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0),
#                                                                             MaxValueValidator(200)])
#     code = models.CharField(max_length=10, validators=[RegexValidator(regex=r'[A-Z]{3}\d{3}$',
#                                                                       message='Code must be in the format AAA-666'
#                                                                       )])


# class Passport(models.Model):
#     info = models.CharField(max_length=255)


# class Person(models.Model):
#     passport = models.OneToOneField(Passport, on_delete=models.CASCADE)

# class Tag(models.Model):
#     title = models.CharField(max_length=255)

# class Post(models.Model):
#     tags = models.ManyToManyField(Tag)

# class Category(models.Model):
#     title = models.CharField(max_length=100)

#     def __str__(self):
#         return self.title


# class Post(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE,
#                                  blank=True, null=True)


    # on_delete = models.CASCADE- каскадное удаление (если удаляется
    # главный обект то удаляется все зависящие от него обекты)
    # on_delete=models.PROTECT - вызывает ошибку припопытки удаления главного обекта
    # on_delete=models.SET_NULL - не удаляет зависящие обекты, а проставляет null
    # if NULL=True
    # models.SET_DEFAULT - ставить default  если был определен default
    # models.DO_NOTHING - вообще ничего не делает(может возникнуть ошибка)
    #
