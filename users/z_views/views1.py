from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Prefetch
from django.forms import modelformset_factory, inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Count, Q
from django.db.models import Max, Min
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
from random import shuffle
from .forms import PostForm
from django.http import JsonResponse
from django.urls import reverse, reverse_lazy
from .models import Post, Category, City, Images, Neighborhood, PostManager, SavedPost, get_upload_path
from django.http import Http404, HttpResponse
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# from rest_framework import viewsets
# from django_filters import rest_framework as filters
from .choices import (category_choices,min_price_choices,max_price_choices,bedroom_choices_2,bathroom_choices,house_type_choices,
new_construction_choices,ready_to_move_choices,furnished_choices,gated_community_choices, neighborhood_choices, city_choices)


# Deactivate Post
def ajax_change_status_deactivate(request):
    pk = request.GET.get('pk')
    post = Post.objects.get(pk=pk)
    try:
        post.active = 0
        post.save()
        return JsonResponse({"success": True})
    except Exception as e:
        return JsonResponse({"success": False})
    return (request, JsonResponse(data))


# Define UserPostListView
class UserPostListView(LoginRequiredMixin, ListView):
    template_name = 'house/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    # paginate_by = 6
    model = Post
    
    def get_queryset(self, *args, **kwargs):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return super().get_queryset(*args, **kwargs).filter(seller = user )

    def get_context_data(self, *args, **kwargs):
        context = super(UserPostListView, self).get_context_data(*args, **kwargs)
        # user = User.objects.filter(username= self.kwargs.get('username'))
        pk = self.request.GET.get('pk')
        context['pk'] = pk
        context['first_name'] = self.request.user.first_name
        context['last_name'] = self.request.user.last_name  
        context['has_posts'] = Post.objects.filter(seller=self.request.user).exists()
        context['active_posts'] = Post.objects.filter(seller=self.request.user, active__contains=1)._by('-date_posted')
        context['inactive_posts'] = Post.objects.filter(seller=self.request.user, active__contains=0).order_by('-date_posted')
        context['posts_count'] = Post.objects.filter(seller=self.request.user).values('id').distinct().count()
        context['active_posts_count'] = Post.objects.filter(seller=self.request.user, active__contains=1).values('id').distinct().count()
        context['inactive_posts_count'] = Post.objects.filter(seller=self.request.user, active__contains=0).values('id').distinct().count()
        return context

    def post(self, request, **kwargs):
        pk = self.request.POST.get('pk')
        post = Post.objects.get(pk=pk)
        username = self.request.user.username
        try:
            post.active = 0
            post.save()
            # return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False})
        # messages.add_message(request, messages.INFO, 'Post Deactivated')
        messages.add_message(request, messages.INFO, 'Post Deactivated')
        return redirect('user-posts', username)
        # return JsonResponse(data)

# Define PostDetailView
class PostDetailView(DetailView):
    template_name = "house/post_detail.html"
    context_object_name = 'object'
    model = Post
    
    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        neighborhood_slug = self.kwargs.get('neighborhood_slug')
        neighborhood = Neighborhood.objects.get(slug=neighborhood_slug)
        city_slug = self.kwargs.get('city_slug')
        city = City.objects.get(slug=city_slug)
        context['featured_apartments_neighborhood'] = featured_apartments_neighborhood
        context['similar_apartments_neighborhood'] = similar_apartments_neighborhood
        context['similar_apartments_city'] = similar_apartments_city
        return context
    
    def post(self, request, **kwargs):
        pk = self.kwargs.get('pk')
        savedhouse = Post.objects.get(pk=pk)
        user = self.request.user
        user_instance = SavedPost.objects.get(user_id = user.id)
        user_instance.post.add(savedhouse)
        # messages.add_message(request, messages.INFO, 'House Saved')
        return redirect('home')

# Define PostCreateView
class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "house/post_create_form.html"

    def post(self, request, **kwargs):
        Post_ImagesFormSet = modelformset_factory(Images, fields=('image',), extra=4, max_num=5)
        form = PostForm(request.POST or None, request.FILES or None)
        formset = Post_ImagesFormSet(request.POST or None, request.FILES or None)

        if form.is_valid() :
            post = form.save(commit = False)
            user = self.request.user
            post.seller = user
            post.save()

            if formset.is_valid():
                for f in formset:
                    try:
                        post_images = Images(post = post,image = f.cleaned_data['image'])
                        post_images.save()
                    except Exception as e:
                        break
            return redirect('user-posts', username=user)


# Define PostUpdateView
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "house/post_update_form.html"
    form_class = PostForm
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostUpdateView, self).get_context_data(**kwargs)
        Post_ImagesFormSet = modelformset_factory(Images, fields=('image',), extra=4, max_num=5)
        qs = Images.objects.filter(post=self.get_object())
        formset = Post_ImagesFormSet(queryset=qs)
        context['formset'] = formset
        return context

    def post(self, request, **kwargs):
        object = self.get_object()
        Post_ImagesFormSet = modelformset_factory(Images, fields=('image',), extra=4, max_num=5)
        form = PostForm(request.POST, request.FILES, instance=object )
        formset = Post_ImagesFormSet(request.POST or None , request.FILES or None)
        
        if form.is_valid() :
            post = form.save(commit = False)
            user = self.request.user
            post.seller = user
            post.save()
            city_slug = self.kwargs.get('city_slug')
            neighborhood_slug = self.kwargs.get('neighborhood_slug')
            title_slug = self.kwargs.get('title_slug')
            pk = self.kwargs.get('pk')
            
            if formset.is_valid():
                for f in formset:
                    try:
                        post_images = Images(post = post,image = f.cleaned_data['image'])
                        post_images.save()
                    except Exception as e:
                        break
            return redirect('post-detail', city_slug=city_slug, neighborhood_slug=neighborhood_slug, pk=pk, title_slug=title_slug)
 
    def get_initial(self):
        initial = super(PostUpdateView, self).get_initial()
        # tags = self.get_object().tag_set.all()
        # initial["tags"] = ", ".join([x.title for x in tags])
        return initial
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.seller:
            return True
        return False


# Define PostDeleteView
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # success_url = reverse_lazy('user-posts')
    template_name = "house/post_confirm_delete.html"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.seller:
            return True
        return False

    def get_success_url(self):
        return reverse('user-posts', kwargs={'username': self.request.user })


# Define PostListView
class PostListView(ListView):
    model = Post
    template_name = 'house/posts_list.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 30
    
    def get_queryset(self, *args, **kwargs):
        category_slug=self.kwargs.get('category_slug')
        city_slug=self.kwargs.get('city_slug')
        neighborhood_slug = self.kwargs.get('neighborhood_slug')
        queryset_list = Post.objects.all().filter(
                category__slug = category_slug,
                city__slug = city_slug,
                neighborhood__slug = neighborhood_slug,
                admin_approved__contains=1, 
                active__contains=1)
        return queryset_list
    
    def get_context_data(self, *args, **kwargs):
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        queryset_list = self.get_queryset()
        featured = list(Post.objects.filter(featured__contains = True))
        random.shuffle(featured)
        category_slug=self.kwargs.get('category_slug')
        category = Category.objects.get(slug=category_slug)
        city_slug=self.kwargs.get('city_slug')
        context['category_choices']= dict(category_choices)
        context['featured']= featured
        context['city_choices']= dict(city_choices)
        context['neighborhood_choices']= dict(neighborhood_choices)
        context['bedroom_choices_2']= dict(bedroom_choices_2)
        context['new_construction_choices']= dict(new_construction_choices)
        context['form'] = PostForm() 
        return context
    
    def post(self, request, **kwargs):
        category_name = request.POST['category_name']
        city_name = request.POST['city_name']
        neighborhood_name = request.POST['neighborhood_name']
        city_slug = city.slug
        neighborhood_slug = neighborhood.slug
        return redirect('house-home', category_slug=category_slug, city_slug=city_slug, neighborhood_slug=neighborhood_slug)
    

# Define HomeView
class HomeView(ListView):
    template_name = "house/home.html"
    model = Neighborhood
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context = { 
                'category_choices': dict(category_choices),
                'city_choices': dict(city_choices),
                'neighborhood_choices': dict(neighborhood_choices)
                }
        return context
        
    def post(self, request, **kwargs):
        category_name = request.POST['category_name']
        city_name = request.POST['city_name']
        neighborhood_name = request.POST['neighborhood_name']
        category = Category.objects.get(title=category_name)
        city = City.objects.get(title=city_name)
        neighborhood = Neighborhood.objects.get(title=neighborhood_name)
        category_slug = category.slug
        city_slug = city.slug
        neighborhood_slug = neighborhood.slug
        return redirect('house-home', category_slug=category_slug, city_slug=city_slug, neighborhood_slug=neighborhood_slug)
    
    
    def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('register')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})


@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            #return redirect('user-posts', username=username)
            return redirect('profile', username=username)
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    if request.user == user:    
        return render(request, "users/profile.html", context)
    else:
        raise PermissionDenied()  

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')





# Define Responses View
def responses(request, username):
user = get_object_or_404(User, username=username)
user_responses = Response.objects.order_by('-contact_date').filter(user_id=request.user.id)
context = {
     'responses':user_responses,
         }
    if request.user == user: 
         return render(request,'house/user_responses.html',context)
    else:
         raise PermissionDenied()      
    
