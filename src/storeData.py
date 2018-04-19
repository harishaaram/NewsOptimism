import json

from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen



def load_afinn_scores():
    """
        Download the AFINN lexicon, unzip, and read the latest word list in AFINN-111.txt

        Returns:
        afinn....dictionary with terms as key and scores as value
     """
    url = urlopen('http://www2.compute.dtu.dk/~faan/data/AFINN.zip')
    zipfile = ZipFile(BytesIO(url.read()))
    afinn_file = zipfile.open('AFINN/AFINN-111.txt')
    afinn = dict()
    for line in afinn_file:
        parts = line.strip().split()
        if len(parts) == 2:
            afinn[parts[0].decode("utf-8")] = int(parts[1])
    return afinn


def afinn_sentiment(terms, afinn, data):
    """
    Collect all the text articles from path file csv_link and returns the preprocessed dictionaried words
     Params:
       terms...list of words
       afinn...preexisting dictionary from load_afinn_scores()
       data...empty dictionary list
     Returns:
       total...int of total score of words
       total_pos...int of total score of only positive scored words
       total_neg...int of total score of only negative scored words
     """
    total = 0
    total_neg = 0
    total_pos = 0
    ls = []
    for t in terms:
        if t in afinn:
            ls.append(t)
            total += afinn[t]
            if afinn[t] > 0:
                data['pos'].append(t)
                total_pos += afinn[t]
            else:
                data['neg'].append(t)
                total_neg += afinn[t]
    return (total, total_pos, total_neg)



def json_storage(allWords, file_dir, date_val):
    """
    Stores all the positive and negative connotation words in the article along with the frequency count
    and the article date as JSON file
     Params:
       allWords...all the terms that appear in the all the articles of that news media
       file_dir...file path
       date_val...date of the article

     """

    afinn = load_afinn_scores()
    data = {}
    data['Date'] = date_val
    data['pos'] = []
    data['neg'] = []
    data['NetOutcome'], data['posCount'],data['negCount'] = afinn_sentiment(allWords, afinn, data)

    with open(file_dir, 'w') as out:
        json.dump(data, out)
