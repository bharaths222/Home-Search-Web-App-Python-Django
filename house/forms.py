from django import forms
from django.forms import inlineformset_factory
from django.forms.models import modelformset_factory
from .models import Post, Neighborhood, Category, City
from .choices import (house_type_choices, city_choices, neighborhood_choices, new_construction_choices, 
gated_community_choices, ready_to_move_choices, furnished_choices, category_choices, house_type_choices, rental_type_choices)


class PostForm(forms.ModelForm):

    #category field
    category = forms.ModelChoiceField(
        label='',
        required=True,
        widget=forms.Select,
        queryset=Category.objects.all(),
        empty_label= 'Select Category'
    )
    def clean_category(self):
        return self.cleaned_data['category']

    #house_type field
    house_type = forms.ChoiceField(
        label= '',
        required=True,
        widget=forms.Select,
        choices=house_type_choices,
    )
    def clean_house_type(self):
        return self.cleaned_data['house_type']

    #city field
    city = forms.ModelChoiceField(
        label='',
        required=True,
        widget=forms.Select,
        queryset=City.objects.all(),
        empty_label= 'Select City'
    )
    def clean_city(self):
        return self.cleaned_data['city']

    #neighborhood field
    neighborhood = forms.ModelChoiceField(
        label='',
        required=True,
        widget=forms.Select,
        queryset=Neighborhood.objects.all(),
        empty_label= 'Select Neighborhood'
    )
    def clean_neighborhood(self):
        return self.cleaned_data['neighborhood']
    
    #facing field
    facing = forms.ChoiceField(
        label= '',
        required=True,
        widget=forms.Select,
        choices=facing_choices,
    )
    def clean_facing(self):
        return self.cleaned_data['facing']

    class Meta:
        model = Post

        fields = (
            'category',
            'city',
            'neighborhood',
            'address',
            'zipcode',
            'house_type',
            'beds',
            'baths',
            'sqft',
            'price',
            'facing',
            'new_construction',
            'ready_to_move',
            'furnished',
            'gated_community', 
            'gated_community_name', 
            'balcony',
            'parking',
            'security',
            'power_backup',
            'water_supply',
            'club_house',
            'photo_main',  
            'photo_main_2',                            
        )
        labels  = {
            'category':'',
            'city':'',
            'neighborhood':'',
            'address':'',
            'zipcode':'',
            'house_type':'',
            'beds':'',
            'baths':'',
            'sqft':'',
            'price':'',
            'facing':'',
            'new_construction':'New Construction',
            'ready_to_move':'Ready to Move',
            'furnished':'Furnished',
            'gated_community':'Gated Community', 
            'gated_community_name':'',
            'balcony':'Balcony',
            'parking':'Parking',
            'security':'Security',
            'power_backup':'Power Backup',
            'water_supply':'Water Supply',
            'club_house':'Club House',
            'photo_main':'',
            'photo_main_2': '',
        }
        widgets = {
            # 'category': forms.CheckboxSelectMultiple(),
            'address' : forms.TextInput(attrs= {'placeholder': 'House Address'}),
            'zipcode' : forms.TextInput(attrs= {'placeholder': 'Zipcode'}),
            'sqft' : forms.TextInput(attrs= {'placeholder': 'Sqft'}),
            'price' : forms.TextInput(attrs= {'placeholder': '(₹)Price'}),
            'gated_community_name' : forms.TextInput(attrs= {'placeholder': 'Gated Community Name'}),
            # 'new_construction' : forms.CheckboxInput(attrs= {'style': 'color:black'}),
            # 'city': forms.Select(attrs={'style': 'color:red'}),
            # 'item' : forms.TextInput(attrs= {'placeholder': 'Item', 'style': 'width:25em'}),
            # 'quantity' : forms.TextInput(attrs= {'placeholder': 'Quantity', 'style': 'width:15em'}),
            # 'price' : forms.TextInput(attrs= {'placeholder': '$Price', 'style': 'width:15em'}),
            # 'minimum delivery fee' : forms.TextInput(attrs= {'placeholder': '$Fee', 'style': 'width:15em'}),
            # 'description' : forms.Textarea(attrs= {'placeholder': 'Item Description',
            #                                         'rows': 3,
            #                                         'cols': 40,
            #                                         'style': 'height: 7em; width:25em'}),
            # 'dietary': forms.Select(attrs={'style': 'width:15em'}),
            # 'date_available' : forms.DateInput(attrs= {'type': 'date',
            #                                            'style': 'width:15em'}),
            # 'beds': forms.Select(attrs={'style': 'width:10em'}),
            # 'category': forms.Select(attrs={'style': 'width:13em'}),
            # 'pickup_delivery_info' : forms.Textarea(attrs= {
            #                                         'placeholder': 'Pickup or Delivery Information',
            #                                         'rows': 3,
            #                                         'cols': 40,
            #                                         'style': 'height: 7em; width:25em'
            #                                         }),
        }
    
  
