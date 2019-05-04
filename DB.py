"""
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
"""
inhabitants = []

buildings = []


city_information = {
    "CityName": "Paris",
    "Size":             20,      # size in km2
    "MinSizePerInhabitant": 10000,  # size in m2
}