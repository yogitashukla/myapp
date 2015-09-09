#from django.shortcuts import render
#from django.shortcuts import render_to_response
#from .models import Blog
#from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


#def blog(request):
 #   blogs = Blog.objects.all()  #  return render_to_response('mytemplate.html', {'blogs': blogs})
from django.shortcuts import render_to_response
from blog.forms import PostModelForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse
from blog import models as m
from django.template import loader,RequestContext,Context
from actstream.models import model_stream


from django.db.models.signals import post_save
from actstream import action
from blog.models import Blog


def my_handler(sender, instance, created, **kwargs):
    action.send(instance, verb='was saved')

post_save.connect(my_handler, sender=Blog)



def post_form_upload(request):
    if request.method == 'GET':
        form = PostModelForm()
    else:
        # A POST request: Handle Form Upload
        form = PostModelForm(request.POST) # Bind data from request.POST into a PostForm

        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            author = form.cleaned_data['author']
            pub_date = form.cleaned_data['pub_date']
            post = m.Blog.objects.create(title=title,pub_date=pub_date,text=text,author=author)
            action.send(request.user, verb='activity created')
            post_save.connect(my_handler, sender=Blog)
            return HttpResponseRedirect('/up(post)')

    return render(request, 'form_upload.html', {
        'form': form,
    })


def up(request):
    post = m.Blog.objects.all().order_by('pub_date').reverse()

    return render_to_response('temp.html', {'post': post})


def index(request):
    pe = m.Blog.objects.all()
    t = loader.get_template('index.html')
    c = Context({'pe': pe})
    return HttpResponse(t.render(c))


def delete(request, id):
    p = m.Blog.objects.get(pk=id)
    p.delete()
    action.send(request.user, verb='activity delete')
    post_save.connect(my_handler, sender=Blog)
   # st = model_stream(p[0])
    return HttpResponseRedirect('/up')


def edit(request, id):
    p = m.Blog.objects.get(pk=id)
    if request.method == 'POST':
        p.author = request.POST['author']
        p.title = request.POST['title']
        p.text = request.POST['text']
        p.pub_date = request.POST['pub_date']
        p.save()
        action.send(request.user, verb='activity edited')
        post_save.connect(my_handler, sender=Blog)
    t = loader.get_template('index.html')
    c = RequestContext(request, {'post': p})

   # return redirect ("//")
      #  return HttpResponseRedirect('/up')
    return HttpResponse(t.render(c))


