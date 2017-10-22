
import json
import requests  # pip install requests
from flask import Flask,render_template,url_for,request,redirect

app=Flask(__name__)

phenotypeDict = {}

def retrieveData():
    '''
        Retrieves data in API and puts them into a dictionary. A phenotype value is paired with a list of its name description and score key
    '''
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
        phenotypeDict[p.phenotype] = [p.text, p.score]



if __name__ == '__main__':
    retrieveData()

