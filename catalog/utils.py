from django.contrib.postgres.search import SearchVector, SearchQuery, \
    SearchRank

from catalog.models import Plant


def q_search(query):
    vector = SearchVector('name', 'description')
    query = SearchQuery(query)

    return Plant.objects.annotate(rank=SearchRank(vector, query)).order_by('-rank')