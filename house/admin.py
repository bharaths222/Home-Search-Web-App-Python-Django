from django.contrib import admin
from .models import Post, Rental, Category, City, Neighborhood, Images, Contact


# You can customize the columns that you want to display in the Listings admin page in this class

class PostImageInline(admin.TabularInline):
    model = Images
    extra = 3

# class RentalImageInline(admin.TabularInline):
#     model = Images
#     extra = 3


class PostAdmin(admin.ModelAdmin):
    inlines = [ PostImageInline, ]
    list_display = ('__str__','id','active','city','neighborhood', 'date_posted','seller')
    list_display_links = ('id', 'seller')
    list_filter = ('seller','city','neighborhood','active','admin_approved','featured') # Filter the listings by seller
    list_editable = ('active',)
    search_fields = ('address','city','zipcode')
    # prepopulated_fields = {'slug': ('title',)}
    list_per_page = 25
    class Meta:
        model = Post

class RentalAdmin(admin.ModelAdmin):
    # inlines = [ RentalImageInline, ]
    list_display = ('__str__','id','active','city','neighborhood', 'date_posted','seller')
    list_display_links = ('id', 'seller')
    list_filter = ('seller','city','neighborhood','active','admin_approved','featured') # Filter the listings by seller
    list_editable = ('active',)
    search_fields = ('address','city','zipcode')
    list_per_page = 25
    class Meta:
        model = Rental

class CityAdmin(admin.ModelAdmin):
    list_display = ["__str__",]
    class Meta:
        model = City


class NeighborhoodAdmin(admin.ModelAdmin):
    list_display = ["__str__","city",]
    class Meta:
        model = Neighborhood


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Rental, RentalAdmin)
admin.site.register(City, CityAdmin )
admin.site.register(Neighborhood, NeighborhoodAdmin)
# admin.site.register(MyPost)
admin.site.register(Category)
admin.site.register(Images)
admin.site.register(Contact)


