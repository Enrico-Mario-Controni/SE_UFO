import flet as ft

class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def populate_dd(self):
        """ Metodo per popolare i dropdown """
        # TODO
        anni= self._model.get_years()

        self._view.dd_year.options = [ft.dropdown.Option(anno) for anno in anni]


    def on_change_years(self,e):
        self.anno_selezionato= self._view.dd_year.value

        forme= self._model.get_shape(self.anno_selezionato)

        self._view.dd_shape.options= [ft.dropdown.Option(forma) for forma in forme]

        self._view.update()

    def on_change_shapes(self,e):

        self.forma_selezionata= self._view.dd_shape.value
        print(self.anno_selezionato)
        print(self.forma_selezionata)


    def handle_graph(self, e):
        """ Handler per gestire creazione del grafo """
        # TODO
        grafo=self._model.get_graph(self.anno_selezionato, self.forma_selezionata)

        dizionario_pesi=self._model.get_edges_near()

        self._view.lista_visualizzazione_1.controls.append(ft.Text(f" {grafo}"))

        for el in dizionario_pesi:
            self._view.lista_visualizzazione_1.controls.append(ft.Text(f" Nodo {el}, somma peso su archi {dizionario_pesi[el]} "))


        self._view.page.update()


    def handle_path(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del cammino """
        # TODO

        distanza, cammino = self._model.ricorsione()

        for el in range(len(cammino)-1):
            self._view.lista_visualizzazione_2.controls.append(ft.Text(f" {cammino[el]} -->{cammino[el+1]}, distanza {distanza} "))
        self._view.page.update()



