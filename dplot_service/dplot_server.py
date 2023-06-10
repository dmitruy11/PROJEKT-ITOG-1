from cProfile import label
import pandas as pd
from flask import Flask, request
import json
import pickle
import re
import matplotlib.pyplot as plt
import seaborn as sns


def get_standard_name(x):
    """Function for .apply():
       checks if x is a federal subject and standardizes its name, 
       otherwise returns None
    """
    for key, value in standard_names.items():
        x = re.sub('[\(].*?[\)]', '', x)  # del everything within ()
        if re.search(key, x.lower()):
            return value
    return None


app = Flask(__name__)
abels = pd.read_csv("dplot_service/data/labels.csv")
with open('dplot_service/data/standard_names.pkl', 'rb') as f:
        standard_names = pickle.load(f)

        
# Root endpoint
@app.route('/')
def index():
    msg = (
        "Distribution plot server<br>"
        "Use dplot_client.py to connect"
        )
    return msg


# Plotting a distribution
@app.route('/plot', methods=['POST'])
def plot_service():
    
    # Data preparation
    df = pd.DataFrame(json.loads(request.json))
    df['region'] = df['region'].apply(get_standard_name)
    df = df.dropna(subset='region').set_index('region').sort_index()
    df.iloc[:, 0] = pd.to_numeric(df.iloc[:, 0], errors='coerce')
    df['cluster'] = label
    
    # Making a figure
    fig = plt.figure(figsize=(6.5, 4)) 
    sns.boxplot(data=df, x=df.iloc[:, 0], y='cluster', orient='h')
    fig.suptitle("'" + str((df.columns)[0]) + "' distributions", fontsize=20)
    plt.savefig('./logs/distributions.png')
    plt.clf()
     
    return 'Ok'


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)

    ### docker build -t markov22/dplot_service .      docker build -t markov22/PROJEKT .     docker build -t /dplot_service .
    
    ### docker build -t dplot_server .       docker run  dplot_server       docker run hello-world   docker images