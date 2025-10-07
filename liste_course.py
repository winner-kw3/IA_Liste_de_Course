import pandas

data = {
    "Produit": ['Pomme', 'Fraise', 'Laitue', 'Carotte'],
    "Stock": [50, 87, 123, 90,],
    "Prix unitaire": [0.8, 3.5, 1.4, 1,]
}

mon_df = pandas.DataFrame(data)

print(mon_df)