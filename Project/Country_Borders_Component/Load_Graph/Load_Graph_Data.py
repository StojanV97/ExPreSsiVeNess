import csv
import os

from Core.models import Graph, Vertex, Edge
from Load_Graph.Country import Country


class LoadGraphData(object):
    __slots__ = '_graph', '_list_of_all_countries', '_list_of_edges', '_europe', '_asia', '_n_america', '_s_america', '_africa'

    def EntryPointName(self):
        return "Countries"

    def __init__(self):
        self._graph = Graph()
        self._list_of_all_countries = []
        self._europe = ["Russian Federation", "Germany", "United Kingdom of Great Britain and Northern Ireland",
                        "France", "Italy", "Spain", "Ukraine", "Poland", "Romania", "Netherlands", "Belgium", "Czechia",
                        "Greece",
                        "Portugal", "Sweden", "Hungary", "Belarus", "Austria", "Serbia", "Switzerland", "Bulgaria",
                        "Denmark", "Finland", "Slovakia", "Norway", "Ireland", "Croatia", "Moldova (the Republic of)",
                        "Bosnia and Herzegovina", "Albania", "Lithuania", "North Macedonia", "Slovenia", "Latvia",
                        "Estonia", "Montenegro", "Luxembourg", "Malta", "Iceland", "Andorra", "Monaco", "Liechtenstein",
                        "San Marino", "Holy See"]
        self._asia = ["China", "India", "Indonesia", "Pakistan", "Bangladesh", "Japan", "Philippines", "Viet Nam",
                      "Turkey",
                      "Iran (Islamic Republic of)", "Thailand", "Myanmar", "Korea (the Republic of)",
                      "Korea (Democratic People's Republic of)", "Iraq",
                      "Afghanistan", "Saudi Arabia", "Uzbekistan", "Malaysia", "Yemen", "Nepal", "Sri Lanka",
                      "Kazakhstan", "Syrian Arab Republic",
                      "Cambodia", "Jordan", "Azerbaijan", "United Arab Emirates", "Tajikistan", "Israel",
                      "Lao People's Democratic Republic",
                      "Lebanon", "Kyrgyzstan", "Turkmenistan", "Singapore", "Oman", "Palestine, State of", "Kuwait",
                      "Georgia", "Mongolia",
                      "Armenia", "Qatar", "Bahrain", "Timor-Leste", "Cyprus", "Cyprus", "Maldives", "Brunei Darussalam"]
        self._n_america = ["Canada", "United States of America", "Mexico", "Cuba", "Dominican Republic", "Puerto Rico",
                           "Guatemala", "Costa Rica", "Panama"]
        self._s_america = ["Colombia", "Venezuela (Bolivarian Republic of)", "Brazil", "Argentina", "French Guiana",
                           "Guyana",
                           "Paraguay", "Peru", "Suriname", "Uruguay", "Bolivia (Plurinational State Of)", "Ecuador",
                           "Chile"]

        self._africa = ["Algeria", "Libya", "Mali", "Mauritania", "Niger", "Tunisia", "Western Sahara", "Egypt",
                        "Sudan",
                        "Cote d’Ivoire", "Guinea", "Guinea-Bissau", "Liberia", "Senegal", "Sierra Leone",
                        "Gambia (the)",
                        "Benin", "Burkina Faso", "Ghana", "Togo", "Nigeria", "Cameroon", "Chad", "Ethiopia", "Eritrea",
                        "South Sudan", "Djibouti", "Kenya", "Somalia", "Sudan",
                        "Congo (the Democratic Republic of the)",
                        "Angola", "Burundi", "Central African Republic", "Rwanda", "Tanzania (the United Republic of)",
                        "Uganda", "Zambia", "Gabon", "Equatorial Guinea", "Malawi", "Mozambique", "Eswatini",
                        "South Africa",
                        "Zimbabwe", "Botswana", "Lesotho", "Namibia", "Madagascar"]

    @property
    def graph(self):
        return self._graph

    @property
    def list_of_all_countries(self):
        return self._list_of_all_countries

    def initialize_countries(self, file_path):

        if os.path.isfile(file_path) is False:
            print("File doesn't exist!")
            return None

        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            line_counter = 0
            for row in reader:
                if line_counter == 0:
                    pass
                elif line_counter >= 1:
                    country = Country(row[0], row[1])
                    country.country_border_codes.append(row[2])
                    country.country_border_names.append(row[3])
                    self.list_of_all_countries.append(country)
                line_counter += 1

    def filter_countries(self):
        for country in self.list_of_all_countries:
            for country2 in self.list_of_all_countries:
                if country.country_name == country2.country_name:
                    if country.country_border_names != country2.country_border_names:
                        country.country_border_names.append(country2.country_border_names[0])
                        country.country_border_codes.append(country2.country_border_codes[0])

    def initialize_graph(self, _list):
        _dict = {}
        for country in _list:
            _dict[country.country_name] = country
        for country in _dict:
            vertex = Vertex(_dict[country],country)
            self.graph.insert_vertex(vertex)
        for vertex in self.graph.outgoing:
            edges = []
            for country in vertex.element.element.country_border_names:
                e = Edge(vertex.element.element.country_name, country)
                edges.append(e)
            self._graph.outgoing[vertex] = edges

        # for vertex in self.graph.outgoing:
        #     for edge in self.graph.outgoing[vertex]:
        #         if edge._origin == vertex.element.name:
        #             edge.ajdis = vertex.element.ajdi
        #         if edge._destination == vertex.element.name:
        #             edge.ajdid = vertex.element.ajdi

    def display_graph(self):
        for vertex in self._graph.outgoing:
            print(vertex.element.element.country_name)
            for edge in self._graph.outgoing[vertex]:
                print(str(edge))
            print("\n")

    def display_all_countries(self, graph, combobox):
        graph2 = Graph()
        if combobox == "Europe":
            for country in graph.outgoing:
                for country_name in self._europe:
                    if country.element.element.country_name == country_name:
                        graph2.insert_vertex(country.element, country.element.element.country_name)
            return graph2
        elif combobox == "Asia":
            for country in graph.outgoing:
                for country_name in self._asia:
                    if country.element.element.country_name == country_name:
                        graph2.insert_vertex(country.element)
            return graph2
        elif combobox == "Africa":
            for country in graph.outgoing:
                for country_name in self._africa:
                    if country.element.element.country_name == country_name:
                        graph2.insert_vertex(country.element)
            return graph2
        elif combobox == "North America":
            for country in graph.outgoing:
                for country_name in self._n_america:
                    if country.element.element.country_name == country_name:
                        graph2.insert_vertex(country.element)
            return graph2
        elif combobox == "South America":
            for country in graph.outgoing:
                for country_name in self._s_america:
                    if country.element.element.country_name == country_name:
                        graph2.insert_vertex(country.element)
            return graph2
        else:
            graph2 = graph
            return graph2

    def load_countries(self, file_path):
        self.initialize_countries(file_path)
        self.filter_countries()
        self.initialize_graph(self._list_of_all_countries)
        return self._graph


if __name__ == '__main__':
    ld = LoadGraphData()
    ld.initialize_countries(
        "D:\\Fakultet\\Projekti\\SOK_02_15_2020\\ExPreSsivNess\\Project\\Country_Borders_Component\\Load_Graph\\GEODATASOURCE-COUNTRY-BORDERS.CSV")
    ld.filter_countries()
    ld.initialize_graph(ld.list_of_all_countries)
    ld.display_graph()