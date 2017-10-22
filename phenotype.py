#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests  # pip install requests

class Phenotype():
    def __init__(self, phenotype, text, score):
        self._phenotype = phenotype
        self._text = text
        self._score = score
    def getPhenotype(self):
        return self._phenotype
    def getText(self):
        return self._text
    def getScore(self):
        return self._score
        


def _main():
    token = 'GENOMELINKTEST'
    headers = {'Authorization': 'Bearer {}'.format(token)}

    phenotypes = ['carbohydrate-intake', 'protein-intake', 'vitamin-a', 'vitamin-b12', 'vitamin-d', 'vitamin-e', 
                'calcium', 'magnesium', 'iron', 'endurance-performance']
    population = 'european'


    for phenotype in phenotypes: 
        report_url = 'https://genomicexplorer.io/v1/reports/{}?population={}'.format(phenotype, population)
        response = requests.get(report_url, headers=headers)
        data = response.json()
        data_str = json.dumps(data)
        data_dict = json.loads(data_str)
        
        p = Phenotype(data_dict["phenotype"]["display_name"],data_dict["summary"]["text"],data_dict["summary"]["score"])
        print(p.getPhenotype())
        print(p.getText())
        print(p.getScore())

    # chrom = 'chr1'
    # start = '100000'
    # end = '100500'
    # sequence_url = 'https://genomicexplorer.io/v1/genomes/sequence/?region={}:{}-{}'.format(chrom, start, end)
    # response = requests.get(sequence_url, headers=headers)
    # data = response.json()
    # print(json.dumps(data))

if __name__ == '__main__':
    _main()
