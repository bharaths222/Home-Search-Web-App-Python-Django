from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Response
from django.core.mail import send_mail
# Create your views here.
def response(request):
    if request.method == "POST":
        post_id = request.POST['post_id']
        post = request.POST['post']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        # realtor_email = request.POST['realtor_email']
        
        # Check if user has made inquiry of this post already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Response.objects.all().filter(post_id=post_id,user_id=user_id)
            city_slug = self.kwargs.get('city_slug')
            neighborhood_slug = self.kwargs.get('neighborhood_slug')
            title_slug = self.kwargs.get('title_slug')
            pk = self.kwargs.get('pk')
            if has_contacted:
                messages.error(request,'You have already made an inquiry for this post')
                # return redirect('/posts/'+listing_id)
                return redirect('post-detail', city_slug=city_slug, neighborhood_slug=neighborhood_slug, pk=pk, title_slug=title_slug)

        contact = Response(post=post, post_id=post_id,name=name,email=email,phone=phone,message=message,user_id=user_id)

        contact.save()


        messages.success(request, 'Your inquiry has been received, seller will get back to you shortly')
        # return redirect('/listings/'+listing_id)
        return redirect('post-detail', city_slug=city_slug, neighborhood_slug=neighborhood_slug, pk=pk, title_slug=title_slug)
