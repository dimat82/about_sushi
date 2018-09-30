from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from menu.models import *
from order.forms import *
from django.contrib import messages
from django.core.mail import send_mail
from article.models import Article
from django.contrib.auth.models import User

# Create your views here.
class IndexView(ListView):
    template_name = 'index.html'
    model = Article

    def get_queryset(self):
        articles = Article.objects.all()[:3]
        return articles

class RollsList(ListView):
    template_name = 'menu/rolls_list.html'
    model = Rolls

class SushisList(ListView):
    template_name = 'menu/sushi_list.html'
    model = Sushi

class SetList(ListView):
    template_name = 'menu/set_list.html'
    model = Sets

class SoupList(ListView):
    template_name = 'menu/soups_list.html'
    model = Soups

class RollDetail(DetailView):
    model = Rolls
    template_name = 'menu/menu_detail.html'
    form = None
    food_id = None
    back = 'rolls'

    def get(self, request, *args, **kwargs):
        self.food_id = self.kwargs['pk']
        self.form = RollOrderForm(initial={'food':self.food_id})
        return super().get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        context['back'] = self.back
        return context

    def post(self,request,*args,**kwargs):
        self.form = RollOrderForm(request.POST)
        if  self.form.is_valid():
            self.form.save()
            send_mail(self.form.cleaned_data['name'],self.form.cleaned_data['phone'],'tarasovd40@gmail.com',
                      ['dimat82@list.ru'])
            messages.add_message(request,messages.SUCCESS,'{}, Ваш заказ отправлен для обработки!'.format(self.form.cleaned_data['name'].title()))
            return redirect('rolls')
        return super().get(request,*args,**kwargs)

class SetDetail(DetailView):
    model = Sets
    template_name = 'menu/menu_detail.html'
    form = None
    food_id = None
    back = 'sets'

    def get(self, request, *args, **kwargs):
        self.food_id = self.kwargs['pk']
        self.form = SetsOrderForm(initial={'food': self.food_id})
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        context['back'] = self.back
        return context

    def post(self,request,*args,**kwargs):
        self.form = SetsOrderForm(request.POST)
        if  self.form.is_valid():
            self.form.save()
            send_mail(self.form.cleaned_data['name'],self.form.cleaned_data['phone'],'tarasovd40@gmail.com',
                      ['dimat82@list.ru'])
            messages.add_message(request,messages.SUCCESS,'{}, Ваш заказ отправлен для обработки!'.format(self.form.cleaned_data['name'].title()))
            return redirect('rolls')
        return super().get(request,*args,**kwargs)

class SoupDetail(DetailView):
    model = Soups
    template_name = 'menu/menu_detail.html'
    form = None
    food_id = None
    back = 'soups'

    def get(self, request, *args, **kwargs):
        self.food_id = self.kwargs['pk']
        self.form = SoupOrderForm(initial={'food': self.food_id})
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        context['back'] = self.back
        return context

    def post(self,request,*args,**kwargs):
        self.form = SoupOrderForm(request.POST)
        if  self.form.is_valid():
            self.form.save()
            send_mail(self.form.cleaned_data['name'],self.form.cleaned_data['phone'],'tarasovd40@gmail.com',
                      ['dimat82@list.ru'])
            messages.add_message(request,messages.SUCCESS,'{}, Ваш заказ отправлен для обработки!'.format(self.form.cleaned_data['name'].title()))
            return redirect('rolls')
        return super().get(request,*args,**kwargs)

class SushiDetail(DetailView):
    model = Sushi
    template_name = 'menu/menu_detail.html'
    form = None
    food_id = None
    back = 'sushi'

    def get(self, request, *args, **kwargs):
        self.food_id = self.kwargs['pk']
        self.form = SushiOrderForm(initial={'food': self.food_id})
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        context['back'] = self.back
        return context

    def post(self,request,*args,**kwargs):
        self.form = SushiOrderForm(request.POST)
        if  self.form.is_valid():
            self.form.save()
            send_mail(self.form.cleaned_data['name'],self.form.cleaned_data['phone'],'tarasovd40@gmail.com',
                      ['dimat82@list.ru'])
            messages.add_message(request,messages.SUCCESS,'{}, Ваш заказ отправлен для обработки!'.format(self.form.cleaned_data['name'].title()))
            return redirect('rolls')
        return super().get(request,*args,**kwargs)


class Menu(TemplateView):
    template_name = 'menu/menu.html'

    def get(self, request, *args, **kwargs):
        return super().get(request,*args,**kwargs)

