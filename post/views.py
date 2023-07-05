from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# localhost:8000/products
# def get_product(request):
#pass
from post.models import Post


def posts_list(request):
    queryset = Post.objects.all()
    print(queryset)
    # return HttpResponse('<h1>Ok here it comes The hello world! </h1>')
    return render(request, 'listing.html', {'posts': queryset})


#REST

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializers

@api_view(['GET'])        #функция принимает только get response
def posts_list_api_view(request):
    queryset = Post.objects.all()
    serializer = PostSerializers(queryset, many = True)
    return Response(serializer.data)    # we return in response


@api_view(["GET"])
def post_detail(request, id):



    # post = Post.objects.get(id=id)
    # serializer = PostSerializers(post)
    # return Response(serializer.data)
    try:
        post = Post.objects.get(id=id)
        serializer = PostSerializers(post)
        return Response(serializer.data)
    except Post.DoesNotExist:
        return Response('такого обекта нет')
         






#QuerySet - позволяет читать данные из базы данных, фильтровать и изменять их порядок
# objects - это Manager который позволяет работать с бд 
# Они предоставляет нам доступы через методы к django ORM (котрая в свою очередь отправляет запросы в бд)
# Это интерфейс к/й нам позволяет работать с бд через модели

# Model.objects.all()
# Метод all() возвращает QuerySet свех обектов в бд
# SELECT * from table_name;

#filter(**kwargs)
# Возвращает новый QuerySet, содержащий обекты, к/е соответсвуют заданным параметрам поиска
# Post.objects.filter(created_at__year=2022)
# Post.objects.filter(category=1)
# Post.objects.all().filter(category=1) 

# exclude(**kwargs)
# Возвращает QuerySet, содержащий обекты, к/е не соответсвуют заданным параметрам поиска
# Post.objects.exclude(category=1)

# get()
# Возвращает новый QuerySet, содержащий лишь один объект по условию 
# Post.objects.get(id=1)

# order_by
# Post.objects.order_by('price')# идет по возрастанию
# Post.objects.order_by('-price')# идет по убываниюю 


# Post.objects.all()[:5]


