from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, DetailView
from house.models import Post, City, Category, Neighborhood
from django.db.models import Count
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from random import shuffle


class SearchPostListView(ListView):
   
    template_name = "search/search_houses.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchPostListView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        city = City.objects.all().annotate(num_post = Count("post")).order_by("-num_post")
        neighborhood = Neighborhood.objects.all().annotate(num_post = Count("post")).order_by("-num_post")
        featured = list(Post.objects.filter(featured__contains = True))
        shuffle(featured)
        category  = Category.objects.all()
        context['query'] = query 
        context['city'] = city
        context['category'] = category
        context['featured'] = featured
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        
        if query is not None:
            post_list = list(Post.objects.search(query))
            shuffle(post_list)
            paginator = Paginator(post_list, 5)
            page = self.request.GET.get('page')
            
            try:
                post = paginator.page(page)
            except PageNotAnInteger:
                post = paginator.page(1)
            except EmptyPage:
                post = paginator.page(paginator.num_pages)
            return post

            # return Post.objects.search(query)
        return Post.objects.featured()
        '''
        __icontains = field contains this
        __iexact = fields is exactly this
        '''

       

