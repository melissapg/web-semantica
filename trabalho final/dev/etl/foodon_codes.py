import rdflib
import pandas as pd


g = rdflib.Graph()
g.parse(location='bagunça/foodon.owl')

foodon_query = """
PREFIX foodon: <http://purl.obolibrary.org/obo/FOODON_>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX gene: <http://www.geneontology.org/formats/oboInOwl#>

select ?s ?narrowSynonym (strafter(str(?s), "_") as ?cod)
where {
  ?s gene:hasNarrowSynonym ?narrowSynonym .
	filter(contains(str(?s), 'FOODON_')) .
}
"""

foodon_codes = g.query(foodon_query)

results_list = []
for codes in foodon_codes:
    results_list.append((str(codes.s), str(codes.narrowSynonym), str(codes.cod)))

df = pd.DataFrame(results_list, columns=["Code", "NarrowSynonym", "Cod"])

df.to_csv("data/csv/foodon_codes.csv", index=False, encoding='utf-8')