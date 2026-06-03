import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizzaOggetti(self, e):
        self._model.buildGraph()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato"))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene {self._model.getNumNodi()} nodi e {self._model.getNumEdges()} archi"))
        #riabilito i campi che avevo bloccato perche da fare solo dopo il grafo
        self._view._txtIdOggetto.disabled= False
        self._view._btnCompConnessa.disabled = False


        self._view.update_page()

    def handleCompConnessa(self,e):
        txtIn =self._view._txtIdOggetto.value
        if txtIn == "" :
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Attenzione inserire un valore nel campo id", color = "red"))
            self._view.update_page()
            return
        try:
            id = int(txtIn)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Attenzione inserire un valore NUMERICO nel campo id", color="red"))
            self._view.update_page()
            return
        if not self._model.hasNode(id):
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(
                ft.Text(f"Attenzione, l'id inserito non è presente nel grafo.", color="orange"))
            self._view.update_page()
            return

        dimensione= self._model.getInfoCompConnessa(id)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text( f"La componente connessa contetente l'oggetto corrispondente all'id {id} ha dimensione {dimensione}",color = "green"))
        #parte due
        self._view._btnCerca.disabled = False
        self._view._ddLun.disabled = False
        lunValues= list(range(2,dimensione))
        #per riempire il dropdown
        #for v in lunValues:
            #self._view._ddLun.option.append(ft.dropdown.Option(v))
        #self._view._ddLun.option = lunValues
        #altra opzione di riempimento
        #lunValuesDD= list(map(lambda x: ft.dropdown.Option(x), lunValues))
        #self._view._ddLun.options = lunValuesDD
        lunValuesDD = list(map(lambda x: ft.dropdown.Option(x), lunValues))

        self._view._ddLun.options = lunValuesDD

        self._view.update_page()

        #parte due
    def handleCerca(self, e):
        source = self._model.getNodeFromID(int(self._view._txtIdOggetto.value))#ho già fatto i controlli nel handle comp connessa
        lun = self._view._ddLun.value
        if lun is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(
                ft.Text("Attenzione scegliere un valore del campo Lunghezza", color="red"))
            self._view.update_page()
        lunInt =int(lun)
        #richiamo i metodi del model
        path, cost = self._model.getOptPath(source, lunInt)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(
            ft.Text(f"Ho trovato un cammino che da {source} con peso totale {cost}",color="green"))
        self._view.txt_result.controls.append(
            ft.Text(f"Di seguito i nodi che compongono questo cammino:", color="green"))
        for p in path:
            self._view.txt_result.controls.append(ft.Text(p))

        self._view.update_page()



        self._view.txt_result.controls.clear()



