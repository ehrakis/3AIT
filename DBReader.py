import DB


def get_inhabitant_number():
    return len(DB.inhabitants)


def get_inhabitant_presentation(inhabitant):
    building = next(building for building in DB.buildings if building["BuildingID"] == inhabitant["MainAddress"])
    return "Hi I'm {} {}. I live at {}. I'm {} years old and I have {} children. I'm a {}".format(
        inhabitant["FirstName"],
        inhabitant["FamilyName"],
        inhabitant["FamilyName"],
        get_building_address(building),
        inhabitant["Age"],
        len(inhabitant["Children"]),
        inhabitant["Activity"],
    )


def get_building_address(building):
    if building["Type"] == "Flat":
        inline_address = "{} {}, Flat {}".format(
            building["StreetNumber"],
            building["StreetName"],
            building["FlatNumber"],
        )
    else:
        inline_address = "{} {},".format(
            building["StreetNumber"],
            building["StreetName"]
        )
    return "{} {}".format(
        inline_address,
        building["City"]
    )


def get_inhabitant_by_id(national_id):
    try:
        inhabitant = next(inhabitant for inhabitant in DB.inhabitants if inhabitant["NationalID"] == national_id)
        return inhabitant
    except KeyError:
        print("Couldn't find inhabitant with NationalID:", national_id)
        return None


def get_building_by_id(building_id):
    try:
        building = next(building for building in DB.buildings if building["BuildingID"] == building_id)
        return building
    except KeyError:
        print("Couldn't find inhabitant with NationalID:", building_id)
        return None


def get_buildings_by_type(building_type):
    return [building for building in DB.buildings if building["Type"] == building_type]


def get_inhabitants_by_activity(activity):
    return [inhabitant for inhabitant in DB.inhabitants if inhabitant["Activity"] == activity]


def present_all_inhabitants():
    for inhabitant in DB.inhabitants:
        print(get_inhabitant_presentation(inhabitant))
