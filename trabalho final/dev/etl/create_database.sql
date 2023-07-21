CREATE TABLE food_composition (
  codigo varchar(30),
  nome varchar(1000),
  taxon varchar(500),
  energia varchar(15),
  umidade varchar(15),
  carboidrato_total varchar(15),
    proteina varchar(15),
    lipidios varchar(15),
  fibra_alimentar varchar(15),
  alcool varchar(15),
  cinzas varchar(15),
  colesterol varchar(15),
  acidos_graxos_saturados varchar(15),
  acidos_graxos_monoiinsaturados varchar(15),
  acidos_graxos_poliinsaturados varchar(15),
  acidos_graxos_trans varchar(15),
  calcio varchar(15),
  ferro varchar(15),
  sodio varchar(15),
  magnesio varchar(15),
  fosforo varchar(15),
  potassio varchar(15),
  zinco varchar(15),
  cobre varchar(15),
  selenio varchar(15),
  vitamina_a_re varchar(15),
  vitamina_a_rae varchar(15),
  vitamina_d varchar(15),
  vitamina_e varchar(15),
  tiamina varchar(15),
  riboflavina varchar(15),
  niacina varchar(15),
  vitamina_b6 varchar(15),
  vitamina_b12 varchar(15),
  vitamina_c varchar(15),
  equivalente_de_folato varchar(15),
  sal_de_adicao varchar(15),
  acucar_de_adicao varchar(15),
  foodon_id varchar(15)
)
create table food_composition_table(
  codigo varchar(5)
)

LOAD DATA LOCAL INFILE 'food_composition.csv'
INTO TABLE food_composition
COLUMNS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;