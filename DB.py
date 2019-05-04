inhabitants = [
    {
        "NationalID":   0,
        "FamilyName":   "",
        "FirstName":    "",
        "MainAddress":  0,
        "Age":          "",
        "Habitation":   {
            "owner": [],
            "renter": []
        },
        "Car":          [],
        "Sex":          "",
        "Status":       "",
        "Mother":       0,
        "Father":       0,
        "Children":     [],
        "Activity":     "",
    }
]

buildings = [
    {
        "BuildingID":   0,
        "StreetNumber": 0,
        "FlatNumber":   0,
        "StreetName":   "",
        "PostalCode":   "",
        "RoomNumber":   0,
        "Type":         "",     # Flat, house, shop, town hall
        "PublicBuilding":   True,
        "Size":         0,      # size in m2
        "City":         "",
    }
]


city_information = {
    "Size":             0,      # size in km2
    "MinSizePerInhabitant": 0,  # size in m2
}