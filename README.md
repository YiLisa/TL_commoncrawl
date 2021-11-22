# TL_commoncrawl
### TASK
In this task, your goal is to find pages from the ​common crawl archive​ that discuss ​or are relevant to COVID-19’s economic impact. We would like you to produce a list of 1000 pages (URL’s) from the ​2020 archives​ that discuss or are relevant to COVID-19’s economic impact. For every result URL in your list that meets the stated requirement, you will earn 1 point, and for every result URL in your list that does not fit the requirement, you will lose 1 point. Your goal is to maximize the number of points so if you are able to produce more than 1000 pages that’s even better, but 1000 is a good goal for the allocated time. Also include which month(s) of the 2020 archives you pulled the URLs from.
### Attempts
After reading tutorials from http://commoncrawl.org/the-data/examples/ I tried several methods to tackle this problem.
At first, I tried to use the comcrawl library from https://github.com/michaelharms/comcrawl to search the data in the archieve. Then I tried some other library to accessing WARC files like warc and warcio. However, I kept receiving errors about the __builtin__ when running and I can't find a working solution for this problem. So after 2-3hr of trying install and run these packages, I decided to shift my direction.
### Final Appoarch
I selected some keywords about covid and economic impact for searching purpose. And some trusted news websites urls to construct the url with index refering to date in common crawl archive. Then I request the response with those urls and use beautifulsoup to get text from the html of the website. Then we can find the related keywords in the content and add the url and month to the result list if that is a match. I also add threads to speed up the crawling process. Due to the limited computing power of my laptop, I didn't finish running the script in time.
### Possible imporvement
Simply finding keywords in content is not the best way to know the topic of the article. A better way may be extract the whole article and analyse it with NLP package like nltk and gensim to get a better understanding of the article. We can train a model for embedding and get a vector representation for tfidf words and classify the content to see if it is related to covid economics impact.
