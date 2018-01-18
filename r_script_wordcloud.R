#Install and load library
# update.packages(ask = FALSE)
# install.packages("NLP", dependencies=TRUE)
# install.packages("slam", dependencies=TRUE)
# install.packages("tm", dependencies=TRUE) # for text mining
# install.package("SnowballC", dependencies=TRUE) # for text stemming
# install.packages("wordcloud", dependencies=TRUE)# word-cloud generator
# install.packages("RColorBrewer", dependencies=TRUE) # color palettes
# install.packages('lda', dependencies=TRUE)
# install.packages('modeltools', dependencies=TRUE)
# install.packages('stats4', dependencies=TRUE)
# # install.packages('methods', dependencies=TRUE)
# install.packages('toppicmodels', dependencies=TRUE)
# install.packages('ggplot2', dependencies = TRUE)
# install.packages("NbClust", dependencies = TRUE)
# install.packages("factoextra", dependencies = TRUE)

cat('\014')
library(NLP)
library(tm)
library(SnowballC)
library(RColorBrewer)
library(wordcloud)
library(ggplot2)
library(factoextra)
# library(cluster)
library(NbClust)
# library(fpc)

#Data Loading:
rm(list = ls())
setwd("/home/harish/PycharmProjects/NewsOptimism/")

#-----------------------------REUTERS---------------------

reu_text<-c("/home/harish/PycharmProjects/NewsOptimism/sample/data/reu/20102017/")
summary(reu_text)

#corpus
reuters_corpus <- Corpus(DirSource(reu_text, recursive=TRUE),readerControl = list(reader=readPlain))

# data preprocessing
#Cleaning and Preprocessing#
reuters_corpus<-tm_map(reuters_corpus,removePunctuation);
reuters_corpus<-tm_map(reuters_corpus,removeNumbers); 

reuters_corpus<-tm_map(reuters_corpus,removeWords,stopwords("english")); 

reuters_corpus<-tm_map(reuters_corpus, content_transformer(tolower));

headers4<-c("inside", "article", "text", "inside", "summary","keywords", "said", "title", "year", "will", "reuter","reuters", "percent", "friday", "also", "week")
reuters_corpus<-tm_map(reuters_corpus, removeWords, headers4); 

reuters_corpus<-tm_map(reuters_corpus, stemDocument, language="english"); 
reuters_corpus<-tm_map(reuters_corpus,stripWhitespace); 


#Document Term Matrix
dtm4<-DocumentTermMatrix(reuters_corpus,control=list(wordLengths=c(4,Inf)))
dim(dtm4)
matDTM<-as.matrix(dtm4)
dim(matDTM)
tfidf4<-weightTfIdf(dtm4)
tfidf4
sparse4<-removeSparseTerms(tfidf4,0.995)
s4<-as.matrix(sparse4); dim(s4)


#Frequent words for observation
v4<-sort(colSums(as.matrix(matDTM)), decreasing=TRUE)
df4<-data.frame(word=names(v4),freq=v4)
head(df4,30)


#BarPlot
png('reuters.png')
barplot(df4[1:20,]$freq, las = 2, names.arg = df4[1:20,]$word,
        col ="lightblue", main ="Most frequent words on 10/20/17 in Reuters",
        ylab = "Word frequencies")
dev.off()

#Wordcloud
png(filename = 'wordcloud_reu.png')
wordcloud(names(v4), v4, max.words=100, scale=c(1.5,.3), rot.per=0.15, random.order=F,colors=brewer.pal(8, "Dark2"))
dev.off()

#-----------------------------CNN---------------------

reu_text<-c("/home/harish/PycharmProjects/NewsOptimism/sample/data/cnn/20102017/")
summary(reu_text)

#corpus
reuters_corpus <- Corpus(DirSource(reu_text, recursive=TRUE),readerControl = list(reader=readPlain))

# data preprocessing
#Cleaning and Preprocessing#
reuters_corpus<-tm_map(reuters_corpus,removePunctuation);
reuters_corpus<-tm_map(reuters_corpus,removeNumbers); 

reuters_corpus<-tm_map(reuters_corpus,removeWords,stopwords("english")); 

reuters_corpus<-tm_map(reuters_corpus, content_transformer(tolower));

headers4<-c("inside", "article", "text", "inside", "summary","keywords", "said", "title", "year", "will", "cnn", "percent", "friday", "also", "week", 'photo', 'just', 'that')
reuters_corpus<-tm_map(reuters_corpus, removeWords, headers4); 

reuters_corpus<-tm_map(reuters_corpus, stemDocument, language="english"); 
reuters_corpus<-tm_map(reuters_corpus,stripWhitespace); 


#Document Term Matrix
dtm4<-DocumentTermMatrix(reuters_corpus,control=list(wordLengths=c(4,Inf)))
dim(dtm4)
matDTM<-as.matrix(dtm4)
dim(matDTM)
tfidf4<-weightTfIdf(dtm4)
tfidf4
sparse4<-removeSparseTerms(tfidf4,0.995)
s4<-as.matrix(sparse4); dim(s4)


#Frequent words for observation
v4<-sort(colSums(as.matrix(matDTM)), decreasing=TRUE)
df4<-data.frame(word=names(v4),freq=v4)
head(df4,30)


#BarPlot
png('cnn.png')
barplot(df4[1:20,]$freq, las = 2, names.arg = df4[1:20,]$word,
        col ="lightblue", main ="Most frequent words on 10/20/17 in CNN",
        ylab = "Word frequencies")
dev.off()

#Wordcloud
png(filename = 'wordcloud_cnn.png')
wordcloud(names(v4), v4, max.words=100, scale=c(1.5,.3), rot.per=0.15, random.order=F,colors=brewer.pal(8, "Dark2"))
dev.off()

#-----------------------------FOX--------------------

reu_text<-c("/home/harish/PycharmProjects/NewsOptimism/sample/data/fox//20102017/")
summary(reu_text)

#corpus
reuters_corpus <- Corpus(DirSource(reu_text, recursive=TRUE),readerControl = list(reader=readPlain))

# data preprocessing
#Cleaning and Preprocessing#
reuters_corpus<-tm_map(reuters_corpus,removePunctuation);
reuters_corpus<-tm_map(reuters_corpus,removeNumbers); 

reuters_corpus<-tm_map(reuters_corpus,removeWords,stopwords("english")); 

reuters_corpus<-tm_map(reuters_corpus, content_transformer(tolower));

headers4<-c("inside", "article", "text", "inside", "summary","keywords", "said", "title", "year", "will", "fox", "percent", "friday", "also", "week", 'photo', 'just', 'news')
reuters_corpus<-tm_map(reuters_corpus, removeWords, headers4); 

reuters_corpus<-tm_map(reuters_corpus, stemDocument, language="english"); 
reuters_corpus<-tm_map(reuters_corpus,stripWhitespace); 


#Document Term Matrix
dtm4<-DocumentTermMatrix(reuters_corpus,control=list(wordLengths=c(4,Inf)))
dim(dtm4)
matDTM<-as.matrix(dtm4)
dim(matDTM)
tfidf4<-weightTfIdf(dtm4)
tfidf4
sparse4<-removeSparseTerms(tfidf4,0.995)
s4<-as.matrix(sparse4); dim(s4)


#Frequent words for observation
v4<-sort(colSums(as.matrix(matDTM)), decreasing=TRUE)
df4<-data.frame(word=names(v4),freq=v4)
head(df4,30)


#BarPlot
png('fox.png')
barplot(df4[1:20,]$freq, las = 2, names.arg = df4[1:20,]$word,
        col ="lightblue", main ="Most frequent words on 10/20/17 in foxnews",
        ylab = "Word frequencies")
dev.off()

#Wordcloud
png(filename = 'wordcloud_fox.png')
wordcloud(names(v4), v4, max.words=100, scale=c(1.5,.3), rot.per=0.15, random.order=F,colors=brewer.pal(8, "Dark2"))
dev.off()

#-----------------------------huffington---------------------

reu_text<-c("/home/harish/PycharmProjects/NewsOptimism/sample/data/huf/20102017/")
summary(reu_text)

#corpus
reuters_corpus <- Corpus(DirSource(reu_text, recursive=TRUE),readerControl = list(reader=readPlain))

# data preprocessing
#Cleaning and Preprocessing#
reuters_corpus<-tm_map(reuters_corpus,removePunctuation);
reuters_corpus<-tm_map(reuters_corpus,removeNumbers); 

reuters_corpus<-tm_map(reuters_corpus,removeWords,stopwords("english")); 

reuters_corpus<-tm_map(reuters_corpus, content_transformer(tolower));

headers4<-c("inside", "article", "text", "inside", "summary","keywords", "said", "title", "year", "will", "huf", "percent", "friday", "also", "week", 'photo', 'just', 'news')
reuters_corpus<-tm_map(reuters_corpus, removeWords, headers4); 

reuters_corpus<-tm_map(reuters_corpus, stemDocument, language="english"); 
reuters_corpus<-tm_map(reuters_corpus,stripWhitespace); 


#Document Term Matrix
dtm4<-DocumentTermMatrix(reuters_corpus,control=list(wordLengths=c(4,Inf)))
dim(dtm4)
matDTM<-as.matrix(dtm4)
dim(matDTM)
tfidf4<-weightTfIdf(dtm4)
tfidf4
sparse4<-removeSparseTerms(tfidf4,0.995)
s4<-as.matrix(sparse4); dim(s4)


#Frequent words for observation
v4<-sort(colSums(as.matrix(matDTM)), decreasing=TRUE)
df4<-data.frame(word=names(v4),freq=v4)
head(df4,30)


#BarPlot
png('huf.png')
barplot(df4[1:20,]$freq, las = 2, names.arg = df4[1:20,]$word,
        col ="lightblue", main ="Most frequent words on 10/20/17 in huffingtonpost",
        ylab = "Word frequencies")
dev.off()

#Wordcloud
png(filename = 'wordcloud_huf.png')
wordcloud(names(v4), v4, max.words=100, scale=c(1.5,.3), rot.per=0.15, random.order=F,colors=brewer.pal(8, "Dark2"))
dev.off()

#-----------------------------nyt---------------------

reu_text<-c("/home/harish/PycharmProjects/NewsOptimism/sample/data/nyt/20102017/")
summary(reu_text)

#corpus
reuters_corpus <- Corpus(DirSource(reu_text, recursive=TRUE),readerControl = list(reader=readPlain))

# data preprocessing
#Cleaning and Preprocessing#
reuters_corpus<-tm_map(reuters_corpus,removePunctuation);
reuters_corpus<-tm_map(reuters_corpus,removeNumbers); 

reuters_corpus<-tm_map(reuters_corpus,removeWords,stopwords("english")); 

reuters_corpus<-tm_map(reuters_corpus, content_transformer(tolower));

headers4<-c("inside", "article", "text", "inside", "summary","keywords", "said", "title", "year", "will", "new york", "percent", "friday", "times", "image", 'photo', 'sign', 'newslett', 'also', 'like')
reuters_corpus<-tm_map(reuters_corpus, removeWords, headers4); 

reuters_corpus<-tm_map(reuters_corpus, stemDocument, language="english"); 
reuters_corpus<-tm_map(reuters_corpus,stripWhitespace); 


#Document Term Matrix
dtm4<-DocumentTermMatrix(reuters_corpus,control=list(wordLengths=c(4,Inf)))
dim(dtm4)
matDTM<-as.matrix(dtm4)
dim(matDTM)
tfidf4<-weightTfIdf(dtm4)
tfidf4
sparse4<-removeSparseTerms(tfidf4,0.995)
s4<-as.matrix(sparse4); dim(s4)


#Frequent words for observation
v4<-sort(colSums(as.matrix(matDTM)), decreasing=TRUE)
df4<-data.frame(word=names(v4),freq=v4)
head(df4,30)


#BarPlot
png('nyt.png')
barplot(df4[1:20,]$freq, las = 2, names.arg = df4[1:20,]$word,
        col ="lightblue", main ="Most frequent words on 10/20/17 in New york times",
        ylab = "Word frequencies")
dev.off()

#Wordcloud
png(filename = 'wordcloud_nyt.png')
wordcloud(names(v4), v4, max.words=100, scale=c(1.5,.3), rot.per=0.15, random.order=F,colors=brewer.pal(8, "Dark2"), main = "Most frequent words on 10/20/17 in New york times")
dev.off()
