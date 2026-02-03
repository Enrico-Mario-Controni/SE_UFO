from database.dao import  DAO
import networkx as nx
from geopy import distance

class Model:

    def __init__(self):
        self.G= nx.Graph()

    def get_years(self):
        anni= DAO.get_years()
        return anni

    def get_shape(self, anno):
        forme= DAO.get_shape(anno)
        return forme

    def get_graph(self, anno, forma):
        nodes= DAO.get_state()

        for el in nodes:
            self.G.add_node(el[1])

        edges= DAO.get_neighbors(anno, forma)
        for el in edges:
            self.G.add_edge(el[0], el[1], peso=el[2])

        return self.G

    def get_edges_near(self):

        dizionario_pesi={}

        nodi= self.G.nodes()

        for nodo in nodi:

            successori= self.G.neighbors(nodo)
            dizionario_pesi[nodo]= 0

            for el in successori:
                peso= self.G[nodo][el]["peso"]
                dizionario_pesi[nodo]+=peso

        return dizionario_pesi

    def get_coordinate(self):

        coordinate= DAO.get_coordinate()

        self.dizionario_coordinate= {}

        for el in coordinate:

            self.dizionario_coordinate[el[0]]= (el[1], el[2])

        return self.dizionario_coordinate


    def ricorsione(self):

        best_distance=0
        best_path=[]

        nodi=self.G.nodes()

        self.dizionario_coordinate= self.get_coordinate()

        for nodo in nodi:

            distance, cammino = self.path_find(nodo, -1,[nodo])

            if distance > best_distance:
                best_distance=distance
                best_path=cammino

        return  best_distance,best_path



    def path_find(self, nodo, peso_precedente, lista_cammino):

        distanza=0
        cammino= lista_cammino.copy()

        successori=self.G.neighbors(nodo)


        for el in successori:
            peso= self.G[nodo][el]["peso"]

            lat1, lng1 = self.dizionario_coordinate[nodo.lower()]
            lat2, lng2 = self.dizionario_coordinate[el.lower()]

            distanza_corrente = distance.geodesic((lat1, lng1), (lat2, lng2)).km



            if peso > peso_precedente and el not in lista_cammino  :


                    totale, path = self.path_find(el, peso, lista_cammino+[el])

                    if totale + distanza_corrente > distanza:
                        distanza= totale + distanza_corrente
                        cammino=path

        return distanza, cammino















