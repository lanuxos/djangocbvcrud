from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class Test(View):
    def get(self, request):
        return HttpResponse("Django CBV HttpResponse")
    

# create
from django.views.generic.edit import CreateView
from .models import *

class CreatePost(CreateView):
	

	# specify the model for create view
	model = Post

	# specify the fields to be displayed
	fields = ['title', 'detail']
	
	# can specify success url
	# url to redirect after successfully
	# updating details
	success_url ="../all-posts/"


# retrieve / list view
from django.views.generic.list import ListView

class Posts(ListView):

	# specify the model for list view
	model = Post

# retrieve / list view reverse ordering
class AllPosts(ListView):

	# specify the model for list view
	model = Post
	def get_queryset(self, *args, **kwargs):
		qs = super(AllPosts, self).get_queryset(*args, **kwargs)
		qs = qs.order_by("-id")
		return qs


# detail view
from django.views.generic.detail import DetailView

class PostDetail(DetailView):
	# specify the model to use
	model = Post


# update view
# import generic UpdateView
from django.views.generic.edit import UpdateView

class UpdatePost(UpdateView):
	# specify the model you want to use
	model = Post

	# specify the fields
	fields = [
		"title",
		"detail"
	]

	# can specify success url
	# url to redirect after successfully
	# updating details
	success_url ="../all-posts/"

# delete view
# import generic UpdateView
from django.views.generic.edit import DeleteView

class DeletePost(DeleteView):
	# specify the model you want to use
	model = Post
	
	# can specify success url
	# url to redirect after successfully
	# deleting object
	success_url ="../all-posts/"


# form view
# import generic FormView
from django.views.generic.edit import FormView

# Relative import of GeeksForm
from .forms import InputForm, PostForm

class PostFormView(FormView):
	# specify the Form you want to use
	form_class = PostForm
	
	# specify name of template
	template_name = "app/post_form.html"

	# can specify success url
	# url to redirect after successfully
	# updating details
	success_url ="../all-posts/"


class InputFormView(FormView):
	form_class = InputForm
	template_name = 'app/input_form.html'

	success_url = '../all-posts'