from django.contrib.postgres.search import SearchVector, SearchQuery, \
    SearchRank, SearchHeadline

from catalog.models import Plant


def q_search(query):
    vector = SearchVector('name', 'description')
    query = SearchQuery(query)

    return Plant.objects.annotate(headline=SearchHeadline('name', query, start_sel='<span style="background-color: yellow;"', stop_sel='</span>'))