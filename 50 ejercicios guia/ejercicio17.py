
compras = ["pan", "leche", "huevos", "queso", "yogur"]
print("Lista inicial:", compras)


compras = [item for item in compras if item != "huevos"]
print("\nDespués de eliminar huevos (filtrando):", compras)


compras = compras + ["mantequilla"]
print("\nDespués de añadir mantequilla (concatenación):", compras)