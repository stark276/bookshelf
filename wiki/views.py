from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponse, HttpResponseRedirect

from wiki.models import Page
from .forms import PostCreateForm


class PageListView(ListView):
    """ Renders a list of all Pages. """
    model = Page

    def get(self, request):
        """ GET a list of Pages. """
        pages = self.get_queryset().all()
        return render(request, 'list.html', {
          'pages': pages
        })

class PageDetailView(DetailView):
  """ Renders a specific page based on it's slug."""
  model = Page

  def get(self, request, slug):
    """ Returns a specific wiki page by slug. """
    page = self.get_queryset().get(slug__iexact=slug)
    return render(request, 'page.html', {
    'page': page
    })

  def post(self, request, slug):
    page = self.get_queryset().get(slug__iexact=slug)
    form = PostCreateForm(request.POST, initial=page)
    if form.is_valid():
      form.save()




class PostCreateView(CreateView):

  def get(self, request, *args, **kwargs):
      form = PostCreateForm()
      context = {'form': form}
      return render(request, 'form.html', context)

  def post(self, request, *args, **kwargs):
      form = PostCreateForm(request.POST)
      if form.is_valid():
          page = form.save()
          return HttpResponseRedirect(reverse_lazy('wiki-details-page', args=[page.slug])) #because of the slug it goes to that specific page
      return render(request, 'form.html', {'form': form})

