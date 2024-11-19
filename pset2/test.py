import numpy as np
import csv

def p_gene_and_trait(gene, bats_list):
    norm = len(bats_list)
    count = 0
    for bat in bats_list:
        if bat[gene] == 'True' and bat['T'] == 'True':
            count += 1
    return count / norm

def p_gene(gene, bats_list):
    norm = len(bats_list)
    count = 0
    for bat in bats_list:
        if bat[gene] == 'True':
            count += 1
    return count / norm

def p_trait(bats_list):
    norm = len(bats_list)
    count = 0
    for bat in bats_list:
        if bat['T'] == 'True':
            count += 1
    return count / norm

def test():
    
    # Reading in bats.csv
    reader = csv.DictReader(open('bats.csv'))
    bats = list(reader)
    
    genes = ['G1', 'G2', 'G3', 'G4', 'G5']
    
    for gene in genes:
        p_trait_given_gene = p_gene_and_trait(gene, bats) / p_trait(bats)
        print(f'P({gene} | T): {p_trait_given_gene}')
        print(f'P({gene}): {p_gene(gene, bats)} \n')
    
test()
    
    