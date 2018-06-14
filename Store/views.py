from django.views import generic
from .models import Product, CATEGORIES, Contact
from .forms import ContactForm


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
