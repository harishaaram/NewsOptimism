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
import sys
import os
import time


def newsscraping(url, media_name):
    import os
    os.getcwd()

    os.chdir('/home/harish/PycharmProjects/NewsOptimism/')

    ## ddmmyyyy format
    filename = time.strftime("%d%m%Y")

    backupfile= open('Backup/'+ media_name + '/' + filename, 'w')
    datasetfile = open('dataset/'+ media_name + '/'  + filename, 'w')

    i = -1

    news_content = newspaper.build(url)  # gets the source(an abstraction of online news) newspaper object
    for eachArticle in news_content.articles:#url links
        i = i +1
        try :
            article = news_content.articles[i]

            article.download()#now download and parse each articles
            article.parse()

            article.nlp()


            backupfile.write("\n"+ "--------------------------------------------------------------" + "\n")
            backupfile.write(str(article.keywords))


            datasetfile.write("\n" + "----SUMMARY ARTICLE-> No. " + str(i) + "\n")
            datasetfile.write(article.summary) #only summary of the article is written in the dataset directory


            backupfile.write("\n"+"----SUMMARY ARTICLE---" + "\n")
            backupfile.write(article.summary)
            backupfile.write("\n"+"----TEXT INSIDE ARTICLE---" + "\n")
            backupfile.write(article.text)
            time.sleep(2)
        except:
            pass

    backupfile.close()
    datasetfile.close()
    #Printing Each corresponding article and its value


def main():
    os.chdir('/home/harish/PycharmProjects/NewsOptimism')  # change working dir
    
    url_list =[ "http://www.nytimes.com/", "http://www.foxnews.com/", "http://www.reuters.com/", "http://www.cnn.com/", "http://www.huffingtonpost.com/" ]
    # u = ["http://www.ndtv.com/"]
    try:
        for url in url_list:
            media_name = url.split('.')[1]#makes subdir ie backup/foxnews
            newsscraping(url, media_name)
    except:
        pass



if __name__ == '__main__':
    main()


