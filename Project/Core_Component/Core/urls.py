from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('read',views.utilize_plugins,name='read_plugins'),
    path('tree',views.tree_layout,name='tree_layout'),
    path('search',views.search_country,name='search_country'),
    path('continents',views.display_countries,name='show_continent'),
    path('force',views.force_graph,name="force_layout_view")


]