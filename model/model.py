import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo =nx.Graph() #perche pesato semplice
        self._nodes = DAO.getAllNodi()
        self._idMapAO = {}
        for n in self._nodes:
            self._idMapAO[n.object_id]= n
        #per ricorsione
        self._optPath =[]
        self._optCost = 0




    def buildGraph(self):
        #nodi

        self._grafo.add_nodes_from(self._nodes)
        #archi
        self.addEdges()

    def addEdges(self):
        alledges = DAO.getEdgesPeso(self._idMapAO)
        for e in alledges:

            self._grafo.add_edge(e.o1, e.o2, weight=e.peso)

    def getNumNodi(self):
        return len(self._nodes)
    def getNumEdges(self):
        return len(self._grafo.edges)
    #puntod
    def getInfoCompConnessa(self, id_oggetto):
        #cercare componente connessa che contenga id oggetto
        #metodo dfs
        #cercare nella documantazione
        if not self.hasNode(id_oggetto):
            return None
        source= self._idMapAO[id_oggetto]
        dfsTree = nx.dfs_tree(self._grafo, source)
        print("size connessa con dfs_tree", len(dfsTree.nodes()))
        #altre due strategie da guardare dalle soluzioni
        return len(dfsTree.nodes())

    def hasNode(self, id_oggetto):
        return id_oggetto in self._idMapAO
    #parte due dopo view e controller
    #funzione gestore della ricorsione
    def getOptPath(self, source, lun):
        parziale = [source]
        #uso backtracking: aggiungo un nodo provo poi lo tolgo e provo un altro
        for n in self._grafo.neighbors(source):
            if n.classification == parziale[-1].classification:
                parziale.append(n)
                self._ricorsione(parziale, lun)
                parziale.pop()
        return self._optPath, self._optCost

    def _ricorsione(self, parziale, lun):
        #verificare condizione di terminazione
        if len(parziale) == lun:
            #verifico che sia meglio del mio best (condizione di ottimalita)
            if self._costoPath(parziale)> self._optCost:
                self._optCost = self._costoPath(parziale)
                #salvo deepcopy di parziale come solu ottima
                self._optPath = copy.deepcopy(parziale)
            # poi esco in ogni caso
            return
        #posso ancora aggiungere
        #copio da prima ma cambio source con parziale[-1]
        for n in self._grafo.neighbors(parziale[-1]):
            if n.classification == parziale[-1].classification:
                parziale.append(n)
                self._ricorsione(parziale, lun)
                parziale.pop() #backtracking

    #funzione che calcola costo path (somma peso archi)
    def _costoPath(self, path):
        costo =0
        for i in range (0, len(path) -1):
            costo += self._grafo[path[i]][path[i + 1]]["weight"]
        return costo
    def getNodeFromID(self, id_oggetto):
        return self._idMapAO[id_oggetto]
    #collego al controller









