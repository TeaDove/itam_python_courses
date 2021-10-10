def greeting(a: str):
    name, surname = a.split()
    return "Доброго времени суток, {} \"Человек\" {}!".format(name, surname)
