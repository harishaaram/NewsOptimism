# NewsOptimism
Comparative Analysis of various news media articles by quantifying how much of words are positive in the article.

# Problem
All around the world both good and bad happens, and we get to know only those that are exposed to us. And, that’s the primary responsibility of the media. But the bigger responsibility of these media houses is the way in which they express the content to the people. 

A responsible media house’s content should be original, unbiased, free of exaggeration and should be very sensitive in handling the emotions of it’s readers and viewers. A same story could be told in different ways and these different ways could definitely trigger different emotions among it’s readers.

It is known that we become who we are by what we say and what we read. Reading a story that’s filled with positive words would make us feel more positive and vice versa. So the wordings of a content definitely plays an equal role as that of the content itself. 

This project aims to answer how some of the major media houses in USA are giving importance to the wordings of their content. The answer would allow the readers to wisely choose their daily source of news that truly cares about its readers.

There is a famous concept called [**Law of attraction**](http://www.thelawofattraction.com/what-is-the-law-of-attraction/) written by **Rhonda Byrne** in her book [Secret](https://en.wikipedia.org/wiki/The_Secret_(book)).It says that we become who we are by what we say!

# Hypothesis:
The English language words are considered to find out how much of positivity or negativity it contains. We measure this by comparing the
frequency of occurrence of the words across various news media.

# Target Audience:
The headline scrollers - people who scroll the news headlines and text directly from the media's homepage.

# Datasource:
    1. "http://www.nytimes.com/"
    2. "http://www.foxnews.com/"
    3. "http://www.reuters.com/"
    4. "http://www.cnn.com/"
    5. "http://www.huffingtonpost.com/"

These are the famous news websites considered based on the unique visitor count obtained from the [research](http://www.journalism.org/files/legacy/NIELSEN%20STUDY%20-%20Copy.pdf)

# Language:
    1. Python 3
    2. R

## Considerations to keep in mind:
1. Country considered is ONLY USA.
2. Data is extracted from the FRONT page of the above data sources.
3. The article title and the summary are extracted.
4. Data has been scrapped from the resources at the **same** time(since it gets updated regularly).
5. Our assumption is there is no bias between choosing articles.

## The Approach
1. Collect news headlines and summary from all our datasets.
2. Convert the text document into Term Documen Matrix
3. Preprocess the data.
4. Tf-idf method is applied to find the importance of word.
5. Sentiment analysis to show of text how much positive or negative for each day.

# Progress:

## 1) Data Extraction Phase:

Data is collected as Text Document from the datasources as mentioned above. Have a look at the text file of the articles
in the reuters.com front page.
![Reuters_10/17/2017](sample/reutersTextSamplefile.png)

It is then converted to a structured CSV format.
## [Have Peek at the file structure](http://nbviewer.jupyter.org/github/harishaaram/NewsOptimism/blob/master/Sample_data_peek.ipynb)

The data as CSV file has the following columns:

* `TITLE`: the Title of the article.
* `SUMMARY`: first few lines of the article's text.
* `TEXT`: Full text inside the article
* `URL`: web link to the article.
* `KEYWORDS`: important words in the article.

[Download original csv file](sample/reuters.csv)

