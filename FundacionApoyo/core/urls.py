from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('donacion/', views.donacion, name="donacion"),
    path('formulario/', views.formulario, name="formulario"),
    path('blog/', views.blog, name="blog"),
    path('visit_us/', views.visit_us, name="visit_us"),
    path('nueva_ficha/', views.nueva_ficha, name="nueva_ficha"),
    path('eliminar/<int:persona_id>/', views.eliminar, name="eliminar"),
    path('editar/<int:persona_id>/', views.editar, name="editar"),
    
]