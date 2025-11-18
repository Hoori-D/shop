from catalog.models import Plant


def q_search(query):
    return Plant.objects.filter(name__search=query)