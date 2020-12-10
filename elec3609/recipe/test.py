from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from django.core.exceptions import ValidationError
from recipe.forms import UserForm, UserProfileForm
from recipe.models import Profile, Post
from datetime import date
from django.core.files.uploadedfile import SimpleUploadedFile

class PageAccessTest_Guest_User(TestCase):
    """
    Test accessibility for all pages (Guest User)
    """
    def test_home(self):
        """
        index (landing page)
        """
        # /index
        url_index = reverse('index')
        response_index = self.client.get(url_index)
        self.assertEqual(response_index.status_code, 200)

    def test_random_recipe(self):
        """
        random recipe page
        """
        # /random
        url_random = reverse('random')
        response_random = self.client.get(url_random)
        self.assertEqual(response_random.status_code, 200)

    def test_user(self):
        """
        User account related pages
        """
        # /login
        url_login = reverse('login')
        response_login = self.client.get(url_login)
        self.assertEqual(response_login.status_code, 200)
        # /password_reset
        url_password_reset = reverse('password_reset')
        response_password_reset = self.client.get(url_password_reset)
        self.assertEqual(response_password_reset.status_code, 200)
        # /signup
        url_signup = reverse('signup')
        response_signup = self.client.get(url_signup)
        self.assertEqual(response_signup.status_code, 200)

    def test_category(self):
        """
        All categories and search views
        """
        # /category
        url_category = reverse('category')
        response_category = self.client.get(url_category)
        self.assertEqual(response_category.status_code, 200)
        # / searchview
        url_searchview = reverse('searchview')
        response_searchview= self.client.get(url_searchview)
        self.assertEqual(response_searchview.status_code, 200)

    def test_all_recipes(self):
        """
        All Recipes for each cetagory
        """
        # /AussieBBQ
        self.assertEqual(self.client.get(reverse('AussieBBQ')).status_code, 200)
        # /baketSweets
        self.assertEqual(self.client.get(reverse('bakedSweets')).status_code, 200)
        # /Bread
        self.assertEqual(self.client.get(reverse('Bread')).status_code, 200)
        # /Breakfast
        self.assertEqual(self.client.get(reverse('Breakfast')).status_code, 200)
        # /Burgers
        self.assertEqual(self.client.get(reverse('Burgers')).status_code, 200)
        # /Chinese
        self.assertEqual(self.client.get(reverse('Chinese')).status_code, 200)
        # /Dessert
        self.assertEqual(self.client.get(reverse('Dessert')).status_code, 200)
        # /Drinks
        self.assertEqual(self.client.get(reverse('Drinks')).status_code, 200)
        # /FriedFood
        self.assertEqual(self.client.get(reverse('FriedFood')).status_code, 200)
        # /Greek
        self.assertEqual(self.client.get(reverse('Greek')).status_code, 200)
        # /Indian
        self.assertEqual(self.client.get(reverse('Indian')).status_code, 200)
        # /Japanese
        self.assertEqual(self.client.get(reverse('Japanese')).status_code, 200)
        # /Lebanese
        self.assertEqual(self.client.get(reverse('Lebanese')).status_code, 200)
        # /Mexican
        self.assertEqual(self.client.get(reverse('Mexican')).status_code, 200)
        # /Pasta
        self.assertEqual(self.client.get(reverse('Pasta')).status_code, 200)
        # /Pastries
        self.assertEqual(self.client.get(reverse('Pastries')).status_code, 200)
        # /Pies
        self.assertEqual(self.client.get(reverse('Pies')).status_code, 200)
        # /Pizza
        self.assertEqual(self.client.get(reverse('Pizza')).status_code, 200)
        # /Rice
        self.assertEqual(self.client.get(reverse('Rice')).status_code, 200)
        # /Salad
        self.assertEqual(self.client.get(reverse('Salad')).status_code, 200)
        # /SandWhich
        self.assertEqual(self.client.get(reverse('SandWhich')).status_code, 200)
        # /Seafood
        self.assertEqual(self.client.get(reverse('Seafood')).status_code, 200)
        # /Snacks
        self.assertEqual(self.client.get(reverse('Snacks')).status_code, 200)
        # /Soup
        self.assertEqual(self.client.get(reverse('Soup')).status_code, 200)
        # /Steak
        self.assertEqual(self.client.get(reverse('Steak')).status_code, 200)
        # /Thai
        self.assertEqual(self.client.get(reverse('Thai')).status_code, 200)
        # /Vegetarian
        self.assertEqual(self.client.get(reverse('Vegetarian')).status_code, 200)


class PageAccessTest_Account_User(TestCase):
    """
    Test accessibility for all pages (Account User)
    """
    def setUp(self):
        url = reverse('signup')
        data={
            'username':'ChevyChase',
            'email':'ggg@chase.com',
            'password1':'chevyspassword',
            'password2':'chevyspassword'

        }
        response = self.client.post(url, data)
        user_form = UserForm(data=data)

    def test_user(self):
        """
        profile page is only accessible to account user
        """
        # /profile
        url_profile = reverse('profile')
        response_profile = self.client.get(url_profile)
        self.assertEqual(response_profile.status_code, 200)

    def test_post(self):
        """
        functions such as post recipes are only avaliable to account user
        """
         # /favoritepage
        url_favoritepage = reverse('favoritepage')
        response_favoritepage = self.client.get(url_favoritepage)
        self.assertEqual(response_favoritepage.status_code, 200)
         # /myrecipes
        url_myrecipes = reverse('myrecipes')
        response_myrecipes = self.client.get(url_myrecipes)
        self.assertEqual(response_myrecipes.status_code, 200)
         # /postrecipes
        url_postrecipes = reverse('postrecipes')
        response_postrecipes = self.client.get(url_postrecipes)
        self.assertEqual(response_postrecipes.status_code, 200)

class UserModelTest(TestCase):
    """
    Test User Model
    """
    def setUp(self):
        """
        Initialise some global users
        """
        self.user_1 = User.objects.create_user('ChevyChase', 'chevy@chase.com', 'chevyspassword')
        self.user_2 = User.objects.create_user('JimCarrey', 'jim@carrey.com', 'jimspassword')
        self.user_3 = User.objects.create_user('DennisLeary', 'dennis@leary.com', 'denisspassword')

    def test_user_after_creation(self):
        """
        Test if user does exist after signiing up
        """
        user_1 = User.objects.get(username="ChevyChase")
        self.assertEqual(user_1.username, 'ChevyChase')
        user_2 = User.objects.get(username="JimCarrey")
        self.assertEqual(user_2.username, 'JimCarrey')
        user_3 = User.objects.get(username="DennisLeary")
        self.assertEqual(user_3.username, 'DennisLeary')

    def test_duplicate_user(self):
        """
        Test if it shows error when creating duplicated users
        """
        ## Test dupliacted username
        url = reverse('signup')
        data={
            'username':'ChevyChase',
            'email':'ggg@chase.com',
            'password1':'chevyspassword',
            'password2':'chevyspassword'

        }
        response = self.client.post(url, data)
        user_form = UserForm(data=data)
        self.assertFalse(user_form.is_valid())
        self.assertEqual(user_form["username"].errors,
                         [str(User._meta.get_field('username').error_messages['unique'])])
        self.assertFalse(user_form["email"].errors==[str(User._meta.get_field('email').error_messages['unique'])])

    def tearDown(self):
        """
        Remove variable creates during testing
        """
        self.user_1.delete()
        self.user_2.delete()
        self.user_3.delete()


class ProfileModelTest(TestCase):
    """
    Test Profile Model
    """
    def setUp(self):
        """
        Initialise some global users
        """
        url = reverse('signup')
        data={
            'username':'ChevyChase',
            'email':'ggg@chase.com',
            'password1':'chevyspassword',
            'password2':'chevyspassword'

        }
        response = self.client.post(url, data)
        user_form = UserForm(data=data)

    def test_user_profile_model_init(self):
        """
        Test whether User and Profile Model is synced when sign up
        """
        profile_all = Profile.objects.all()
        user_all = User.objects.all()
        profile_1 = Profile.objects.get(user=1)

        self.assertEqual(str(profile_1.user), 'ChevyChase')
        self.assertEqual(str(profile_1.dob), 'None')
        self.assertEqual(user_all.count(), profile_all.count())

    def test_edit_profile_form(self):
        """
        Test editing profile form
        """
        # profile_1 = Profile.objects.get(user=1)
        url = reverse('profile')
        data={
            'firstname':'Chevy',
            'lastname':'Chase',
            'bio':'Hi I am Chevy Chase',
        }
        response = self.client.post(url, data)
        profile_form = UserProfileForm(data=data)
        self.assertTrue(profile_form.is_valid())
        self.assertEqual(profile_form['firstname'].value(),'Chevy')
        self.assertEqual(profile_form['lastname'].value(),'Chase')
        self.assertEqual(profile_form['bio'].value(),'Hi I am Chevy Chase')

class PostModelTest(TestCase):

    """
    Test Post model and functions
    """
    def setUp(self):
        self.user_1 = User.objects.create_user('ChevyChase', 'chevy@chase.com', 'chevyspassword')


    def test_create_post(self):
        """
        Test that a post is created and added to the database with the correct fields
        Post is made directly as a model instance
        """
        time = date.today()
        pic = SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')
        post = Post.objects.create(user=self.user_1, title="test1", content="test content", picture='test_image.jpg', timestamp=time)
        postId = post.id
        self.assertTrue(Post.objects.filter(id=postId).exists())
        self.assertEqual(Post.objects.get(id=postId).user, self.user_1)
        self.assertEqual(Post.objects.get(id=postId).title, "test1")
        self.assertEqual(Post.objects.get(id=postId).content, "test content")
        self.assertEqual(Post.objects.get(id=postId).picture, pic)
        self.assertEqual(Post.objects.get(id=postId).timestamp, time)
    
    def test_post_short_content_under_char_limit(self):
        """
        Test the short_content function, where content is under the 200 char limit and should be returned as it
        """
        test_string = 'a' * 30
        time = date.today()
        pic = SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')
        post = Post.objects.create(user=self.user_1, title="test1", content=test_string, picture='test_image.jpg', timestamp=time)
        self.assertEqual(post.short_content, test_string)

    def test_post_short_content_over_char_limit(self):
        """
        Test the short_content function, where content is over the 200 char limit and should be truncated
        """
        test_string = ('a' * 30) + ('b' * 200) + ('c' * 10)
        time = date.today()
        pic = SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')
        post = Post.objects.create(user=self.user_1, title="test1", content=test_string, picture='test_image.jpg', timestamp=time)
        self.assertEqual(post.short_content, (('a'*30) + ('b'*170)+ '...'))

    def test_post_img(self):
        """
        Test the post_img function
        """
    
class PostFormTest(TestCase):
    
    """
    Test Post creation via the Forms
    """

    def setUp(self):
        self.user_1 = User.objects.create_user('ChevyChase', 'chevy@chase.com', 'chevyspassword')


    def test_create_post_form(self):
        """
        Test a post is created and added to the database with the correct fields
        Post is made via the form 
        """

    def test_create_post_form_invalid_title(self):
        """
        Test a post with an invalid title
        """
    
    def test_create_post_form_invalid_content(self):
        """
        """


    def test_post_mandatory_fields(self):
        """
        Test that the mandatory fields are required
        """


class PostViewTest(TestCase):
    """
    Test the view functions/general functionality regarding creating a post
    """

    def setUp(self):
        self.user_1 = User.objects.create_user('ChevyChase', 'chevy@chase.com', 'chevyspassword')

    def test_create_post_form_detailed(self):
        """
        Test the user is redirected to the correct detailed url page for the post once it is created
        """

    def test_post_logged_out(self):
        """
        Test that only authorised and logged in users can create a post
        """


    """
    Testing edit functionality
    """

    def test_edit_post(self):
        """
        Test that a post's details can be edited, and confirm it is the same post 
        """
    
    def test_edit_redirect(self):
        """
        Test that a post's details can be edited, and confirm it is the same post 
        """

    def test_edit_post_nonexistent(self):
        """
        Test that a post's details can be edited, and confirm it is the same post 
        """

    def test_edit_post_not_user(self):
        """
        Test that a post's details can be edited, and confirm it is the same post 
        """

    def test_edit_post_logged_out(self):
        """
        Test that a post's details can be edited, and confirm it is the same post 
        """

    """
    Testing delete functionality
    """

    def test_delete_post(self):
        """
        Test that a post is deleted
        """
    
    def test_delete_redirect(self):
        """
        Test that a post's details can be edited, and confirm it is the same post 
        """

    def test_delete_post_nonexistent(self):
        """
        Test that a post's details can be edited, and confirm it is the same post 
        """

    def test_delete_post_not_user(self):
        """
        Test that a post's details can be edited, and confirm it is the same post 
        """

    def test_delete_post_logged_out(self):
        """
        Test that a post's details can be edited, and confirm it is the same post 
        """

    """
    Testing fav/unfavoriting functionality
    """
    
    def test_fav_post(self):
        """
        Test that a post's details can be edited, and confirm it is the same post 
        """

    def test_fav_redirect(self):
        """
        Test that a post's details can be edited, and confirm it is the same post 
        """

    def test_fav_post_nonexistent(self):
        """
        Test that a post's details can be edited, and confirm it is the same post 
        """


    def test_fav_post_logged_out(self):
        """
        Test that a post's details can be edited, and confirm it is the same post 
        """

    def test_already_fav(self):
        """
        Test that a post's details can be edited, and confirm it is the same post 
        """

    def test_unfav(self):
        """
        Test that a post's details can be edited, and confirm it is the same post 
        """

    def test_already_unfav(self):
        """
        Test that a post's details can be edited, and confirm it is the same post 
        """

