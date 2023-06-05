data_url = "https://query.wikidata.org/sparql"
query = """
        SELECT ?item ?itemLabel ?pubdate ?IMDb_ID WHERE {
          ?item wdt:P31 wd:Q11424.
          ?item wdt:P577 ?pubdate.
          ?item wdt:P345 ?IMDb_ID.
          FILTER((?pubdate > "2013-12-01T00:00:00Z"^^xsd:dateTime))
          SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
        }
        LIMIT 50 """