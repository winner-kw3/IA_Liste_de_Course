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
    "Stock": [2, 5, 3],
    "Prix Quantité": [0.8*2, 3.5*2, 1*3]
}

ticket_df = pandas.DataFrame(data_client)

print(ticket_df)

copi_stock_df = mon_df.copy()
for produit, quantite in zip(ticket_df['Produit'], ticket_df['Stock']):
    copi_stock_df.loc[copi_stock_df['Produit'] == produit, 'Stock'] -= quantite

print("\nStock mis à jour après achat :")
print(copi_stock_df)

#Enregistrer le dataframe dans un fichier CSV
ticket_df.to_csv('liste_course.csv', index=False)