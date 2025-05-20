from django.shortcuts import render
from django.views.generic import ListView , DetailView
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy
from .models import Post

# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = "blog/list.html"
    

# def detail_view(request,blog_id):
#     blog = Post.objects.get(id=blog_id)
#     context = {
#         "blog":blog,
#     }
#     return render(request,'blog/detail.html',context)

class BlogDetailView(DetailView):
    
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'blog'
    
class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog/new.html'
    fields =['title','body','author']
    
class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/edit.html'
    fields =['title','body']
    
class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('blog_list')
    