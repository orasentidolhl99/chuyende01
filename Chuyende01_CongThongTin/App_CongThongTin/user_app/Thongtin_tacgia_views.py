from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from ..models import *
from django.urls import reverse_lazy

class HomeView(ListView):
	model = tblTacGia
	template_name = 'them/TacGia/tacgia-home.html'
	context_object_name = 'tacgia'

class TacGiaDetailView(DetailView):
	model = tblTacGia
	template_name = 'them/TacGia/tacgia_detail.html'
	context_object_name = 'tacgia'

class CreateTacGiaView(CreateView):
	model = tblTacGia
	template_name = 'them/TacGia/new_tacgia.html'
	fields = '__all__'

class TacGiaEditView(UpdateView):
	model = tblTacGia
	template_name = 'them/TacGia/edit_tacgia.html'
	fields = ['TenTacGia','PhongBan','SDT']

class TacGiaDeleteView(DeleteView):
	model = tblTacGia
	template_name = 'them/TacGia/delete_tacgia.html'
	context_object_name = 'tacgia'
	success_url = reverse_lazy('news:home')
