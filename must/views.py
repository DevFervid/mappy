from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Item

class IndexView(generic.ListView):
    template_name = 'must/index.html'
    context_object_name = 'latest_item_list'

    def get_queryset(self):
        #Return the last five published items.
        return Item.objects.order_by('-created_at')[:50]


class DetailView(generic.DetailView):
    model = Item
    template_name='must/detail.html'