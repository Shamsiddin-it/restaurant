from .models import *
from django import forms

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ('image', 'name', 'category', 'description', 'address')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('restaurant', 'rating','description')