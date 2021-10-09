from django.shortcuts import render, redirect, reverse
from django.views import View # <- View class to handle requests 
from django.http import HttpResponse # <- a class to handle sending a type of response 
from django.views.generic.base import TemplateView 
from .models import Champion, Abilities
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

@method_decorator(login_required, name='dispatch')
class Characters(TemplateView):
    template_name = 'characters.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        if name != None:
            context['champions'] = Champion.objects.filter(name__icontains=name, user=self.request.user)
            context['header'] = f"Searching for {name}"
        else:
            
            context["champions"] = Champion.objects.filter(user=self.request.user) # this is where we add the key into our context object for the view to use
            return context

class Profile(TemplateView):
    template_name = 'profile.html'
    
class CharacterCreate(CreateView):
    model = Champion
    fields = ['name', 'img', 'bio']
    template_name = 'character_create.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CharacterCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
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
    
class AbilityCreate(View):
    def post(self, request, pk):
        
        skill1 = request.POST.get('skill1')
        champion = Champion.objects.get(pk=pk)
        Abilities.objects.create(skill1=skill1)
        return redirect('character_detail', pk=pk)
    
class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home.html")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
    

