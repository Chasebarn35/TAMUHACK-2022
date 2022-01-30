from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from instagramy import InstagramUser,InstagramPost
import twint
import csv

def sentiment_scores(sentence): #fullscale copied from geek4geek omegalul
 
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()

    sentiment_dict = sid_obj.polarity_scores(sentence)

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

#-----------------------------------------TODO Instagram Data Collection
def InstaGrab(username):
    user = InstagramUser(username, from_cache = True) ##TODO MAKE SURE THE CACHE IS WORKING
    for x in user.posts:
        with open(username+"Instagram.csv",'w', encoding ='UTF8') as csvfile:
            writer = csv.writer(csvfile)
            print(InstagramPost(x.shortcode,from_cache = True).text)
            writer.writerows(InstagramPost(x.shortcode,from_cache = True).text)


#-----------------------------------------

#--------------------------------------- Parse through each tweet and determine if it's "good" or bad. this is not super great
def TweetRate(User):
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
#------------------------------------------

InstaGrab('taylorswift')