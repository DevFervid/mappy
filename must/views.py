from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from .forms import ItemForm

from .models import Item, Category

# class IndexView(generic.ListView):
#     template_name = 'must/index.html'
#     context_object_name = 'latest_item_list'

#     def get_queryset(self):
#         #Return the last five published items.
#         return Item.objects.order_by('-created_at')[:50]


# class DetailView(generic.DetailView):
#     model = Item
    # template_name='must/detail.html'


# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form': form})

def create_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
    else:
        form = ItemForm()
    return render(request, 'must/create.html', {'form': form})

def item_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    items = Item.objects.filter()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        items = Item.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'items': items
    }
    return render(request, 'must/list.html', context)

def item_detail(request, id, slug):
    item = get_object_or_404(Item, id=id, slug=slug)
    context = {
        'item': item
    }

    return render(request, 'must/details.html', context)