
from django.template import RequestContext
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from .models import Product, Combo
from .forms import ProductSelectForm


class ProductList(ListView):
    model = Product


class ProductView(DetailView):
    model = Product


class ProductCreate(CreateView):
    model = Product
    fields = [
        'name',
        'description',
        'price',
        'quantity'
    ]
    success_url = reverse_lazy('bomboniere:product:product_list')


class ProductUpdate(UpdateView):
    model = Product
    fields = [
        'name',
        'description',
        'price',
        'quantity'
    ]
    success_url = reverse_lazy('bomboniere:product:product_list')


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('bomboniere:product:product_list')


class ComboList(ListView):
    model = Combo


class ComboView(DetailView):
    model = Combo


class ComboCreate(CreateView):
    model = Combo
    fields = [
        'name',
        'description',
        'price',
        'quantity'
    ]
    success_url = reverse_lazy('bomboniere:combo:combo_list')


class ComboUpdate(UpdateView):
    model = Combo
    fields = [
        'name',
        'description',
        'price',
        'quantity'
    ]
    success_url = reverse_lazy('bomboniere:combo:combo_list')


class ComboDelete(DeleteView):
    model = Combo
    success_url = reverse_lazy('bomboniere:combo:combo_list')


class ProductSelect(FormView):

    form_class = ProductSelectForm

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, **kwargs):
        combo_id = kwargs['pk']
        combo = Combo.objects.get(id=combo_id)

        products = form.cleaned_data.get('products')
        
        for product_id in products:
            product = Product.objects.get(id=product_id)
            combo.products.add(product)

        return HttpResponseRedirect(self.get_success_url(combo_id))
    
    def get_success_url(self, combo_id):
        """Return the URL to redirect to after processing a valid form."""
        
        success_url = reverse_lazy('bomboniere:combo:combo_view', kwargs={'pk': combo_id})

        return str(success_url)  # success_url may be lazy
