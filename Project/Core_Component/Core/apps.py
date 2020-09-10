import pkg_resources
from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'Core_Component'
    _graph = None
    _graph_for_continents = None
    _flag = False
    list_of_plugins = []

    @property
    def graph_for_continents(self):
        return self._graph_for_continents

    @graph_for_continents.setter
    def graph_for_continents(self, value):
        self._graph_for_continents = value

    @property
    def flag(self):
        return self._flag

    @flag.setter
    def flag(self, value):
        self._flag = value

    @property
    def graph(self):
        return self._graph

    @graph.setter
    def graph(self, value):
        self._graph = value

    def ready(self):
        self.list_of_plugins = load_plugins('Graph.Load')


def load_plugins(plugin_type):
    plugins = []
    # print(plugin_type)
    for ep in pkg_resources.iter_entry_points(group=plugin_type):
        print(ep)
        p = ep.load()
        print("{} {}".format(ep.name, p))
        plugin = p()
        plugins.append(plugin)

    return plugins
