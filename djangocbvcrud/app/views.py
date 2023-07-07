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


class ExpenseRecord(CreateView):
	model = Expense
	fields = ['category', 'title', 'amount', 'total']
	success_url = '../all-expense/'


class ExpenseList(ListView):
	model = Expense


def DeleteExpense(request):
	if request.method == 'GET':
		reqId = request.GET['id']
		obj = Expense.objects.get(id=reqId)
		id = obj.pk
		obj.delete()
		return HttpResponse(f"record # {id} delete successfully")
	else:
		return HttpResponse("Request method incorrect")
	

def VolumeCalc(request):
	result = {}
	products = Product.objects.all()
	if request.method == 'POST':
		data = request.POST.copy()
		vol = 0 
		wei = 0
		for product in products:
			if data.get(f'{product.pk}'):
				vol += float(data.get(f'{product.pk}')) * product.pacHeight * product.pacLong * product.pacWidth / product.piePerPackage
				wei += float(data.get(f'{product.pk}')) / 5000
		print(vol, wei)
		result = {'vol': vol, 'wei': wei}
	volumes = Volume.objects.all()
	context = {'volumes': volumes, 'products': products, 'result': result}
	return render(request, 'app/volume.html', context)


from calendar import Calendar
from datetime import datetime
def ScheduleGenerator(range, list, supervisor): 
	# range={'year':xxxx, 'month':xx}
	# list is a list of employee
	schedules = {}
	cal = Calendar()
	listInit = 0
	# for c in cal.itermonthdays(range['year'], range['month']):
	for c in cal.itermonthdates(range['year'], range['month']):
		if c.month != range['month']-1 and c.month != range['month']+1:
			schedules[c] = {list[listInit % len(list)]: supervisor[listInit % len(supervisor)]}
			listInit += 1
	return schedules
def Schedule(request):
	employees = Employee.objects.all()
	avaEmployees = Employee.objects.filter(available=True)
	supervisors = Employee.objects.filter(supervisor=True)
	today = datetime.now()
	range = {'year': today.year, 'month': today.month}
	if request.method == 'POST':
		data = request.POST.copy()
		# get year and month from user
		if data.get('year') and data.get('month'):
			range['year'] = int(data.get('year'))
			range['month'] = int(data.get('month'))
		# change employee's available status
		for emp in employees:
			if data.get(f'{emp.pk}'):
				emp.available = True
				emp.save()
			else:
				emp.available = False
				emp.save()
	# generate schedule with ScheduleGenerator method
	schedules = ScheduleGenerator(range, avaEmployees, supervisors)
	print(schedules)
	context = {'employees': employees, 'schedules': schedules}
	return render(request, 'app/schedule.html', context)


