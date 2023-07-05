# open the file in pycharm
# create req.txt
# download libraries
# pip freeze > req.txt
# 6. django-admin startproject config . (command for creating the project where the config name of the file)
# точка обязательно
# *ip adress того сервера.
# ALLOWED_HOSTS = []
# middle wear тоже стоит какая то защита
# Шаблоны не нужны



#
# 7. django-admin startapp post для создания приложений
# from django.db import models
#
# # Create your models here.
# class Category(models.Model):
#     title = models.CharField(max_length=100)
#
# class Post(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
#     title = models.CharField(max_length=100)
#     body = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#нужно просто скачать в req.txt psycopg2-binary
# 8. python3 manage.py makemigrations - команда которая нужна для считывания данных с модели. Похожа на команда git commit. Изменения commitit
# все миграции хранятся в файле migrations
# 9. python3 manage.py migrate - для отправки таблиц в нашу базу данных
# 10. python3 manage.py runserver для запуска сервера
# 11. python3 manage.py createsuperuser для создания юзера с админ правами


# 12.related_name- для определения имени обратной связи с другой моделью. Он устанавливает имя, по которому можно обращаться к связанным обектам из модели. ОН обычно используется в поле ForeignKey
# 13. related_query_name- это опция используется для определения имени обратной связи, используемого в запросах. Она определяет, как связанные обекты могут быть запрошены с помощью методов filter() exclude()
# python3 manage.py shell - открывает интрерактивный интерпретатор пайтон с помьшью ее модно испю когда нкжно работать с джанго проектом для
# проверкик чего то для тестирования фрагмента кода
 #from post.models import Category----> c = Category.objects.all()----->c------><QuerySet [<Category: book>, <Category: Vida>, <Category: Tree>]>
#from post.models import Post----->from post.models import Post----->p------><QuerySet [<Post: book>None>None>, <Post: book>None>None>, <Post: Vida>None>None>, <Post: Tree>ВЫВФЫФ>фывыфвфывыфв>]>


# p = Post.objects.filter(title='Html').delete()---->(1, {'post.Post': 1})

#from post.models import Category, Post - обратно всве заходит

# c = Category.objects.filter(posts__title='front')


import json

json_data = '{"category":"About Alisha", "title":"About her", "body":"Her hobbies"}'
data = json.loads(json_data)
print(data)
print(type(data))
'__________________________________-'
json_data = json.dumps(data)
print(json_data)
print(type(json_data))



#https://github.com/arzyy/django_test.git

# git init
# git remote add origin #https://github.com/arzyy/django_test.git   
# git pull origin master  
# git add . 
# git init
# git branch