import pandas as pd
import matplotlib.pylab as plt


def get_data(filename):
    """Retrieves the filement
    """
    return pd.read_excel(
        'reporter/data/series-1800-2015_simplified.xlsx').T

def clean_data(data):
    serie = data.loc['Série']
    serie = serie.fillna('')
    data.columns = serie.apply(
        lambda val : val
        .replace('.', '')
        .replace(' ', '-')
        .replace('(', '-')
        .replace(')', '-')
        .replace("'", '-')
        .replace(",", '-')
        .lower()
        )
    data = data.drop(['Série'])
    data.index = data.index.astype(int)

def plot1(data):
    fig, ax = plt.subplots()
    ax.scatter(
        x=data['produit-intérieur-brut--milliards-d-€-'],
        y=data['indice-des-prix-à-la-consommation--€--base-2000-'],
        s=data['population--y-compris-dom---milliers-'].fillna(0)/1000,
        alpha=0.4)

    fig.savefig('graph1.png', dpi=300)

def plot2(data):
    fig, ax = plt.subplots()
    ax.scatter(
        x=data['produit-intérieur-brut--milliards-d-€-'],
        y=data['produit-intérieur-brut--milliards-de-£-'],
        alpha=0.4)

    fig.savefig('graph2.png', dpi=300)
