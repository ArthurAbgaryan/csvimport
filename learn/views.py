from django.shortcuts import render
from .models import color


def test_color_url(request):
    objects = color.objects.all()
    return render(request,'learn/test_list.html',{'objects':objects})
# Create your views here.
