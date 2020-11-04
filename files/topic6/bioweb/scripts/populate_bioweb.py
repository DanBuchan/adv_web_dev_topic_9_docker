import os
import sys
import django
import csv
from collections import defaultdict

# sys.path.append("/home/coder/project/topic2/bioweb")
sys.path.append("/home/dbuchan/Course_Dev/docker_containers/adv_web_dev_topic_3_docker/files/topic2/bioweb")
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'bioweb.settings')
django.setup()

from genedata.models import *

# data_file = '/home/coder/project/topic2/scripts/example_data_to_load.csv'
data_file = '/home/dbuchan/Course_Dev/docker_containers/adv_web_dev_topic_3_docker/files/topic2/example_data_to_load.csv'
genes = defaultdict(list)
sequencing = set()
ec = set()
products = defaultdict(dict)
attributes = defaultdict(dict)

with open(data_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = csv_reader.__next__()
    for row in csv_reader:
        product_pairs = row[9].split(';')
        attribute_pairs = row[10].split(';')
        for pair in product_pairs:
            tupple = pair.split(":")
            products[row[0]][tupple[0]] = tupple[1]
        for pair in attribute_pairs:
            tupple = pair.split(":")
            attributes[row[0]][tupple[0]] = tupple[1]
        ec.add(row[8])
        sequencing.add((row[4], row[5]))
        genes[row[0]] = row[1:4]+row[6:9]

GeneAttributeLink.objects.all().delete()
Gene.objects.all().delete()
EC.objects.all().delete()
Sequencing.objects.all().delete()
Attribute.objects.all().delete()
Product.objects.all().delete()

ec_rows = {}
sequencing_rows = {}
gene_rows = {}

for entry in ec:
    row = EC.objects.create(ec_name=entry)
    row.save()
    ec_rows[entry] = row
for seq_centre in sequencing:
    row = Sequencing.objects.create(sequencing_factory=seq_centre[0],
                                    factory_location=seq_centre[1])
    row.save()
    sequencing_rows[seq_centre[0]] = row
for gene_id, data in genes.items():
    row = Gene.objects.create(gene_id=gene_id, entity=data[0],
                              start=data[1], stop=data[2],
                              sense=data[3], start_codon=data[4],
                              sequencing=sequencing_rows['Sanger'],
                              ec=ec_rows[data[5]])
    row.save()
    gene_rows[gene_id] = row

for gene_id, data_dict in products.items():
    for key in data_dict.keys():
        row = Product.objects.create(type=key, product=data_dict[key],
                                     gene=gene_rows[gene_id])
        row.save()

for gene_id, data_dict in attributes.items():
    for key in data_dict.keys():
        row = Attribute.objects.create(key=key, value=data_dict[key])
        row.gene.add(gene_rows[gene_id])
        row.save()
