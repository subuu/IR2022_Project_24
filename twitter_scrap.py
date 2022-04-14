import snscrape.modules.twitter as sntwitter
import pandas as pd
import itertools

# Creating list to append tweet data to
tweets_list = []

# Using TwitterSearchScraper to scrape data and append tweets to list
# query='covid-19 OR covid19 OR coronavirus OR vaccine OR vaccinate OR vaccination OR omicron OR deltavariant OR #covidvaccine OR #coronavaccine OR #covidvaccination OR #StayHomeStaySafe OR pfizer-bioNTech OR pfizer OR moderna OR janssen'
# OR Corporate tax OR Short term and Long term capital gain tax'
q = '"union budget" OR "corporate tax" OR "income tax" OR disinvestment OR "capital expenditure" OR cess OR "fiscal deficit" OR "public debt" OR inflation OR gdp OR defense OR infrasturucture OR'
query1 = '#unionbudget2022-23 OR #budget2022 OR #unionbudget OR #budget OR #unionbudget2022 OR #unionbudget22-23'
#loc = '20.5937, 78.9629, 2000km'
for i, tweet in enumerate(
        sntwitter.TwitterSearchScraper(query1 + 'near:"India" since:2021-12-01 until:2022-01-31 lang:en').get_items()):
    if i > 10000:
        break
    tweets_list.append(
        [tweet.id, tweet.date, tweet.user.username, tweet.content, tweet.user.location, tweet.user.verified,
         tweet.retweetCount, tweet.replyCount, tweet.likeCount])

# Creating a dataframe from the tweets list above
tweets_df2 = pd.DataFrame(tweets_list, columns=['Tweet Id', 'Datetime', 'Username', 'Tweet Content', 'User Location',
                                                'User Verified', 'Retweet Count', 'Reply Count', 'Like Count'])
tweets_df2.to_csv(r'C:\Users\User\Desktop\scrap\india2.csv')
