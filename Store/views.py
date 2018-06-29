from django.views import generic
from .models import Product, CATEGORIES, Contact
from .forms import ContactForm, LoginForm
from django.contrib.auth.views import LoginView, login, logout
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.shortcuts import HttpResponseRedirect, render

# Bokeh

from bokeh.plotting import figure, output_file, show
from bokeh.embed import components


class Home(generic.ListView):
    model = Product
    paginate_by = 9
    context_object_name = 'products'
    template_name = 'Home.html'
    queryset = Product.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['categories'] = CATEGORIES
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        search_query = self.request.GET.get('query', '')
        category = self.request.GET.get('category', '')
        if search_query != '':
            qs = qs.filter(name__icontains=search_query)
        if category != '':
            qs = qs.filter(category=category)
        return qs


class Details(generic.DetailView):
    template_name = 'Details.html'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        return Product.objects.get(pk=self.kwargs['detail_id'])


class AddContact(generic.FormView):
    form_class = ContactForm
    template_name = 'ContactForm.html'

    def form_valid(self, form):
        form = form.save(commit=False)
        form.product = Product.objects.get(pk=self.kwargs['item_id'])
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.request.META['HTTP_REFERER']


class ViewContact(generic.ListView):
    model = Contact
    paginate_by = 20
    context_object_name = 'contacts'
    template_name = 'AdminTable.html'

    def get_queryset(self):
        return Contact.objects.all()


class UserLogin(LoginView):
    template_name = 'registration/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('Home_Page')

    def form_valid(self, form):
        login(self.request, form.get_user())
        return JsonResponse({'Message': 'Success'}, status=200)

    def form_invalid(self, form):
        return JsonResponse({'data': form.errors.as_text()}, status=404)


class UserLogout(generic.View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


class BokehView(generic.View):

    def get(self, request):
        x = Product.objects.get_categories()
        y = Product.objects.get_count()

        p = figure(x_range=x, plot_height=500, title="Product Counts", plot_width=1000)
        p.vbar(x=x, top=[x[1] for x in y], width=0.1)

        p.xgrid.grid_line_color = None
        p.y_range.start = 0

        # Store components
        script, div = components(p)

        data = {'script': script, 'div': div}

        # Feed them to the Django template.
        return JsonResponse(data=data)
