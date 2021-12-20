from django.shortcuts import render
from .forms import UserRegisterForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView, ListView
from .models import Item, Season
from django.contrib.auth.mixins import LoginRequiredMixin



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created has been created! You are now able to log in')
            return redirect('#')
    else:
        form = UserRegisterForm()    
    return render(request, 'users/register.html', {'form':form})



def home(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'users/home.html', context)

class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    fields = ['name', 'about', 'price']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)  

class SeasonCreateView(LoginRequiredMixin, CreateView):
    model = Season
    fields = ['season_name', 'start_date', 'end_date']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)  



class ItemListView(ListView):
    model = Item
    template_name = 'users/home.html' # <app>/<model>_<viewtype>.html 
    context_object_name = 'items'
    ordering = ['-date_posted'] 
    
    def get_context_data(self, **kwargs):
        ctx = super(ItemListView, self).get_context_data(**kwargs)
        ctx['seasons'] = Season.objects.all()
        return ctx

