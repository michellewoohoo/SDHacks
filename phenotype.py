#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
        
