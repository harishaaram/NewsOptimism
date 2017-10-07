# coding: utf-8

#Scrapes the News article of given website and saves into a text document.


import newspaper
from newspaper import Article, news_pool
import sys
import os
import time


def newsscraping(url, media_name):
    import os
    os.getcwd()

    os.chdir('/home/harish/PycharmProjects/NewsOptimism/')

    ## ddmmyyyy format
    filename = time.strftime("%d%m%Y")
    #filename = 'chck3'
    backupfile= open('Backup/'+ media_name + '/' + filename, 'w')
    datasetfile = open('dataset/'+ media_name + '/'  + filename, 'w')

    i = -1

    news_content = newspaper.build(url,memoize_articles=False, language='en', fetch_images = False, number_threads = 1)# gets the source(an abstraction of online news) newspaper object
    papers = [news_content]
    print(news_content.size())
    news_pool.set(papers, threads_per_source=1)
    for eachArticle in news_content.articles:#url links
        i = i +1
        try :
            article = news_content.articles[i]

            article.download()#now download and parse each articles
            article.parse()

            article.nlp()


            backupfile.write("\n"+ "--------------------------------------------------------------" + "\n")

            datasetfile.write("\n" + "----Title -> No. " + str(i) + "\n")
            datasetfile.write(article.title)

            # print(article.title)
            datasetfile.write("\n" + "----URL-> No. "+ str(i) + "\n")
            datasetfile.write(eachArticle.url) #only summary of the article is written in the dataset directory

            backupfile.write("\n" + "----Title -> No. " + str(i) + "\n")
            backupfile.write(article.title)
            backupfile.write("\n" + "----Keywords -> No. " + str(i) + "\n")
            backupfile.write(str(article.keywords))
            backupfile.write("\n"+"----SUMMARY ARTICLE---" + str(i)+ "\n")
            # backupfile.write(article.text)
            backupfile.write(article.summary)
            backupfile.write("\n"+"----TEXT INSIDE ARTICLE---"+ str(i) + "\n")
            backupfile.write(article.text)
            time.sleep(0.1)
        except:
            pass

    backupfile.close()
    datasetfile.close()
    #Printing Each corresponding article and its value


def main():
    os.chdir('/home/harish/PycharmProjects/NewsOptimism')  # change working dir
    
    url_list =["https://www.nytimes.com/", "https://www.foxnews.com/", "https://www.reuters.com/", "https://www.cnn.com/", "https://www.huffingtonpost.com/" ]
    # url_list = ["https://www.cnn.com/"]
    # url_list = ["http://www.bbc.com/"]
    try:
        for url in url_list:
            media_name = url.split('.')[1]#makes subdir ie backup/foxnews
            newsscraping(url, media_name)
    except:
        pass


if __name__ == '__main__':
    main()



