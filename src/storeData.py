import json

from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen


# Download the AFINN lexicon, unzip, and read the latest word list in AFINN-111.txt
url = urlopen('http://www2.compute.dtu.dk/~faan/data/AFINN.zip')
zipfile = ZipFile(BytesIO(url.read()))
afinn_file = zipfile.open('AFINN/AFINN-111.txt')

afinn = dict()

for line in afinn_file:
    parts = line.strip().split()
    if len(parts) == 2:
        afinn[parts[0].decode("utf-8")] = int(parts[1])


def afinn_sentiment(terms, afinn, data):
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



def json_storage(allWords):
    data = {}
    data['pos'] = []
    data['neg'] = []
    data['NetOutcome'], data['posCount'],data['negCount'] = afinn_sentiment(allWords, afinn, data)

    with open("d2.json", 'w') as out:
        json.dump(data, out)
