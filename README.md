# Die Hard Christmas
Using the Twitter API, performed sentiment analysis on whether people think Die Hard is a Christmas movie or not. 

# Problem Statement
One of the great debates trending Twitter every holiday season is whether or not Die Hard is in fact a Christmas movie. This year, we seemed to get even more confirmation that Die Hard is a Christmas classic from Fox, the NYPD and the LAPD. What’s more Christmas than Bruce Willis as NYPD detective John McClane saving his estranged wife and her coworkers from Hans Gruber and his team of terrorists when they attack their holiday party at Nakatomi Plaza. (Fun Fact: Nakatomi Plaza is actually Fox’s main corporate building, Fox Plaza, soon to be Disney Plaza.) Like Santa, Bruce has to shimmy through small spaces, his being the ventilation system, so what more do you need to convince you?

On the other hand, just because a movie takes place during Christmas, doesn’t necessarily mean it’s a Christmas movie. Many argue, in fact, that technically, the movie could take place on any other day than Christmas and still work. I mean, Lethal Weapon is set during Christmas and even includes a Jingle Bell Rock opening, but you don’t hear as many people debating whether that’s a Christmas movie or not. Then, there’s also Bruce Willis’ take on whether the movie is a Christmas movie. (Spoiler Alert: he doesn’t).

***So, is Die Hard really a Christmas movie?***

For my first soiree into sentiment analysis, I decided to use Twitter’s API to determine whether the public truly thinks Die Hard is a Christmas movie or not. In my project, I will be showing how I:

  1. Extracted twitter data using the TwitterAPI library
  2. Do some basic statistics and visualizations using numpy, matplotlib, seaborn, and WordCloud.
  3. Do sentiment analysis of extracted tweets (2,100 tweets from Christmas Day) using Peter Turney ‘s technique mentioned in his paper Thumbs Up or Thumbs Down? Semantic Orientation Applied to Unsupervised Classification of Reviews as well as TextBlob.

# Data Source
  - Data was sourced from [Twitter's API](https://developer.twitter.com/en/docs.html). 

# Analytical Approach
See [my blog](http://amyksu.com/blog/diehard-pt3) for my sentiment analysis approach and [jupyter notebooks](https://github.com/amyksu/die-hard-christmas/blob/master/Part%203%20Sentiment%20Analysis.ipynb).

# Results and Conclusion
For my conclusion, please check out my [blog post](http://amyksu.com/blog/diehard-pt4).

# Limitations
For my sentiment analysis, I used Peter Turney's Semantic Orientation techinique as well as TextBlob. There were limitations to both techniques. 

## Semantic Orientation
The PMI-based approach to sentiment analysis is meant to be a simple and intuitive introduction. However, because it is a simple algorithm, there are some limitations. According to Peter Turney’s paper, the algorithm achieves an average accuracy of 74% in his evaluation of 410 reviews. In addition, he states that the accuracy ranges from 84% to 66%. Furthermore, the semantic scores are calculated based on terms, or words, meaning that there is no notion of “concept” and other aspects of natural language, such as phrases such as not good or very bad.

## TextBlob
When looking at our tweets and the sentiment labels, there are some inaccuracies with the way some of the tweets are labeled. For example, “I guess Die Hard is a Christmas movie” was labeled as a negative tweet when it should be positive, while “Forget ‘Die Hard,’ ‘Go’ Is the Ultimate Anti-Christmas Movie” is labeled as negative as well, but should be neutral.

# Note
  - Tweets were pulled on the evening of Christmas (December 25, 2018) and the Twitter API pull was stopped once I had gotten 2,111 tweets.
  
