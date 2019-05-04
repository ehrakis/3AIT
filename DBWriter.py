import DBReader
import DATA
import DB
from random import randint


def add_public_bulding(bulding_type, size):
    building = {
        "BuildingID": DBReader.get_possible_building_id(),
        "StreetNumber": 0,
        "FlatNumber": 0,
        "StreetName": "",
        "PostalCode": "",
        "RoomNumber": 0,
        "Type": bulding_type,  # Flat, house, shop, town hall
        "PublicBuilding": True,
        "Size": size,  # size in m2
        "City": DB.city_information["CityName"],
    }
    DB.buildings.append(building)


def create_home():
    building = {
        "BuildingID": DBReader.get_possible_building_id(),
        "StreetNumber": 0,
        "FlatNumber": 0,
        "StreetName": "",
        "PostalCode": "",
        "RoomNumber": 0,
        "Type": "House",  # Flat, house, shop, town hall
        "PublicBuilding": False,
        "Size": DB.city_information["MinSizePerInhabitant"]*3,  # size in m2
        "City": DB.city_information["CityName"],
    }
    DB.buildings.append(building)
    return building


def create_person(activity, age, sex=None, family_name=None, building=None):
    """
    3 possible activities : Student, Worker, Retired
    """
    sex = ["Male", "Female"][randint(0, 1)] if not sex else sex
    building = create_home() if not building else DBReader.get_building_by_id(building)
    inhabitant = {
        "NationalID": DBReader.get_possible_id(),
        "FamilyName": family_name if family_name else DATA.FamilyName[randint(0, len(DATA.FamilyName)-1)],
        "FirstName": DATA.MenFirstName[randint(0, len(DATA.MenFirstName)-1)] if sex == "Male" else DATA.WomenFirstName[randint(0, len(DATA.WomenFirstName)-1)],
        "MainAddress": building["BuildingID"],
        "Age": age,
        "Habitation": {
            "owner": [building["BuildingID"]],
            "renter": []
        },
        "Car": [],
        "Sex": sex,
        "Status": "Single" if age < 25 else "Married",
        "Mother": 0,
        "Father": 0,
        "Children": [],
        "Activity": activity
    }

    DB.inhabitants.append(inhabitant)

    return inhabitant


def create_family():
    """
    a family is composed of :
        - 2 grand father
        - 2 grand mother
        - 1 father
        - 1 mother
        - 1 child (randomly choose if he is a boy or a girl)
    """
    # Child
    child_age = randint(0, 22)
    child = create_person("Student", child_age)

    # Child parent's
    father = create_person("Worker",
                           child_age + randint(20, 35),
                           sex="Man",
                           family_name=child["FamilyName"],
                           building=child["MainAddress"])

    mother = create_person("Worker",
                           child_age + randint(20, 35),
                           sex="Woman",
                           family_name=child["FamilyName"],
                           building=child["MainAddress"])
    have_child(mother, father, child)

    # Child grand parent's
    mother_father = create_person("Retired",
                                  mother["Age"] +
                                  randint(20, 35),
                                  sex="Man")
    mother_mother = create_person("Retired",
                                  mother["Age"] +
                                  randint(20, 35),
                                  sex="Woman",
                                  family_name=mother_father["FamilyName"],
                                  building=mother_father["MainAddress"])
    have_child(mother_mother, mother_father, mother)

    father_father = create_person("Retired",
                                  father["Age"] +
                                  randint(20, 35),
                                  sex="Man",
                                  family_name=child["FamilyName"])
    father_mother = create_person("Retired",
                                  father["Age"] +
                                  randint(20, 35),
                                  sex="Woman",
                                  family_name=child["FamilyName"],
                                  building=father_father["MainAddress"])

    have_child(father_mother, father_father, father)


def have_child(mother, father, child):
    """
    define the family bond between parent and child
    """
    mother["Children"].append(child["NationalID"])
    father["Children"].append(child["NationalID"])
    child["Mother"] = mother["NationalID"]
    child["Father"] = father["NationalID"]



