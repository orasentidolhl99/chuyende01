from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from ..models import *
from django.urls import reverse_lazy
from ..forms import *

class HomeView(ListView):
	model = tbltinBai
	template_name = 'them/tinbai/home_tinbai.html'
	#queryset = tblLinhVuc.objects.all()[:5]
	context_object_name = 'tinbai'

class TinBaiDetailView(DetailView):
	model = tbltinBai
	template_name = 'them/tinbai/tinbai_detail.html'
	context_object_name = 'tinbai'

class CreateTinBaiView(CreateView):
	model = tbltinBai
	template_name = 'them/tinbai/new_tinbai.html'
	fields = '__all__'


class TinBaiEditView(UpdateView):
	model = tbltinBai
	template_name = 'them/tinbai/edit_tinbai.html'
	fields = '__all__'

class TinBaiDeleteView(DeleteView):
	model = tbltinBai
	template_name = 'them/tinbai/delete_tinbai.html'
	context_object_name = 'tinbai'
	success_url = reverse_lazy('news:home-tinbai')
