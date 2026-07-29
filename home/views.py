from django.shortcuts import render, redirect, get_object_or_404

from .forms import ContactForm, ProfileForm, PostForm
from .models import Contact, Profile, Post

from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import (
    authenticate,
    login,
    logout,
    update_session_auth_hash
)

from django.contrib.auth.decorators import login_required

from django.db.models import Q



def home(request):

    posts = Post.objects.all().order_by('-created_at')

    return render(
        request,
        'home/index.html',
        {
            'posts': posts
        }
    )



def about(request):

    return render(
        request,
        'home/about.html'
    )



def contact(request):

    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Your message has been sent successfully! ✅"
            )

            return redirect('/contact/')

    else:

        form = ContactForm()


    return render(
        request,
        'home/contact.html',
        {
            'form': form
        }
    )



def register(request):

    if request.method == "POST":

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')


        if password != password2:

            messages.error(
                request,
                "Passwords do not match"
            )


        elif User.objects.filter(username=username).exists():

            messages.error(
                request,
                "Username already exists"
            )


        elif User.objects.filter(email=email).exists():

            messages.error(
                request,
                "Email already exists"
            )


        else:

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            user.save()


            Profile.objects.create(
                user=user
            )


            messages.success(
                request,
                "Account created successfully!"
            )


            return redirect('/login/')


    return render(
        request,
        'home/register.html'
    )



def user_login(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(
            request,
            username=username,
            password=password
        )


        if user is not None:

            login(
                request,
                user
            )

            return redirect('/dashboard/')


        else:

            messages.error(
                request,
                "Invalid username or password"
            )


    return render(
        request,
        'home/login.html'
    )



def user_logout(request):

    logout(request)

    return redirect('/')



@login_required
def dashboard(request):

    profile, created = Profile.objects.get_or_create(
        user=request.user
    )


    return render(
        request,
        'home/dashboard.html',
        {
            'profile': profile
        }
    )



@login_required
def profile(request):

    profile, created = Profile.objects.get_or_create(
        user=request.user
    )


    if request.method == "POST":

        request.user.username = request.POST.get(
            "username"
        )

        request.user.email = request.POST.get(
            "email"
        )

        request.user.save()


        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )


        if form.is_valid():

            form.save()


        messages.success(
            request,
            "Profile updated successfully!"
        )


        return redirect('/profile/')


    form = ProfileForm(
        instance=profile
    )


    return render(
        request,
        "home/profile.html",
        {
            "form": form,
            "profile": profile
        }
    )



@login_required
def change_password(request):

    if request.method == "POST":

        current_password = request.POST.get(
            "current_password"
        )

        new_password = request.POST.get(
            "new_password"
        )

        confirm_password = request.POST.get(
            "confirm_password"
        )


        if not request.user.check_password(
            current_password
        ):

            messages.error(
                request,
                "Current password is incorrect."
            )


        elif new_password != confirm_password:

            messages.error(
                request,
                "New passwords do not match."
            )


        else:

            request.user.set_password(
                new_password
            )

            request.user.save()


            update_session_auth_hash(
                request,
                request.user
            )


            messages.success(
                request,
                "Password changed successfully!"
            )


            return redirect('/dashboard/')


    return render(
        request,
        "home/change_password.html"
    )

# Create Blog Post

@login_required
def create_post(request):

    if request.method == "POST":

        form = PostForm(
            request.POST,
            request.FILES
        )


        if form.is_valid():

            post = form.save(
                commit=False
            )

            post.author = request.user

            post.save()


            messages.success(
                request,
                "Post created successfully! ✅"
            )


            return redirect('/blog/')


    else:

        form = PostForm()


    return render(
        request,
        "home/create_post.html",
        {
            "form": form
        }
    )





# Blog List + Search

def blog_list(request):

    query = request.GET.get('q')


    if query:

        posts = Post.objects.filter(

            Q(title__icontains=query) |

            Q(content__icontains=query)

        ).order_by('-created_at')


    else:

        posts = Post.objects.all().order_by(
            '-created_at'
        )


    return render(
        request,
        'home/blog_list.html',
        {
            'posts': posts,
            'query': query
        }
    )





# Blog Detail

def blog_detail(request, id):

    post = get_object_or_404(
        Post,
        id=id
    )


    return render(
        request,
        'home/blog_detail.html',
        {
            'post': post
        }
    )





# Edit Blog Post

@login_required
def edit_post(request, id):

    post = get_object_or_404(
        Post,
        id=id
    )


    if post.author != request.user:

        messages.error(
            request,
            "You cannot edit this post."
        )

        return redirect('/blog/')



    if request.method == "POST":

        form = PostForm(
            request.POST,
            request.FILES,
            instance=post
        )


        if form.is_valid():

            form.save()


            messages.success(
                request,
                "Post updated successfully! ✅"
            )


            return redirect(
                f'/blog/{post.id}/'
            )


    else:

        form = PostForm(
            instance=post
        )


    return render(
        request,
        'home/edit_post.html',
        {
            'form': form,
            'post': post
        }
    )






# Delete Blog Post

@login_required
def delete_post(request, id):

    post = get_object_or_404(
        Post,
        id=id
    )


    if post.author == request.user:

        post.delete()


        messages.success(
            request,
            "Post deleted successfully! 🗑️"
        )


    else:

        messages.error(
            request,
            "You cannot delete this post."
        )


    return redirect('/blog/')