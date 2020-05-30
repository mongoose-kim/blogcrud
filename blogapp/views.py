from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from .forms import NewBlog

def welcome(request):
    return render(request, 'viewcrud/index.html')

def main(request):
    mytext = Blog.objects.all()
    return render(request, 'home.html', {'myblog' : mytext})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog':blog_detail})

def read(request):
    blogs = Blog.objects.all()
    return render(request, 'viewcrud/funccrud.html', {'blogs':blogs})

def create(request):
    return render(request, 'viewcrud/new.html')

#새로운 데이터 저장=POST
#글쓰기 페이지 띄워줌=GET
def create(request):
    if request.method == 'POST':
        form = NewBlog(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
        return redirect('home')
    else:
        form = NewBlog()
        return render(request, 'viewcrud/new.html', {'form':form})

def update(request, pk):
    blog = get_object_or_404(Blog, pk = pk)

    form = NewBlog(request.POST, instance=blog)
    if form.is_valid:
        form.save()
        return redirect('home')
    
    return render(request, 'viewcrud/new.html', {'form':form})

def delete(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    blog.delete()
    return redirect

    
