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

# url = "http://www.cnn.com/"
# url = "http://www.reuters.com/"
# url = "http://www.foxnews.com/"
url = "http://www.reuters.com/"

a = Article(url)


cnn_paper = newspaper.build(url)#gets the source(an abstraction of online news) newspaper object

article_links_list = list()
article_text_list = []
article_summary_list = []
article_nlp_list = []

f = open("newspaperReuters.txt", "w")
i = -1
for eachArticle in cnn_paper.articles:#url links
    i = i +1
    print(i)
    print("--------------------------------------------------------------")
    print(eachArticle.url)
    article = cnn_paper.articles[i]
    print("--------------------------------------------------------------")
    print(article)

    article_links_list.append(article)
    article.download()#now download and parse each articles
    article.parse()


    print("----TEXT INSIDE ARTICLE---")
    article_text_list.append(article.text)
    print(article.text)


    print("----NLP KEYWORDS---")
    article.nlp()
    article_nlp_list.append(article.keywords)
    print(article.keywords)


    print("----SUMMARY ARTICLE---")
    article_summary_list.append(article.summary)
    print(article.summary)


    f.write("--------------------------------------------------------------")
    f.write(eachArticle.url)
    # f.write(article.keywords)
    f.write(article.summary)
    f.write(article.text)

f.close()
#Printing Each corresponding article and its value


#
# #Reading and closing files;
# def saveFile(text, filename):
#     textOpen = open(filename, "w")
#     textOpen.write(text)
#     textOpen.close()
#
# def main():
#     url = "https://www.reuters.com/"
#     text = html2textLib(url)
#     saveFile(text, "htmltext.txt")
#
# if __name__ == '__main__':
#     main()


