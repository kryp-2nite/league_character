from django.shortcuts import render
from django.views import View # <- View class to handle requests 
from django.http import HttpResponse # <- a class to handle sending a type of response 
from django.views.generic.base import TemplateView 
from .models import Champion
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse


# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

class Characters(TemplateView):
    template_name = 'characters.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        if name != None:
            context['champions'] = Champion.objects.filter(name__icontains=name)
            context['header'] = f"Searching for {name}"
        else:
            
            context["champions"] = Champion.objects.all() # this is where we add the key into our context object for the view to use
            return context

    
class CharacterCreate(CreateView):
    model = Champion
    fields = ['name', 'img', 'bio']
    template_name = 'character_create.html'
    
    def get_success_url(self):
        return reverse('character_detail', kwargs={'pk': self.object.pk})
        
class CharacterDetail(DetailView):
    model = Champion
    template_name = 'character_detail.html'

class CharacterUpdate(UpdateView):
    model = Champion
    fields = ['name', 'img', 'bio']
    template_name = 'character_update.html'
    def get_success_url(self):
        return reverse('character_detail', kwargs={'pk': self.object.pk})

class CharacterDelete(DeleteView):
    model = Champion
    template_name = 'character_delete_confirm.html'
    success_url = "/characters/"
