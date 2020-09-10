from django.db import models


# vetrtex_count() - broj cvorova
# vertices() - lista svih cvorova
# edge_count()  - broj grana
# edges() - lista svig grana
# get_edge(u,v)  - vraca granu izmedju u i v, inace None
# degree(v,out=True)  - broj izlaznih/ulazih grana u v
# incident_degree(v,out=True) - lista izlaznih/ulaznih grana u v
# insert_vertex(x) - dodaj novi cvor sa sadrzajem x
# insert_edge(u,v,x=None) - dodaj novu granu od u ka v sa sadrzajem x
# remove_vertex(v) - ukloni cvor i sve vezane grane
# remove_edge(e) - ukloni granu e


class Vertex(object):

    def __init__(self, x,name = None):
        # self._ajdi = ide
        self._element = x
        self._found = False
        self._name = name

    # @property
    # def ajdi(self):
    #     return self._ajdi

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def found(self):
        return self._found

    @found.setter
    def found(self, value):
        self._found = value

    @property
    def element(self):
        return self._element

    def __hash__(self):  # will allow vertex to be a map/set key
        return hash(id(self))

    def __str__(self):
        return "{} {}".format(str(self._element), self._found)


class Edge:

    def __init__(self, u, v):
        # self._ajdi_d = None
        # self._ajdi_s = None
        self._origin = u
        self._destination = v

    # @property
    # def ajdis(self):
    #     return self._ajdi_s

    # @ajdis.setter
    # def ajdis(self,x):
    #     self._ajdi_s = x    

    # @property
    # def ajdid(self):
    #     return self._ajdi_d

    # @ajdid.setter
    # def ajdid(self,x):
    #     self._ajdi_d = x    

    def endpoints(self):
        return self._origin, self._destination

    def opposite(self, v):
        if not isinstance(v, Graph.Vertex):
            raise TypeError('v must be a Vertex')
        return self._destination if v is self._origin else self._origin
        # raise Exception('v not incident to edge')

    # @property
    # def element(self):
    #     return self._element
    #
    # @element.setter
    # def element(self, value):
    #     self._element = value

    # @property
    # def origin(self):
    #     return self._origin
    
    # @property
    # def destination(self):
    #     return self.destination

    def __hash__(self):  # will allow edge to be a map/set key
        return hash((self._origin, self._destination))

    def __str__(self):
        return '({0},{1})'.format(self._origin, self._destination)


class Graph(object):

    def __init__(self, directed=False):
        self._outgoing = {}
        # self._edges = []
        self._incoming = {} if directed else self._outgoing

    @property
    def outgoing(self):
        return self._outgoing

    def search(self, name):
        v = None
        for vertex in self._outgoing:
            if vertex.element.name.upper() == name.upper():
                vertex.element.found = True
                v = vertex
        return v

    def _validate_vertex(self, v):
        if not isinstance(v, Vertex):
            raise TypeError('Vertex expected')
        if v not in self._outgoing:
            raise ValueError('Vertex does not belong to this graph.')

    def insert_vertex(self,x=None, name=None):
        v = Vertex(x,name)
        self._outgoing[v] = []  # lista cvorova sa kojima je povezan
        if self.is_directed():
            self._incoming[v] = []  # need distinct map for incoming edges
        return v

    def is_directed(self):
        return self._incoming is not self._outgoing

    def vertex_count(self):
        return len(self._outgoing)

    def vertices(self):
        return self._outgoing.keys()

    def edge_count(self):
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed() else total // 2

    def edges(self):
        result = set()  # avoid double-reporting edges of undirected graph
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())  # add edges to resulting set
        return result

    def get_edge(self, u, v):
        self._validate_vertex(u)
        self._validate_vertex(v)
        return self._outgoing[u].get(v)  # returns None if v not adjacent

    def degree(self, v, outgoing=True):
        self._validate_vertex(v)
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing=True):
        self._validate_vertex(v)
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge

    def insert_edge(self, u, v, x=None):
        if self.get_edge(u, v) is not None:  # includes error checking
            raise ValueError('u and v are already adjacent')
        e = Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e

    def create_json_from_vertex(self, vertex):
        name = '{"name":'
        cildrens = ""
        for c_name in vertex.element.element.country_border_names:
            cildrens += name + '"' + c_name + '"' + '}' + ","

        text = '{"name":' + '"Vertex"' + ',"children":' + '[{' + '"name":' + '"' + str(
            vertex.element.element.country_name) + '"' + ',"children":' + "[" + cildrens[
                                                                                          :-1] + "]" + "}," + '{"name":' + '"'+str(
            vertex.element.element.country_code) + '"' + "}]}"
        return text

