# from Core.models import search
from django.apps.registry import apps
from django.http import HttpResponse
from django.shortcuts import render, redirect


def landing_page(request):
    load_plugins = apps.get_app_config('Core_Component').list_of_plugins
    flag = apps.get_app_config('Core_Component').flag
    graph = apps.get_app_config('Core_Component').graph
    graph_f_c = apps.get_app_config('Core_Component').graph_for_continents
    context_variables = {"title": "Graph Vizualization", "load_plugins": load_plugins,
                         "graph": graph, "flag": flag, "g_f_c": graph_f_c}
    return render(request, 'base.html', context_variables)

def force_graph(request):
    return render(request,'forcelayout.html',{})

def tree_layout(request, g_f_c, name, load_plugins, graph):
    vertex = graph.search(name)
    flag = apps.get_app_config('Core_Component').flag
    json_vertex = graph.create_json_from_vertex(vertex)
    if vertex is None:
        return redirect('landing_page')
    context_variables = {"title": "Graph Vizualization", "load_plugins": load_plugins,
                         "graph": graph, "json": json_vertex, "g_f_c": g_f_c, "flag": flag}
    return render(request, "treelayout.html", context_variables)


def search_country(request):
    name = request.POST.get("country")
    if name is None:
        return redirect('landing_page')
    load_plugins = apps.get_app_config('Core_Component').list_of_plugins
    g_f_c = apps.get_app_config('Core_Component').graph_for_continents
    for v in g_f_c.outgoing:
        v.element.found = False
    graph = apps.get_app_config('Core_Component').graph
    try:
        response = tree_layout(request, g_f_c, name, load_plugins, graph)
        return response
    except:
        return redirect('landing_page')


def utilize_plugins(request):
    plugins_initialized = apps.get_app_config('Core_Component').list_of_plugins
    countries_plugin = None
    for plugin in plugins_initialized:
        if plugin.EntryPointName() == "Countries":
            countries_plugin = plugin
    path = request.POST.get("path")
    apps.get_app_config('Core_Component').graph = countries_plugin.load_countries(path)
    return redirect('landing_page')


def display_countries(request):
    load_plugins = apps.get_app_config('Core_Component').list_of_plugins
    g_f_c = apps.get_app_config('Core_Component').graph_for_continents
    countries_plugin = None
    countries = request.POST.get("countries")
    for plugin in load_plugins:
        if plugin.EntryPointName() == "Countries":
            countries_plugin = plugin
    apps.get_app_config('Core_Component').graph_for_continents = countries_plugin.display_all_countries(
        apps.get_app_config('Core_Component').graph, countries)
    apps.get_app_config('Core_Component').flag = True
    context_variables = {"title": "Graph Vizualization",
                         "load_plugins": apps.get_app_config('Core_Component').list_of_plugins,
                         "graph": apps.get_app_config('Core_Component').graph, "g_f_c": g_f_c}
    return redirect('landing_page')
