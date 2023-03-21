import csv

class Tienda:
    def __init__(self):
        self.inventario = {
            "001": {"nombre": "manzana", "precio": 0.5, "cantidad": 10},
            "002": {"nombre": "banana", "precio": 0.3, "cantidad": 15},
            "003": {"nombre": "naranja", "precio": 0.4, "cantidad": 20},
            "004": {"nombre": "pera", "precio": 0.6, "cantidad": 12}
        }

    def actualizarTienda(self, archivo_csv: str) -> bool:
        with open(archivo_csv, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader) # Salta la primera fila que contiene los encabezados del archivo CSV
            for row in reader:
                sku, nombre, precio, cantidad = row
                if sku in self.inventario:
                    self.inventario[sku]["nombre"] = nombre
                    self.inventario[sku]["precio"] = float(precio)
                    self.inventario[sku]["cantidad"] = int(cantidad)
                else:
                    self.inventario[sku] = {"nombre": nombre, "precio": float(precio), "cantidad": int(cantidad)}
        return True
