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


DB.city_information["Size"] = 20
DB.city_information["MinSizePerInhabitant"] = 100
DB.city_information["PersonsPerShop"] = 2000


#AI
rules = [
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
    "less than one food school per 500 students": True,
    "at least one food school per 500 students": False,
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
            print(fact, "then", " and ".join(premises))
            remembers(fact, True)

    return validate


def ai_start(city_facts):
    action_to_take = []
    for fact in city_facts:
        if justify(fact):
            action_to_take.append(fact)
    return action_to_take


def diagnose_current_city():
    pass


def main():
    pass


if __name__ == "__main__":
    main()
