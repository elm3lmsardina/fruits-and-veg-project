from django.contrib.auth.decorators  import login_required
from .forms import UserRegisterForm, UserUpdateForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView, ListView, DetailView
from .models import Item, Season, Type
from django.contrib.auth.mixins import LoginRequiredMixin



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()    
    return render(request, 'users/register.html', {'form':form})



def home(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'users/home.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('home')

    else:
        u_form = UserUpdateForm(instance=request.user)
    
    context = {
        'u_form': u_form
    }
    return render(request, 'users/profile.html', context)

class ItemListView(ListView):
    
    model = Item
    template_name = 'users/home.html' # <app>/<model>_<viewtype>.html 
    context_object_name = 'items'
    ordering = ['-date_posted'] 
    
    def get_context_data(self, **kwargs):
        the_season = self.request.GET.get('the_season', None)
        items = None
        if the_season == None:
            items = Item.objects.all()
        else:
            items =  Item.objects.filter(season_id=the_season)

       
        ctx = super(ItemListView, self).get_context_data(**kwargs)
        ctx['seasons'] = Season.objects.all()
        ctx['items'] = items
        return ctx

class ItemDetailView(DetailView):
    model = Item


#class ItemCreateView(LoginRequiredMixin, CreateView):
 #   model = Item
 #   fields = ['name', 'about', 'price']

 #   def form_valid(self, form):
#      form.instance.author = self.request.user
 #       return super().form_valid(form)  

#class SeasonCreateView(LoginRequiredMixin, CreateView):
#    model = Season
#    fields = ['season_name', 'start_date', 'end_date']

#    def form_valid(self, form):
#        form.instance.author = self.request.user
#        return super().form_valid(form)  

#class TypeCreateView(LoginRequiredMixin, CreateView):
#    model = Type
#    fields = ['type_name']

 #   def form_valid(self, form):
#        form.instance.author = self.request.user
#        return super().form_valid(form)          




    
