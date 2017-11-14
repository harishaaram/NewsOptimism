# coding: utf-8

#Scrapes the News article of given website and saves into a text document.


import newspaper
from newspaper import Article, news_pool
import sys
import os, errno
import time
import pandas as pd
import io


def newsscraping(url, media_name):

    ## ddmmyyyy format
    time_as_fname = time.strftime("%m%d%Y")
    # print(time_as_fname)
    #time_as_fname = 'chck3'
    backupfile= open('Backup/'+ media_name + '/' + time_as_fname, 'w')
    datasetfile = open('dataset/'+ media_name + '/'  + time_as_fname, 'w')

    i = -1

    news_content = newspaper.build(url,memoize_articles=False, language='en', fetch_images = False, number_threads = 1)# gets the source(an abstraction of online news) newspaper object
    # papers = [news_content]
    print(news_content.size())
    # news_pool.set(papers, threads_per_source=1)
    list_dict = [] # contains a list of dictionary with title, summary, text, keywords as keys
    for eachArticle in news_content.articles:#url links
        i = i +1#ith article link
        # if i is 30:
        #     break
        try :
            article = news_content.articles[i]

            article.download()#now download and parse each articles
            article.parse()

            article.nlp()

            backupfile.write("\n"+ "--------------------------------------------------------------" + "\n")

            datasetfile.write("\n" + "-Title-\n")
            datasetfile.write(article.title)
            datasetfile.write("\n" + "-URL-\n")
            datasetfile.write(eachArticle.url)
            datasetfile.write("\n"+"-SUMMARY ARTICLE-\n")#only summary of the article is written in the dataset directory
            datasetfile.write(article.summary)

            backupfile.write("\n" + "-Title- \n")
            backupfile.write(article.title)
            # backupfile.write("\n" + "-URL-\n")
            # backupfile.write(eachArticle.url)
            backupfile.write("\n" + "-Keywords-\n")
            backupfile.write(str(article.keywords))
            backupfile.write("\n"+"-SUMMARY ARTICLE-\n")
            backupfile.write(article.summary)
            backupfile.write("\n"+"-TEXT INSIDE ARTICLE-\n")
            backupfile.write(article.text)

            ----------------------------------------------------------

            #Mapping to Dictionary:
            dictionary={}
            dictionary['TITLE'] = article.title
            dictionary['URL'] = eachArticle.url
            dictionary['SUMMARY'] = article.summary
            dictionary['TEXT'] = article.text
            dictionary['KEYWORDS'] = str(article.keywords)
            list_dict.append(dictionary)

            #
            # time.sleep(0.1)
        except:
            pass
        # print(i)
    # print(list_dict)
    save_direct_to_csv(list_dict,media_name, time_as_fname)
    backupfile.close()
    datasetfile.close()
    #Printing Each corresponding article and its value

def save_direct_to_csv(data, media_name, foldername):
    df = pd.DataFrame(data)
    df = df.dropna(axis=0, how='any')

    buf = io.StringIO()
    df.to_csv(buf, index=False)  # convert DataFrame to csv
    # print(buf.getvalue())
    time_as_fname = str(media_name)+'.csv'
    path_name = make_folder(foldername) + '/'+ time_as_fname
    df.to_csv(path_name)
    # print(list_dict)

def make_folder(fold_name):
    path = '/home/harish/PycharmProjects/NewsOptimism/csvdataset/'+str(fold_name)
    try:
        os.makedirs(path)
        print('sdfdsf')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    return path
    

def main():
    os.getcwd()

    os.chdir('/home/harish/PycharmProjects/NewsOptimism/')

    url_list =["https://www.nytimes.com/", "https://www.foxnews.com/", "https://www.reuters.com/", "https://www.cnn.com/", "https://www.huffingtonpost.com/" ]
    # url_list = ["https://www.bbc.com/"]
    # url_list = ["https://www.cnbc.com/"]
    try:
        for url in url_list:
            media_name = url.split('.')[1]#makes subdir ie backup/foxnews
            newsscraping(url, media_name)
    except:
        pass


if __name__ == '__main__':
    main()



