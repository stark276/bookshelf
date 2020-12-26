from django.urls import path
from wiki.views import PageListView, PageDetailView, PostCreateView

# app_name = 'wiki'

urlpatterns = [
    path('', PageListView.as_view(), name='wiki-list-page'),
    path('new/', PostCreateView.as_view(), name = 'new_page' ),
    path('<str:slug>/', PageDetailView.as_view(), name='wiki-details-page'),
    path('<str:slug>/edit', PageDetailView.as_view(), name='editing')
]
