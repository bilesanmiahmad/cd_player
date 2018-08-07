from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from pastebin.models import Paste

# Create your views here.


class PasteCreate(CreateView):
    model = Paste
    fields = ['name', 'text']


class PasteDetail(DetailView):
    model = Paste
    template_name = "pastebin/paste_detail.html"


class PasteList(ListView):
    model = Paste
    queryset = Paste.objects.all()
    template_name = "pastebin/paste_list.html"
    context_object_name = 'queryset'


class PasteUpdate(UpdateView):
    model = Paste
    fields = ['name', 'text']


class PasteDelete(DeleteView):
    model = Paste
    success_url = reverse_lazy('pastebin_paste_list')
