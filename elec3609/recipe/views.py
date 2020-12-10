# Import Packages
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.core.mail import send_mail, BadHeaderError
from django.db.models.query_utils import Q
from rest_framework import viewsets,permissions, generics
from recipe.forms import UserForm, UserProfileForm, PostForm
from recipe.models import Profile, Post
from recipe.serializers import ProfileSerializer, UserSerializer, PostSerializer
from django.views.generic import ListView

## Category Pages
def AussieBBQ(request):
    allposts = Post.objects.filter(category='AussieBBQ')
    return render(request, 'recipies/AussieBBQ.html',{'allposts': allposts})

def BakedSweets(request):
    allposts = Post.objects.filter(category='BakedSweets')
    return render(request, 'recipies/BakedSweets.html',{'allposts': allposts})

def Bread(request):
    allposts = Post.objects.filter(category='Bread')
    return render(request, 'recipies/Bread.html',{'allposts': allposts})

def Breakfast(request):
    allposts = Post.objects.filter(category='Breakfast')
    return render(request, 'recipies/Breakfast.html',{'allposts': allposts})

def Burgers(request):
    allposts = Post.objects.filter(category='Burgers')
    return render(request, 'recipies/Burgers.html',{'allposts': allposts})

def Chinese(request):
    allposts = Post.objects.filter(category='Chinese')
    return render(request, 'recipies/Chinese.html',{'allposts': allposts})

def Dessert(request):
    allposts = Post.objects.filter(category='Dessert')
    return render(request, 'recipies/Dessert.html',{'allposts': allposts})

def Drinks(request):
    allposts = Post.objects.filter(category='Drinks')
    return render(request, 'recipies/Drinks.html',{'allposts': allposts})

def FriedFood(request):
    allposts = Post.objects.filter(category='Fried Food')
    return render(request, 'recipies/FriedFood.html',{'allposts': allposts})

def Greek(request):
    allposts = Post.objects.filter(category='Greek')
    return render(request, 'recipies/Greek.html',{'allposts': allposts})

def Indian(request):
    allposts = Post.objects.filter(category='Indian')
    return render(request, 'recipies/Indian.html',{'allposts': allposts})

def Japanese(request):
    allposts = Post.objects.filter(category='Japanese')
    return render(request, 'recipies/Japanese.html',{'allposts': allposts})

def Lebanese(request):
    allposts = Post.objects.filter(category='Lebanese')
    return render(request, 'recipies/Lebanese.html',{'allposts': allposts})

def Mexican(request):
    allposts = Post.objects.filter(category='Mexican')
    return render(request, 'recipies/Mexican.html',{'allposts': allposts})

def Pasta(request):
    allposts = Post.objects.filter(category='Pasta')
    return render(request, 'recipies/Pasta.html',{'allposts': allposts})

def Pastries(request):
    allposts = Post.objects.filter(category='Pastries')
    return render(request, 'recipies/Pastries.html',{'allposts': allposts})

def Pies(request):
    allposts = Post.objects.filter(category='Pies')
    return render(request, 'recipies/Pies.html',{'allposts': allposts})

def Pizza(request):
    allposts = Post.objects.filter(category='Pizza')
    return render(request, 'recipies/Pizza.html',{'allposts': allposts})

def Rice(request):
    allposts = Post.objects.filter(category='Rice')
    return render(request, 'recipies/Rice.html',{'allposts': allposts})

def Salad(request):
    allposts = Post.objects.filter(category='Salad')
    return render(request, 'recipies/Salad.html',{'allposts': allposts})

def Sandwich(request):
    allposts = Post.objects.filter(category='Sandwich')
    return render(request, 'recipies/SandWich.html',{'allposts': allposts})

def Seafood(request):
    allposts = Post.objects.filter(category='Seafood')
    return render(request, 'recipies/Seafood.html',{'allposts': allposts})

def Snacks(request):
    allposts = Post.objects.filter(category='Snacks')
    return render(request, 'recipies/Snacks.html',{'allposts': allposts})

def Soup(request):
    allposts = Post.objects.filter(category='Soup')
    return render(request, 'recipies/Soup.html',{'allposts': allposts})

def Steak(request):
    allposts = Post.objects.filter(category='Steak')
    return render(request, 'recipies/Steak.html',{'allposts': allposts})

def Thai(request):
    allposts = Post.objects.filter(category='Thai')
    return render(request, 'recipies/Thai.html',{'allposts': allposts})

def Vegetarian(request):
    allposts = Post.objects.filter(category='Vegetarian')
    return render(request, 'recipies/Vegetarian.html',{'allposts': allposts})

## Page /random
def random(request):
    return render(request, 'home/random.html',{})

## Page /
def index(request):
    return render(request, 'home/index.html',{})

## Page /category
def category(request):
    return render(request, 'categories/category.html',{})

## Page /searchview
class searchviewView(TemplateView):
    template_name = 'categories/searchview.html'

#Gets user input and displays appropriate results using 3 attributes
def searchedresultView(request):
    model = Post
    template_name = 'categories/searchedresult.html'

    query = request.GET.get('q')
    object_list = Post.objects.filter(
        # search through all the Posts using the below 3 attributes
        Q(title__icontains=query) | Q(content__icontains=query) | Q(category__icontains=query)
    )

    return render(request, 'categories/searchedresult.html', {'object_list': object_list})


## Page /login
def login(request):
    if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            print(form.errors)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is None:
                    messages.error(request, "Invalid username or password.")
                else:
                    auth_login(request, user)
                    return render(request, 'home/index.html',{})
            else:
                messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                        template_name = "user/login.html",
                        context={"form":form})

## Page /logout
def logout(request):
    auth_logout(request)
    return render(request, 'home/index.html',{})

## Page /signup
def signup(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid() and user_form.cleaned_data['password1'] == user_form.cleaned_data['password2']:
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password1')
            email = user_form.cleaned_data.get('email')

            User.objects.create_user(username=username, password=password, email=email)
            user = User.objects.get(username=username)
            user.set_password(password)
            user.save()
            profile = Profile.objects.create(user=user)

            auth_login(request, user)
            return render(request, 'home/index.html',{})
    else:
        user_form = UserForm()
    return render(request, 'user/signup.html', {'user_form': user_form})

## Favouriting function
def favorite(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you need to be signed in to do that!')
        return redirect('signup')
    if request.method == 'POST':
        fav = Post.objects.get(pk=pk)
        profile = Profile.objects.get(user=request.user)
        if fav in profile.favorites.all():
            messages.error(request, 'That post is already in your favorites')
        else:
            profile.favorites.add(fav)
            messages.success(request, 'Post added to Favorites!')
    return redirect('favoritepage')

## Remove from favourites function
def deletefavorite(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you need to be signed in to do that!')
        return redirect('signup')
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        profile = Profile.objects.get(user=request.user)
        if post not in profile.favorites.all():
            messages.error(request, 'That post is not in your favorites')
            return redirect('index')
        else:
            profile.favorites.remove(post)
            messages.success(request, 'Post removed from Favorites!')
    return redirect('favoritepage')

## Page /favourite
def favoritepage(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you need to be signed in to do that!')
        return redirect('signup')
    profile = Profile.objects.get(user=request.user)
    favposts = profile.favorites.all()
    return render(request, 'account/favoritepage.html',{'favposts': favposts})

## Page /postrecipes
def postrecipes(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you need to be signed in to do that!')
        return redirect('signup')
    if request.method == 'POST':
        post_form = PostForm(data=request.POST, files=request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
           # post_img = PostForm(instance=request.post)
           # post.published_date = timezone.now()
            post.save()
            return redirect('detail', pk=post.pk)
    else:
        post_form = PostForm()
    return render(request, 'account/postrecipes.html',{'form': post_form})


## Page /myrecipes
def myrecipes(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you need to be signed in to do that!')
        return redirect('signup')
    if request.method == 'GET':
        allposts = Post.objects.filter(user=request.user)
        return render(request, 'account/myrecipes.html',{'allposts': allposts})


## Page /recipedetailed
def recipedetailed(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'account/recipedetailed.html', {'post': post})

## Delete user
def delete_user(request, username):
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you need to be signed in to do that!')
        return redirect('signup')
    post = get_object_or_404(User, username=username)
    if request.method == "POST":
       request.user.delete()
    print("click")
    messages.success(request,"Account Deleted!")
    return redirect('index')

## Page /profile
def profile(request):
    print("triggered")
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you need to be signed in to do that!')
        return redirect('signup')
    if request.method == 'POST':
        profile_form = UserProfileForm(instance=request.user.profile,data=request.POST,files=request.FILES)
        if profile_form.is_valid():
            profile_form.save()
          #  profile_form = UserProfileForm(instance=request.user.profile)
            return render(request, 'account/profile.html',{'profile_form': profile_form})
        else:
            messages.error(request,'Error updating your profile')
    else:
        profile_form = UserProfileForm(instance=request.user.profile)
    return render(request, 'account/profile.html',{'profile_form': profile_form})

## Page /password_reset
def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                subject = "Password Reset for Second Breakfast"
                from_email = 'noreply@secondbreakfast.com'
                email_template_name = "user/password_resent_email.txt"
                for user in associated_users:
                    c = {
                        "username":user.username,
                        "email":user.email,
                        'domain':'127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, from_email , [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                return render(request, 'user/password_reset_done.html',{'user': associated_users[0]})
            if not User.objects.filter(email=data, is_active=True).exists():
                password_reset_form = PasswordResetForm()
                messages.error(request,'There is no user registered with the specified E-Mail address.')
    else:
       password_reset_form = PasswordResetForm()

    return render(request=request, template_name="user/password_reset.html", context={"password_reset_form":password_reset_form})

## To delete a post
def deletepost(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you need to be signed in to do that!')
        return redirect('signup')
    post = get_object_or_404(Post, id=pk)
    if request.method == "POST":
        if request.user != post.user:
            messages.error(request,'Sorry, you cannot delete this post')
            return redirect('index')
        else:
            post.delete()
            messages.success(request,'Post successfully deleted')
    return redirect('myrecipes')


## To edit a post
def editpost(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you need to be signed in to do that!')
        return redirect('signup')
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'account/postrecipes.html', {'form': post_form})


## RESTful API: Profile
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# RESTful API: User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

## RESTful API: Post
## With help from https://medium.com/analytics-vidhya/how-to-create-rest-api-using-django-rest-framework-a-blog-app-15a175884979
class PostListSet(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


