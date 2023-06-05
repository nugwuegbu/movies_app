from SPARQLWrapper import SPARQLWrapper,JSON

sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
sparql.setQuery("""SELECT ?item ?itemLabel ?pubdate ?IMDb_ID WHERE {
  ?item wdt:P31 wd:Q11424.
  ?item wdt:P577 ?pubdate.
  ?item wdt:P345 ?IMDb_ID.
  FILTER((?pubdate > "2013-12-31T00:00:00Z"^^xsd:dateTime))
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
} OFFSET 20 LIMIT 1 """)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()


if __name__ == '__main__':
    # print(type(results))
    output = []
    inner_out = {}
    for key, value in results.items():
        for k,v in value.items():
            if k == 'bindings':
                for data in v:
                    for x,y in data.items():
                        print("--")
                        print(x)
                        if x == "IMDb_ID":
                            inner_out["imb_id"] = y['value']
                        elif x == "pubdate":
                            inner_out["published_date"] = y['value']
                        else:
                            inner_out["title"] = y['value']
                    output.append(inner_out)
    # print(output)
    print("--end--")
#Movies released after 2013
