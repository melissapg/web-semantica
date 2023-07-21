import rdflib

g = rdflib.Graph()
g.parse(location='output.ttl', format="turtle")


alimentos = g.query("""
PREFIX rdfs: <https://www.w3.org/2000/01/rdf-schema#>
PREFIX wbt: <https://wikifcd.wikibase.cloud/wiki/Property:>

select ?alimento ?carboidrato
where {
    ?s wbt:P10 ?carboidrato .
    ?s rdfs:label ?alimento
}
""")


max = ['', 0]
for alimento in alimentos:
    valor = float(str(alimento.carboidrato).replace(',','.')) if alimento.carboidrato != 'NA' else 0
    nome = str(alimento.alimento)
    if valor > max[1]:
        max[0] = nome
        max[1] = valor