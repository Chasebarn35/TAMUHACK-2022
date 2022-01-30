from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import twint
import csv

def sentiment_scores(sentence): #fullscale copied from geek4geek omegalul
 
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()
 
    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)
     
    # print("Overall sentiment dictionary is : ", sentiment_dict)
    # print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
    # print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
    # print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")
 
    # print("Sentence Overall Rated As", end = " ")
 
    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05 :
        return "Positive"
 
    elif sentiment_dict['compound'] <= - 0.05 :
        return "Negative"
 
    else :
        return "Neutral"

#------------------------------------------ Collects Twitter Data to a csv with the name of the username
def TweetGrab(TweetCount, username):
    c = twint.Config()

    c.Username = username
    c.Custom["tweet"] = ["tweet"]
    c.Custom["user"] = ["bio"]
    c.Limit = TweetCount # Grabs in batches of 20, so TweetCount will not actually be necessarily accurate
    c.Store_csv = True
    c.Output = username + "Twitter.csv"
    twint.run.Search(c)
#-----------------------------------------

#-----------------------------------------TODO Facebook Data Collection



#-----------------------------------------

#--------------------------------------- TODO Parse through each tweet and determine if it's "good" or bad
User = ""
TweetGrab(100,User)
sumPos = 0
sumNeg = 0
sumNeu = 0
with open(User+"Twitter.csv", newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='\n', quotechar='|')
    for row in reader:
        tempans = sentiment_scores(row)
        if(tempans == "Positive"):
            sumPos+=1
        if(tempans == "Negative"):
            sumNeg+=1
        if(tempans == "Neutral"):
            sumNeu+=1
print(str(sumPos) + " positive Tweets")
print(str(sumNeg) + " negative Tweets")
print(str(sumNeu) + " neutral Tweetss")
