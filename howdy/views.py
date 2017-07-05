 # howdy/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils import timezone
from .models import Post


# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

# Add this view
class AboutPageView(TemplateView):
    template_name = "about.html"

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'howdy/post_list.html', {'posts': posts})
    