from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, UpdateView, ListView

from .models import Poll


def base_view(request):
    return HttpResponse("ok")


class CreatePollView(CreateView):
    model = Poll
    template_name = 'polls.html'
    fields = '__all__'
    success_url = '/jose'


class UpdatePollView(UpdateView):
    model = Poll
    template_name = 'polls.html'
    success_url = '/jose'
    fields = '__all__'


class ListPollsView(ListView):
    model = Poll
    template_name = 'polls_list.html'
    success_url = '/jose'
