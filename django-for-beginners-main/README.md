# django-for-beginners

Welcome to the Django for beginners! In this tutorial, we will walk through building a simple web application using Django. We'll cover the essential concepts. By following this hands-on approach, you'll gain understanding of Django's core features. Let's get started!

## Step 1: Setting Up the Project

Install Python: Follow the official Python installation guide for your operating system.

**Create a Virtual Environment:**

Open your terminal and run the following commands:

```
python3 -m venv myenv
```

```
source myenv/bin/activate
```

**Install Django:**

Run the command in your virtual environment to install Django.
```
pip install django
```

To check installation
```
python3 -m django --version
```

**Create a Django Project:**

Run 

```
django-admin startproject shop
```
To create a new Django project named ``` shop ```.

Run

```
python3 manage.py runserver 
```

To run the development server

## Step 2: Creating new application inside project

Run

```

python3 manage.py startapp products

```

This command should be executed in the same directory where the ```manage.py``` file is located, which is the root directory of your Django project.

After running this command, Django will generate a new folder named "products" with the initial structure of the app

Once you've created the "products" app, you'll need to include it in your project's settings. Open the ```shop/settings.py``` file and find the ```INSTALLED_APPS``` list and add ```"products.apps.ProductsConfig"``` to the list

```

INSTALLED_APPS = [
    # ...
    "products.apps.ProductsConfig",
    # ...
]

```

## Step 3: Creating Views and Configuring URLs and Routing

Open the file ```views.py``` inside the ```products``` folder and add the code given below

```

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the products index.") 

```

Create a file ```urls.py``` inside products folder and add the code below

```

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

```

Now open ```urls.py``` in shop folder and add code given below

```

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("products/", include("products.urls")),
]

```

Now run the server using command

```
python3 manage.py runserver 
```

Open the url ```http://127.0.0.1:8000/products/``` to see the first django app

## Step 4: Building Models and Database Relationships


**Configure Database Settings:**

Open ``` shop/settings.py ``` and configure the database settings according to your needs (e.g., SQLite, MySQL, PostgreSQL).

**Define Models:**

Open file called ``` models.py ``` in ```products``` directory. 

Define your models using Django's model syntax, including fields and relationships.

```

from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.CharField(max_length=3000)
    
```

**Create Database Tables:**

Run 

```
python3 manage.py makemigrations
```

```
python3 manage.py migrate
```

to create the necessary database tables.

Now install [DB Browser for SQLite](https://sqlitebrowser.org/dl/) and open ```db.sqlite3``` file inside project directory to view it

## Step 5: Django Admin Panel

Before acccessing the django admin page we need to create an admin user for that

Run

```

python manage.py createsuperuser

```

provide username, email and password to complete admin user creation

**Register Models:**

Open ``` products/admin.py ``` and register your models to make them accessible via the Django admin interface.

```

from django.contrib import admin
from .models import Product

# Register your models here.
admin.site.register(Product)

```

To customise view of products in admin panel

```

from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

# Register your models here.
admin.site.register(Product, ProductAdmin)

```

## Step 6: Creating Templates

Create a folder called ```templates``` inside products directory

Inside templates folder create a html file called ```index.html```

```

<h2>Products</h2>
<ul>
    {% for product in products %}
        <li>{{ product.name }}</li>
    {% endfor %}
</ul>

```

Now modify the ```views.py``` file so as to display index.html

```

from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products}) 
    
```

## Step 7: Using Bootstrap

Create a file called ```theme.html``` inside ```products/templates``` directory as given below

```

<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Shop</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
  </head>
  <body>
    {% block content %}

    {% endblock %}

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous"></script>
  </body>
</html>

```

Modify ```index.html``` as given below

```

{% extends 'theme.html' %}

{% block content %}

<h2>Products</h2>

<div class="container">

    {% for product in products %}
             
        <div class="card" style="width: 18rem;">
            <img src="{{product.image}}" class="card-img-top" alt="...">
            <div class="card-body">
            <h5 class="card-title">{{product.name}}</h5>
            <p class="card-text">${{product.price}}</p>
            <a href="#" class="btn btn-primary">Go somewhere</a>
            </div>
        </div>
    
    {% endfor %}  

</div>
    
{% endblock %}
    
```

Your Shop is now complete. You can modify this app as per your creativity and logic

## Conclusion

Congratulations on completing the practical Django tutorial for beginners! You've built a simple web application with database models, views, templates, URL routing. This hands-on approach should have provided you with a foundation in Django development. Keep exploring Django's extensive features and consider building more complex projects to further enhance your skills. 

**Happy coding!**

## Step 8: Further Learning

**Django Documentation:**

The official Django documentation is an excellent resource to explore in-depth explanations, tutorials, and reference materials. Visit the Django documentation website at [https://docs.djangoproject.com/](https://docs.djangoproject.com/) to access the latest documentation.

**Django for Beginners:**

A step-by-step guidebook written by William S. Vincent that covers the basics of Django development. It provides hands-on examples and practical explanations for beginners. You can find it at [https://djangoforbeginners.com/](https://djangoforbeginners.com/).

**Django Girls Tutorial:**

Django Girls offers a beginner-friendly tutorial that walks you through building a simple web application using Django. It provides clear instructions and code examples. Access the tutorial at [https://tutorial.djangogirls.org/](https://tutorial.djangogirls.org/).

**DjangoCon Videos:**

DjangoCon is an annual conference focused on Django and web development. The conference features talks and presentations by industry experts. You can find recorded videos from past DjangoCon events on YouTube and the official DjangoCon website.

**Django Project's YouTube Channel:**

The Django Project maintains a YouTube channel where you can find video tutorials, talks, and interviews related to Django. Visit the channel at [https://www.youtube.com/user/django](https://www.youtube.com/user/django).

**Two Scoops of Django:**

A comprehensive book by Daniel Roy Greenfeld and Audrey Roy Greenfeld that provides best practices, tips, and techniques for Django development. It covers various topics and advanced concepts. Find it at [https://www.twoscoopspress.com/products/two-scoops-of-django-3-x](https://www.twoscoopspress.com/products/two-scoops-of-django-3-x).

**Django Reddit and Forum:**

Engage with the Django community through platforms like the Django subreddit [https://www.reddit.com/r/django/](https://www.reddit.com/r/django/) and the Django forum [https://forum.djangoproject.com/](https://forum.djangoproject.com/). Participate in discussions, ask questions, and learn from other Django developers.

**Django Packages:**

Explore the Django Packages website [https://djangopackages.org/](https://djangopackages.org/) to discover and explore a wide range of Django packages and libraries. It's a valuable resource to find pre-built solutions for common functionalities.

***Remember, practice is key to mastering Django. Work on personal projects, contribute to open-source projects, and experiment with different features and techniques. Stay up-to-date with the latest Django releases and advancements in the Django ecosystem.*** 

### Happy learning!
