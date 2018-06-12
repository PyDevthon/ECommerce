from django.shortcuts import render
from django.views import generic
from .models import Product


class Home(generic.ListView):
    model = Product
    paginate_by = 9
    context_object_name = 'products'
    template_name = 'Home.html'
    queryset = Product.objects.all()


class Details(generic.DetailView):
    template_name = 'Details.html'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        return Product.objects.get(pk = self.kwargs['key'])

