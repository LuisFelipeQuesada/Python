from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from leads.models import Agent
from.forms import AgentModeForm

# Create your views here.
class AgentListView(LoginRequiredMixin, ListView):
    template_name = "agents/agent_list.html"
    form = AgentModeForm

    def get_queryset(self):
        return Agent.objects.all()

class AgentCreateView(LoginRequiredMixin, CreateView):
    template_name = "agents/agent_create.html"

    def get_success_url(self):
        return reverse('agents:agents-list')
