
import json
import requests  # pip install requests
import genomelink
from phenotype import Phenotype
from flask import Flask,render_template,url_for,request,redirect,session

app=Flask(__name__)

phenotypeDict = {}

@app.route('/')
def index():
    retrieveData();
    authorize_url = genomelink.OAuth.authorize_url(scope=['report:eye-color report:beard-thickness report:morning-person'])

    # Fetching a protected resource using an OAuth2 token if exists.
    reports = []
    if session.get('oauth_token'):
        for name in ['eye-color', 'beard-thickness', 'morning-person']:
            reports.append(genomelink.Report.fetch(name=name, population='european', token=session['oauth_token']))

    return render_template('home.html', authorize_url=authorize_url, reports=reports)

@app.route('/callback')
def callback():
    # The user has been redirected back from the provider to your registered
    # callback URL. With this redirection comes an authorization code included
    # in the request URL. We will use that to obtain an access token.
    token = genomelink.OAuth.token(request_url=request.url)

    # At this point you can fetch protected resources but lets save
    # the token and show how this is done from a persisted token in index page.
    session['oauth_token'] = token
    return redirect(url_for('index'))

def retrieveData():
    '''
        Retrieves data from API and puts them into a dictionary. A phenotype value is paired with a list of its name description and score key
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
        phenotypeDict[p._phenotype] = [p._text, p._score]

if __name__ == '__main__':
    # This allows us to use a plain HTTP callback.
    import os
    os.environ['DEBUG'] = "1"
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    # Run local server on port 5000.
    app.secret_key = os.urandom(24)
    app.run(debug=True)

