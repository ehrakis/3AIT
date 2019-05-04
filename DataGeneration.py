"""
    Basic functions to generate data about the city

    TODO:
        * fill module's docstring

    Problem :
        Un habitant est identifié par: Nom,  Prénom, Rue, Code postal, Age, [Nombre d’habitation, Propriétaire ou  non],
        [Nombre  de  voiture, Propriétaire ou non], Homme, Femme, Seul, Père, Mère, [Enfant, Scolarisé ou Non].

        Un bâtiment est identifié par:Rue, Code postal, Nombre de pièce, Appartement, Maison, Bâtiment public, Superficie.

        Données complémentaires:Superficie de la commune, Superficie par habitant nécessaire pour vivre.
"""

inhabitants = [
    {
        "NationalID":   0,
        "FamilyName":   "",
        "FirstName":    "",
        "Address":      "",
        "PostalCode":   "",
        "Age":          "",
        "Habitation":   [],     # list of tuple containing a string equal to owner or renter and a building ID
        "Car":          [],
        "Sex":          "",
        "Status":       "",
        "Mother":       0,
        "Father":       0,
        "Children":     [],     # Need to handle the way the program see if a children is in school or not
        "Activity":     "",     # school or work
    }
]

buildings = [
    {
        "BuildingID":   0,
        "StreetNumber": 0,
        "StreetName":   "",
        "PostalCode":   "",
        "RoomNumber":   0,
        "Type":         "",     # Flat or house
        "PublicBuilding":   True,
        "Size":         0,      # size in m2
    }
]

city_information = {
    "Size":             0,      # size in km2
    "MinSizePerInhabitant": 0,  # size in m2
}

# 1 Definition of city information : city Size and minimum size per inhabitant

# 2 Create a function to generate a building

# 3 Create a function to generate a list building

# 4 Handling building consistency so 2 building don't have the same address
