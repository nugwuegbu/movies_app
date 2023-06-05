"""
This a Sparql utiltiy for running and filtering Sparql queries
download data from queries
store data to database
"""
from SPARQLWrapper import SPARQLWrapper,JSON
from main.models import Movies
from celery import shared_task

class SparqlUtil:

    """Global variables"""
    data_url = None
    query = None
    user = None


    def query_raw_data(self):
        sparql = SPARQLWrapper(self.data_url)
        sparql.setQuery(self.query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        return results
    # @shared_task
    def data_result(self):
        output = []
        inner_out = {}

        # movie_data = Movies()
        for key, value in self.query_raw_data().items():
            for k, v in value.items():
                if k == 'bindings':
                    for data in v:
                        movie_data = Movies()
                        for x, y in data.items():
                            if x == "IMDb_ID":
                                movie_data.imdb_id = y['value']
                                inner_out["imdb_id"] = y['value']
                            elif x == "pubdate":
                                inner_out["published_date"] = y['value']
                                movie_data.published_date = y['value']
                            elif x == "itemLabel":
                                inner_out["title"] = y['value']
                                movie_data.title = y['value']

                            else:
                                pass
                        output.append(inner_out)
                        movie_data.user = self.user
                        movie_data.save()
        return output