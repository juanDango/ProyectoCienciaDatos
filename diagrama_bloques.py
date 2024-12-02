import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()

nodes = [
    "Preparación\nde\ndatos",
    "Carga\nde\ndatos",
    "Selección\ninicial\nde\nvariables",
    "Variables\nfinancieras",
    "Indicadores\noperativos",
    "Métricas\nde\nsolvencia",
    "Otros\n(NAICS,\nEmpleados)",
    "Limpieza",
    "Imputación\nde\nvalores\nfaltantes",
    "Eliminación\nde\nvalores\nnulos",
    "Procesamiento\nNAICS",
    "Agrupación\nen\nsectores\namplios",
    "Import/\nExport",
    "Creación\nde\ncolumnas\nadicionales",
    "Eliminación\nde\ncolumnas\noriginales",
    "Transformación",
    "Métricas\ngeneradas",
    "Normalización",
    "Codificación"
]

edges = [
    ("Carga\nde\ndatos", "Preparación\nde\ndatos"),

    
    ("Preparación\nde\ndatos", "Transformación"),
    ("Preparación\nde\ndatos", "Codificación"),
    ("Preparación\nde\ndatos", "Normalización"),
    ("Preparación\nde\ndatos", "Limpieza"),
    ("Preparación\nde\ndatos", "Selección\ninicial\nde\nvariables"),

    ("Selección\ninicial\nde\nvariables", "Variables\nfinancieras"),
    ("Selección\ninicial\nde\nvariables", "Indicadores\noperativos"),
    ("Selección\ninicial\nde\nvariables", "Otros\n(NAICS,\nEmpleados)"),
    ("Selección\ninicial\nde\nvariables", "Eliminación\nde\ncolumnas\noriginales"),

    ("Creación\nde\ncolumnas\nadicionales", "Métricas\ngeneradas"),
    ("Transformación", "Creación\nde\ncolumnas\nadicionales"),
    ("Creación\nde\ncolumnas\nadicionales", "Procesamiento\nNAICS"),
    ("Creación\nde\ncolumnas\nadicionales", "Métricas\nde\nsolvencia"),

    ("Limpieza", "Imputación\nde\nvalores\nfaltantes"),
    ("Limpieza", "Eliminación\nde\nvalores\nnulos"),
    ("Otros\n(NAICS,\nEmpleados)", "Procesamiento\nNAICS"),

    ("Procesamiento\nNAICS", "Agrupación\nen\nsectores\namplios"),
    
    ("Creación\nde\ncolumnas\nadicionales", "Import/\nExport"),
    ("Eliminación\nde\ncolumnas\noriginales", "Import/\nExport"),
    
    
    
    
]

G.add_nodes_from(nodes)
G.add_edges_from(edges)

layer_assignment = {
    "Preparación\nde\ndatos": 1,
    "Carga\nde\ndatos": 0,
    "Selección\ninicial\nde\nvariables": 2,
    "Variables\nfinancieras": 3,
    "Indicadores\noperativos": 3,
    "Métricas\nde\nsolvencia": 4,
    "Otros\n(NAICS,\nEmpleados)": 3,
    "Limpieza": 2,
    "Imputación\nde\nvalores\nfaltantes": 3,
    "Eliminación\nde\nvalores\nnulos": 3,
    "Procesamiento\nNAICS": 4,
    "Agrupación\nen\nsectores\namplios": 5,
    "Import/\nExport": 4,
    "Creación\nde\ncolumnas\nadicionales": 3,
    "Eliminación\nde\ncolumnas\noriginales": 3,
    "Transformación": 2,
    "Métricas\ngeneradas": 4,
    "Normalización": 2,
    "Codificación": 2
}

nx.set_node_attributes(G, layer_assignment, "subset")

pos = nx.multipartite_layout(G, subset_key="subset")

# Dibujar el grafo
plt.figure(figsize=(14, 8))
nx.draw_networkx(
    G, pos, with_labels=True, node_size=3300, node_color="lightblue",
    font_size=8, arrowsize=15, node_shape="o",
)
plt.title("Preparación de Datos", fontsize=12)
plt.tight_layout()
plt.savefig("images/diagrama_bloques.png", format="png", dpi=600)