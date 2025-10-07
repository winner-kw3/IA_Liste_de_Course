import pandas

data = {
    "Produit": ['Pomme', 'Fraise', 'Laitue', 'Carotte'],
    "Stock": [50, 87, 123, 90,],
    "Prix unitaire": [0.8, 3.5, 1.4, 1,]
}

mon_df = pandas.DataFrame(data)

# Le gérant souhaite consulter la liste des produits.
print(mon_df)

# Le gérant souhaite consulter les informations sur la laitue.
print(mon_df.loc[mon_df['Produit'] == 'Laitue'])

data_client = {
    "Produit": ['Pomme', 'Fraise', 'Carotte'],
    "Stock": [2, 5, 3]
}

# data_client["Prix Quantité"] = [
    # data["Prix unitaire"][0] * data_client["Stock"][0],
    # data["Prix unitaire"][1] * data_client["Stock"][1],
    # data["Prix unitaire"][3] * data_client["Stock"][2]
# ]



data_client["Prix Quantité"] = [
    data["Prix unitaire"][data["Produit"].index(produit)] * quantite
    for produit, quantite in zip(data_client["Produit"], data_client["Stock"])
]




ticket_df = pandas.DataFrame(data_client)

print(ticket_df)

copi_stock_df = mon_df.copy()
for produit, quantite in zip(ticket_df['Produit'], ticket_df['Stock']):
    copi_stock_df.loc[copi_stock_df['Produit'] == produit, 'Stock'] -= quantite

print("\nStock mis à jour après achat :")
print(copi_stock_df)

#Enregistrer le dataframe dans un fichier CSV
mon_df.to_csv('liste_course.csv', index=False)
