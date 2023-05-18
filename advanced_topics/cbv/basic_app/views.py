from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models


class IndexView(TemplateView):
    template_name = 'index.html'


class SchoolListView(ListView):
    model = models.School
    context_object_name = 'schools'


class SchoolDetailView(DetailView):
    model = models.School
    context_object_name = 'school_detail'
    template_name = 'basic_app/school_detail.html'


class SchoolCreateView(CreateView):
    model = models.School
    fields = ('name', 'principal', 'location')


class SchoolUpdateView(UpdateView):
    model = models.School
    fields = ('name', 'principal')


class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:list')
