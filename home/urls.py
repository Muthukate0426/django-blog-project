from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.home,
        name='home'
    ),


    path(
        'about/',
        views.about,
        name='about'
    ),


    path(
        'contact/',
        views.contact,
        name='contact'
    ),


    path(
        'register/',
        views.register,
        name='register'
    ),


    path(
        'login/',
        views.user_login,
        name='login'
    ),


    path(
        'logout/',
        views.user_logout,
        name='logout'
    ),


    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),


    path(
        'profile/',
        views.profile,
        name='profile'
    ),


    path(
        'change-password/',
        views.change_password,
        name='change_password'
    ),



    # Create Blog Post

    path(
        'create-post/',
        views.create_post,
        name='create_post'
    ),



    # All Blogs + Search

    path(
        'blog/',
        views.blog_list,
        name='blog_list'
    ),



    # Blog Detail

    path(
        'blog/<int:id>/',
        views.blog_detail,
        name='blog_detail'
    ),



    # Edit Post

    path(
        'edit-post/<int:id>/',
        views.edit_post,
        name='edit_post'
    ),



    # Delete Post

    path(
        'delete-post/<int:id>/',
        views.delete_post,
        name='delete_post'
    ),

] 