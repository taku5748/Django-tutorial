from xml.etree.ElementTree import Comment
from django.shortcuts import render,redirect

from .forms import CommentForm
from .models import Post

# Create your views here.

def frontpage(request):
    posts = Post.objects.all()
    return render(request, "blog/frontpage.html",{"posts": posts})

def post_detail(request,slug):
    # slug->strType
    post = Post.objects.get(slug=slug)

    form = CommentForm()

    if request.method == "POST":
        print("METHOD IS POST")
        print(request.POST['body'])
        form = CommentForm(request.POST)



    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()

        return redirect("post_detail",slug = post.slug)
    else:
        form = CommentForm()

    return render(request,"blog/post_detail.html",{"post":post,"form":form})
    
