import nltk #imports the nltk module
nltk.download("words") # downloads English words
nltk.download("stopwords") # downloads English stopwords
import pandas as pd

import re
import enchant
d = enchant.Dict("en_US")

nltk.download("punkt") # downloads punkt tokenizer models
nltk.download('averaged_perceptron_tagger') # downloads the algorithm for predicting the part of speech information
nltk.download('maxent_ne_chunker') # downloads the maximum entropy chunker that has been trained on the ACE 2004 corpus https://catalog.ldc.upenn.edu/LDC2005T09



def collectWords_perNewsMedia(csv_link):
    """
    Collect all the text articles from path file csv_link and returns the preprocessed dictionaried words
     Params:
       csv_link...link to the .csv file
     Returns:
       Words_perday...list of words after preprocessing
     """
    df = pd.read_csv(csv_link)
    df = df.dropna(how='any')

    Words_perday = []
    stopwords = set(nltk.corpus.stopwords.words("english"))

    for i in range(df.shape[0]):
        data = str(df['TEXT'].iloc[i])
        data = data.replace("\n", "")
        words_string = nltk.word_tokenize(data)
        Words_perday.extend(
            [word.lower() for word in words_string if (
            not re.match('.*\d+', word) and d.check(word) == True and (len(word) > 2) and (
            word.lower() not in stopwords))])

    return Words_perday

