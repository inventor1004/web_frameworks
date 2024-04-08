from django.shortcuts import render
from .models import Post
from django.http import JsonResponse
from django.core import serializers
from .forms import PostForm
from profiles.models import Profile

# Create your views here.

def post_list_and_create(request):
  form = PostForm(request.POST or None)
  context = {'form': form}

  if request.method == 'POST':
    if form.is_valid():
      author = Profile.objects.get(user=request.user)
      instance = form.save(commit=False)
      instance.author = author
      instance.save()
      return JsonResponse({
          'title': instance.title,
          'body': instance.body,
          'author': instance.author.user.username,
          'id': instance.id,
      })

      form = PostForm()
      context['form'] = form

  return render(request, 'posts/main.html', context)


def load_post_data_view(request, num_posts):
  if request.method == 'POST' or request.method == 'GET':
    visible = 3 
    upper = num_posts
    lower = upper - visible
    size = Post.objects.all().count()

    qs = Post.objects.all()
    data = []
    for obj in qs:
      item = {
        'id': obj.id,
        'title': obj.title,
        'body': obj.body,
        'liked': True if request.user in obj.liked.all() else False,
        'count': obj.like_count,
        'author': obj.author.user.username
      }
      data.append(item)
    return JsonResponse({'data':data[lower:upper], 'size': size})
    

def like_unlike_post(request):
  if request.method == 'POST':
    pk = request.POST.get('pk')
    obj = Post.objects.get(pk=pk)
    if request.user in obj.liked.all():
        liked = False
        obj.liked.remove(request.user)
    else:
        liked = True
        obj.liked.add(request.user)
    return JsonResponse({'liked': liked, 'count': obj.like_count, 'id': pk})
    

def hello_world_view(requst):
  return JsonResponse({'text': 'hello world'})