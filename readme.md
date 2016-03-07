#Time Serious

## Time Serious is an [editors lab hackathon project](http://www.walkleys.com/editorslab/) which takes a data input, analyses it, and outputs a news report in natural language, with publication-ready graphics. [Here's the working - but buggy - demo](https://timeserious.herokuapp.com/).

### The problem

In a media environment where reporters have less time, journalists often have to write formulaic stories such as covering stories about the weather - how hot is it, is it a new record, or recurring stories like politician's expenses and donations - who spent the most, who are the top 5, was it more or less than last year. 

Reporters themselves want more time to work on deeper, more meaningful stories - like why the climate is changing, which politicians are abusing the expenses system. There is a strong public benefit in these stories.

One thing that many of these formulaic, recurring stories have in common is that they involve data, often time series data. In surveying just the last week of stories in a small section of our own site, we found at least five such examples. Economic figures, polling figures, emissions data, and weather data.

### The solution

So, our pitch was to build a system that can automate the analyse, writing, and production of graphics for these stories. Data in, news story out. 

While similar things have been built before, as far as we know these systems are either proprietary and closed, or they've been built for specific data input, like earthquakes or sport stats. Ours will be open source and data agnostic.

For our demo, all you need to do is pop the data into the Google sheet and enter some key variables.

Once you input the variables and the data source, you can tell the program to build the news report. Then, you can pick up the news report and publish it on your site with any additions you think necessary.

Some people have joked that we’re making our reporters redundant. We’re really not. What we’re doing is solving a major newsroom problem. We’re keeping editors happy, because they get their story about how hot it is, and also faster than the competition. We’re keeping journalists happy, because they get the chance to spend that little bit more time digging into the data they really want to look at and going beyond the surface.

And we’re in turn providing a better news product for our readers, who get the benefit of the formula driven news stories and the deeper and more meaningful investigations our reporters want to work on.

It also has the added benefit of taking the hassle out of data analysis and graphic production.

In the future, this could be used, and built on, in a number of ways:

* plugged into a scraper, which would produce a story automatically when a dataset is updated (eg. weather forecasts for heatwaves, crime statistics, period data releases like donations)
* plugged into a scraper, and producing a story whenever a condition is met (eg. crime statistics go up, five days of above average temperatures)
* broadened to ingest different data formats, like using the Twitter API to automate 'viral' social media stories (identify key original tweets, volume of tweets on topic, etc.) or political campaign speeches (natural language processing, text and sentiment analysis etc.)
* adding an graphical interface to allow journalists to create new templates
* use machine learning to score entities and text for importance and public interest based on previous news reports (ie. putting a certain company further up the news story, or putting a certain sentence structure higher up the story rather than lower)
* use machine learning to automate the creation of new templates based on previous news stories





