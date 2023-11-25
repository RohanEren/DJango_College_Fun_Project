from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student
from django.urls import reverse_lazy

class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    fields = "__all__"
    success_url = '/'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'studetail.html'

class StudentCreateView(CreateView):
    model = Student
    template_name = 'forms.html'
    fields = ['name', 'departent', 'rollnumber', 'accountnumber', 'amount']

class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'stuupdate.html'
    fields = ['name', 'departent', 'rollnumber', 'accountnumber', 'amount']
    success_url = '/'

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'studelete.html'
    success_url = '/'
    
class StudentListView(ListView):
    model = Student
    template_name = 'stulist.html'
    context_object_name = 'student_list'
    
