from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.http import HttpResponse
# Create your views here.


def home(request):
    restaurants = Restaurant.objects.all()
    return render(request, "home.html", {"restaurants":restaurants})

def get_res(request,pk):
    restaurant = Restaurant.objects.filter(id = pk).first()
    return render(request, "get_restaurant.html", {"restaurant":restaurant})


def add_res(request):
    form = RestaurantForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = RestaurantForm()
    return render(request, "add_res.html", {"form":form})

def upd_res(request, pk):
    restaurant = Restaurant.objects.filter(id = pk).first()
    if restaurant:
        form = RestaurantForm(request.POST, request.FILES, instance=restaurant)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect("home")
        else:
            form = RestaurantForm(instance=restaurant)
        return render(request, "upd_res.html", {"form":form})
    else:
        return HttpResponse("not found")
    
def del_res(request, pk):
    restaurant = Restaurant.objects.filter(id = pk).first()
    if restaurant:
        if request.method == "POST":
                restaurant.delete()
                return redirect("home")
        return render(request, "del_res.html", {"restaurant":restaurant})
    else:
        return HttpResponse("not found")
    
def reviews(request, pk):
    reviews = Review.objects.filter(id = pk).all()
    return render(request, "reviews.html", {"reviews":reviews})

def get_review(request, pk):
    review = Review.objects.filter(id = pk).first()
    return render(request, "get_review.html", {"review":review})

def add_review(request):
    form = ReviewForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ReviewForm()
    return render(request, "add_review.html", {"form":form})