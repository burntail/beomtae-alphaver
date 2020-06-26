from django.contrib import admin
from django.urls import path
import myapp.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.home, name="home"),
    path('about/', myapp.views.about, name="about"),
    path('list/', myapp.views.list, name="list"),
    path('detail/<int:blog_id>', myapp.views.detail, name="detail"),
    path('create', myapp.views.create, name="create"),
    path('create_completed/', myapp.views.create_completed, name="create_completed"),
    path('update/<int:blog_id>', myapp.views.update, name="update"),
    path('update_final/<int:blog_id>', myapp.views.update_final, name="update_final"),
    path('delete/<int:blog_id>', myapp.views.delete, name="delete"),

]
