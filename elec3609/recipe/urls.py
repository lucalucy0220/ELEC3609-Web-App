from django.urls import path
from . import views
import recipe.views as recipe_views
from django_rest_passwordreset import views as password_views
from django.conf.urls import url, include
from .views import (postrecipes, myrecipes, recipedetailed)
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
router = DefaultRouter()
router.register(r'profile', views.ProfileViewSet)
router.register(r'user', views.UserViewSet)

urlpatterns = [
    ## Path for each page
    path('', recipe_views.index, name='index'),
    path('random/',recipe_views.random, name='random'),
    path('category/', recipe_views.category, name='category'),
    path('<int:pk>/favorite/', recipe_views.favorite, name='favorite'),
    path('<int:pk>/deletefavorite/', recipe_views.deletefavorite, name='deletefavorite'),
    path('favoritepage/', recipe_views.favoritepage, name='favoritepage'),
    path('myrecipes/',recipe_views.myrecipes, name='myrecipes'),
    path('recipedetailed/',recipe_views.recipedetailed, name='recipedetailed'),
    path('postrecipes/', recipe_views.postrecipes, name='postrecipes'),
    path('profile/', recipe_views.profile, name='profile'),
    path('deleteProfile/<str:username>', recipe_views.delete_user, name='deleteProfile'),
    path('delete/<int:pk>', recipe_views.deletepost, name="delete"),
    path('edit/<int:pk>', recipe_views.editpost, name="edit"),
    path('signup/',recipe_views.signup, name='signup'),
    path('logout/',recipe_views.logout, name='logout'),
    path('login/', recipe_views.login, name='login'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="user/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), name='password_reset_complete'),
    path("password_reset/", recipe_views.password_reset_request, name="password_reset"),
    path('<int:pk>/', recipe_views.recipedetailed, name='detail'),
    path('searchview/', recipe_views.searchviewView.as_view(), name='searchview'), #changes
    path('searchedresult/', recipe_views.searchedresultView, name='searchedresult'),

    ## Specific Category pages
    path('AussieBBQ/',recipe_views.AussieBBQ, name='AussieBBQ'),
    path('BakedSweets/',recipe_views.BakedSweets, name='BakedSweets'),
    path('Bread/',recipe_views.Bread, name='Bread'),
    path('Breakfast/',recipe_views.Breakfast, name='Breakfast'),
    path('Burgers/',recipe_views.Burgers, name='Burgers'),
    path('Chinese/',recipe_views.Chinese, name='Chinese'),
    path('Dessert/',recipe_views.Dessert, name='Dessert'),
    path('Drinks/',recipe_views.Drinks, name='Drinks'),
    path('FriedFood/',recipe_views.FriedFood, name='FriedFood'),
    path('Greek/',recipe_views.Greek, name='Greek'),
    path('Indian/',recipe_views.Indian, name='Indian'),
    path('Japanese/',recipe_views.Japanese, name='Japanese'),
    path('Lebanese/',recipe_views.Lebanese, name='Lebanese'),
    path('Mexican/',recipe_views.Mexican, name='Mexican'),
    path('Pasta/',recipe_views.Pasta, name='Pasta'),
    path('Pastries/',recipe_views.Pastries, name='Pastries'),
    path('Pies/',recipe_views.Pies, name='Pies'),
    path('Pizza/',recipe_views.Pizza, name='Pizza'),
    path('Rice/',recipe_views.Rice, name='Rice'),
    path('Salad/',recipe_views.Salad, name='Salad'),
    path('SandWich/',recipe_views.Sandwich, name='SandWich'),
    path('Seafood/',recipe_views.Seafood, name='Seafood'),
    path('Snacks/',recipe_views.Snacks, name='Snacks'),
    path('Soup/',recipe_views.Soup, name='Soup'),
    path('Steak/',recipe_views.Steak, name='Steak'),
    path('Thai/',recipe_views.Thai, name='Thai'),
    path('Vegetarian/',recipe_views.Vegetarian, name='Vegetarian'),
    url(r'^selectable/', include('selectable.urls')),

    ## RESTful API for Post objects
    url(r'^api/', include(router.urls)),
    path('api/<int:pk>', views.PostDetailSet.as_view()),
    path('api/all', views.PostListSet.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

