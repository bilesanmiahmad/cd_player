from django.shortcuts import render, redirect,render_to_response, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.dates import MonthArchiveView, WeekArchiveView

from blog.models import Post
from blog.forms import PostForm, CommentForm
# Create your views here.


@user_passes_test(lambda u: u.is_superuser)
def addPost(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        request.session['name'] = request.user.username
        return redirect(post)
    return render(request, 'blog/add_post.html', {'form': form})


def viewPost(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm(request.POST or None)
    print("before")
    if form.is_valid():
        comment = form.save(commit=False)
        print("test")
        print(comment)
        comment.post = post
        comment.save()
        print(comment.name)
        print(request.session)
        # request.session['name'] = comment.name
        # request.session['email'] = comment.email
        # request.session['website'] = comment.website
        return redirect(request.path)
    print(request.path)
    form.initial['name'] = request.session['name']
    # form.initial['email'] = request.session['email']
    # form.initial['website'] = request.session['website']
    return render(request, 'blog/blog_post.html', {'form': form, 'post': post})


class PostMonthArchiveView(MonthArchiveView):
    queryset = Post.objects.all()
    date_field = 'created'
    allow_future = True


class PostWeekArchiveView(WeekArchiveView):
    queryset = Post.objects.all()
    date_field = 'created'
    week_format = '%W'
    allow_future = True
