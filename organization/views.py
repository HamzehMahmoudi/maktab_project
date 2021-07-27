from django.db.models.fields import related
from . import models
from django.shortcuts import redirect, render
from django.views import generic
from .forms import OrganForm
from django.core.exceptions import PermissionDenied


class CreateOragan(generic.CreateView):
    """
    salesman can add an organization using this view 
    """
    form_class = OrganForm
    template_name = "organization/creatorgan.html"
    success_url = 'organlist'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.creator = self.request.user
        instance.save()
        return redirect('organlist')


class Organlist(generic.ListView):
    """
    view to see all organizations together 
    """
    model = models.Organization
    template_name = "organization/organlist.html"
    paginate_by = 10  # show 10 organization per page

    def get_queryset(self):  # only org creator can see oganization
        return models.Organization.objects.filter(creator=self.request.user)


class OrgDetail(generic.DetailView):
    model = models.Organization

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        if self.request.user == obj.creator:  # only org creator can see details
            return super().get(request, *args, **kwargs)
        else:
            raise PermissionDenied


class ProductList(generic.ListView):
    model = models.Product
    paginate_by = 10