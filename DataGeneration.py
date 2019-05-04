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

import utils
import DB
import DBReader
import DBWriter
import math

#AI
rules = [
    (("less than one school per 500 students",), "Add school"),
    (("at least one school per 500 students",), "Enough school"),
    (("less than one food shop per 2000 inhabitants",), "Add food shop"),
    (("at least one food shop per 2000 inhabitants",), "Enough food shop"),
    (("less than one police station per 20000 inhabitants",), "Add police station"),
    (("at least one police station per 20000 inhabitants",), "Enough police station"),
    (("less than one fire station per 20000 inhabitants",), "Add fire station"),
    (("at least one fire station per 20000 inhabitants",), "Enough fire station"),
    (("less than one medical office per 500 inhabitants",), "Add medical office"),
    (("at least one medical office per 500 inhabitants",), "Enough medical office"),
    (("less than one drug store per 1000 inhabitants",), "Add drug store"),
    (("at least one drug store per 1000 inhabitants",), "Enough drug store"),
    (("Enough food shop",
      "Enough police station",
      "Enough fire station",
      "Enough medical office",
      "Enough drug store",
      ), "Enough public places"),
    (("at least 75% of the city is filled",), "Enough inhabitants"),
    (("less than 75% of the city is filled",
      "Enough public places"), "Add inhabitants"),
    (("Enough inhabitants",
      "Enough public places"), "Good city"),
]

memory = {}

initial_facts = {
    "less than one school per 500 students": True,
    "at least one school per 500 students": False,
    "less than one food shop per 2000 inhabitants": True,
    "at least one food shop per 2000 inhabitants": False,
    "less than one police station per 20000 inhabitants": True,
    "at least one police station per 20000 inhabitants": False,
    "less than one fire station per 20000 inhabitants": True,
    "at least one fire station per 20000 inhabitants": False,
    "less than one medical office per 500 inhabitants": True,
    "at least one medical office per 500 inhabitants": False,
    "less than one drug store per 1000 inhabitants": True,
    "at least one drug store per 1000 inhabitants": False,
    "less than 75% of the city is filled": True,
    "at least 75% of the city is filled": False,
}


def in_then(fact):
    results = []
    for premises, conclusion in rules:
        if fact == conclusion:
            results.append((premises, conclusion))
    return results


def knows(fact):
    result = None
    if initial_facts:
        result = initial_facts.get(fact)
    if not result and memory:
        result = memory.get(fact)
    return result


def remembers(fact, result):
    global memory
    memory[fact] = result


def justify(fact):
    result = knows(fact)

    if result:
        return result

    rules = in_then(fact)

    if not rules:
        remembers(fact, None)
        return None

    for premises, conclusion in rules:
        validate = True
        for premise in premises:
            if not justify(premise):
                validate = False
                break

        if validate:
            remembers(fact, True)

    return validate


def ai_start(city_facts):
    global memory
    memory = {}
    action_to_take = []
    for fact in city_facts:
        if justify(fact):
            action_to_take.append(fact)
    return action_to_take
#en AI


def diagnose_current_city():
    inhabitants_number = DBReader.get_inhabitant_number()
    student_number = DBReader.get_inhabitants_number_by_activity("Student")
    school_number = DBReader.get_buildings_number_by_type("School")
    fire_station_number = DBReader.get_buildings_number_by_type("FireStation")
    police_station_number = DBReader.get_buildings_number_by_type("PoliceStation")
    food_shop_number = DBReader.get_buildings_number_by_type("FoodShop")
    medical_office_number = DBReader.get_buildings_number_by_type("MedicalOffice")
    drug_store_number = DBReader.get_buildings_number_by_type("DrugStore")
    percentage_covered = DBReader.get_percentage_covered()

    global initial_facts

    initial_facts["less than one school per 500 students"] = True if math.ceil(student_number / 500) > school_number else False
    initial_facts["at least one school per 500 students"] = not initial_facts["less than one school per 500 students"]

    initial_facts["less than one food shop per 2000 inhabitants"] = True if math.ceil(inhabitants_number/2000) > food_shop_number else False
    initial_facts["at least one food shop per 2000 inhabitants"] = not initial_facts["less than one food shop per 2000 inhabitants"]

    initial_facts["less than one police station per 20000 inhabitants"] = True if math.ceil(inhabitants_number/20000) > police_station_number else False
    initial_facts["at least one police station per 20000 inhabitants"] = not initial_facts["less than one police station per 20000 inhabitants"]

    initial_facts["less than one fire station per 20000 inhabitants"] = True if math.ceil(inhabitants_number/20000) > fire_station_number else False
    initial_facts["at least one fire station per 20000 inhabitants"] = not initial_facts["less than one fire station per 20000 inhabitants"]

    initial_facts["less than one medical office per 500 inhabitants"] = True if math.ceil(inhabitants_number/500) > medical_office_number else False
    initial_facts["at least one medical office per 500 inhabitants"] = not initial_facts["less than one medical office per 500 inhabitants"]

    initial_facts["less than one drug store per 1000 inhabitants"] = True if math.ceil(inhabitants_number/1000) > drug_store_number else False
    initial_facts["at least one drug store per 1000 inhabitants"] = not initial_facts["less than one drug store per 1000 inhabitants"]

    initial_facts["less than 75% of the city is filled"] = True if percentage_covered < 75 else False
    initial_facts["at least 75% of the city is filled"] = not initial_facts["less than 75% of the city is filled"]


def act(action_to_take):
    for action in action_to_take:
        if action == "Add food shop":
            DBWriter.add_public_bulding("FoodShop", 500)

        if action == "Add school":
            DBWriter.add_public_bulding("School", 1000)

        elif action == "Add police station":
            DBWriter.add_public_bulding("PoliceStation", 500)

        elif action == "Add fire station":
            DBWriter.add_public_bulding("FireStation", 500)
        elif action == "Add medical office":
            DBWriter.add_public_bulding("MedicalOffice", 200)

        elif action == "Add drug store":
            DBWriter.add_public_bulding("DrugStore", 200)

        elif action == "Add inhabitants":
            DBWriter.create_family()


def main():
    is_good_city = False
    while not is_good_city:
        diagnose_current_city()
        fact_to_test = [
            "Add school",
            "Add food shop",
            "Add police station",
            "Add fire station",
            "Add medical office",
            "Add drug store",
            "Add inhabitants",
            "Good city"
        ]
        action_to_take = ai_start(fact_to_test)
        if "Good city" in action_to_take:
            is_good_city = True
        else:
            act(action_to_take)

        print(round(DBReader.get_percentage_covered() / 75 * 100), "%", sep="")

if __name__ == "__main__":
    main()
    print(
        "".join(["Town must have :\n",
                 "\t- {} inhabitants,\n",
                 "\t- {} food shop,\n",
                 "\t- {} police station,\n",
                 "\t- {} fire station,\n",
                 "\t- {} school,\n",
                 "\t- {} medical office,\n",
                 "\t- {} drug store,\n"]).format(
            DBReader.get_inhabitant_number(),
            DBReader.get_buildings_number_by_type("FoodShop"),
            DBReader.get_buildings_number_by_type("PoliceStation"),
            DBReader.get_buildings_number_by_type("FireStation"),
            DBReader.get_buildings_number_by_type("School"),
            DBReader.get_buildings_number_by_type("MedicalOffice"),
            DBReader.get_buildings_number_by_type("DrugStore"),
        )
        )

