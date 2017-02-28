from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .forms import ReportForm
from .models import Project, Report



class ReportFormView(FormView):
	form_class = ReportForm
	# model = Contact
	initial = {'key': 'value'}
	template_name = 'report_form.html'
	success_url = '/thanks/'

	def get(self, request, *args, **kwargs):
		form = self.form_class(initial=self.initial)
		return render(request, self.template_name, {'form': form})


	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
		return render(request, self.template_name, {'form': form})

class ProjectDetailView(DetailView):
	model = Project
	template_name = 'inner.html'

	def get_context_data(self, **kwargs):
		context = super(ProjectDetailView, self).get_context_data(**kwargs)
		return context


class ProjectListView(ListView):
	model = Project
	template_name = 'project_list.html'

	def get_context_data(self, **kwargs):
		context = super(ProjectListView, self).get_context_data(**kwargs)
		return context

def home(request):
	template_name = 'index.html'
	return render(request, template_name, {})

def inner(request):
    return render(request, 'inner.html', {})