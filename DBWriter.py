def add_public_bulding(bulding_type):
    pass


def create_person(activity, Sex=None):
    """
    3 possible activities : Student, Worker, Retired
    :param activity:
    :return:
    """
    return {}


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
    child = create_person("Student")

    # Child parent's
    mother = create_person("Worker", "Women")
    father = create_person("Worker", "Men")
    have_child(mother, father, child)

    # Child grand parent's
    mother_father = create_person("Retired", "Men")
    mother_mother = create_person("Retired", "Women")
    have_child(mother_mother, mother_father, mother)

    father_father = create_person("Retired", "Men")
    father_mother = create_person("Retired", "Women")
    have_child(father_mother, father_father, father)


def have_child(mother, father, child):
    """
    define the family bond between parent and child
    """
    mother["Children"].append(child["NationalID"])
    father["Children"].append(child["NationalID"])
    child["Mother"] = mother["NationalID"]
    child["Father"] = father["NationalID"]



