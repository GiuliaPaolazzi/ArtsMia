from database.DAO import DAO
from model.model import Model

allobj = DAO.getAllNodi()
print(len(allobj))
mdl= Model()
mdl.buildGraph()
print(f" Il Grafo contiene {mdl.getNumNodi()} nodi e {mdl.getNumEdges()}")
dim =mdl.getInfoCompConnessa(1224)
print(f"DIM = {dim}")