# coding: utf-8

#Scrapes the front web page of given website and saves into a text document.

#Check Google Notes:
import html2text
import requests
#Make the proxy settings, if your access is through a proxy server
# import lassie
# import pprint
# url = "https://www.reuters.com/"
# pprint.pprint(lassie.fetch(url))

import newspaper
from newspaper import Article
import os
import time

# t = os.path.join('/home/harish/PycharmProjects/NewsOptimism/Backup', time.strftime("%d%m%Y"))
# os.makedirs(t)
# os.path.exists('/home/harish/PycharmProjects/NewsOptimism/Backup')

## ddmmyyyy format
print (time.strftime("%d%m%Y"))

# def create_filename(url):
#     media_name = url.split('.')[1]
#     t = os.path.join('/home/harish/PycharmProjects/NewsOptimism/Backup', time.strftime("%d%m%Y"))
#     bolean = os.path.exists(t)
#     if bolean == False:
#         os.makedirs(t)
#         return

def newsscraping(url, media_name):
    import os
    os.getcwd()

    os.chdir('/home/harish/PycharmProjects/NewsOptimism/')
    filename = time.strftime("%d%m%Y")

    backupfile= open('Backup/'+ media_name + '/' + filename, 'w')
    datasetfile = open('dataset/'+ media_name + '/'  + filename, 'w')

    i = -1

    cnn_paper = newspaper.build(url)  # gets the source(an abstraction of online news) newspaper object
    for eachArticle in cnn_paper.articles:#url links
        i = i +1
        print(i)
        print("--------------------------------------------------------------")
        print(eachArticle.url)
        article = cnn_paper.articles[i]
        print("--------------------------------------------------------------")
        print(article)

        article.download()#now download and parse each articles
        article.parse()


        print("----TEXT INSIDE ARTICLE---")
        print(article.text)


        print("----NLP KEYWORDS---")
        article.nlp()
        print(article.keywords)


        print("----SUMMARY ARTICLE---")
        print(article.summary)


        backupfile.write("\n"+ "--------------------------------------------------------------" + "\n")
        backupfile.write(str(article.keywords))

        backupfile.write("\n"+"----SUMMARY ARTICLE---" + "\n")
        datasetfile.write("\n" + "----SUMMARY ARTICLE-> No. " + str(i) + "\n")
        datasetfile.write(article.summary) #only summary of the article is written in the dataset directory
        backupfile.write(article.summary)
        backupfile.write("\n"+"----TEXT INSIDE ARTICLE---" + "\n")
        backupfile.write(article.text)

    backupfile.close()
    datasetfile.close()
    #Printing Each corresponding article and its value


def main():
    os.chdir('/home/harish/PycharmProjects/NewsOptimism')  # change working dir
    
    url_list =[ "http://www.nytimes.com/", "http://www.foxnews.com/", "http://www.reuters.com/", "http://www.cnn.com/", "http://www.huffingtonpost.com/" ]
    # u = ["http://www.ndtv.com/"]
    for url in url_list:
        media_name = url.split('.')[1]#makes subdir ie backup/foxnews
        
        newsscraping(url, media_name)


if __name__ == '__main__':
    main()


