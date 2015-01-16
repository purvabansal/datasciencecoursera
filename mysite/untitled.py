
import tweepy,json
from py2neo import Graph,Node,Relationship,watch
graph=Graph()
#Consumer Keys and access tokens, used for OAuth
consumer_key = 'WDpZcbcXK6C4RASBaWPn2EsRM'
consumer_secret = 'p2PIw953cXOhfhjeADZUdLeaPnqwlb0DoiEv5ylmSvUqv67lWr'
access_token = '2911455882-iJf4Hs056YOAQc2P5u8aE3bAySFFW67n5SXKb6d'
access_token_secret = '3R1mtgGpMpg13QxVuFfIxoPgpSkVODtVjTQLWSVYt82IL'
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# Creation of the actual interface, using authentication
api = tweepy.API(auth)
# Creates the user object. The me() method returns the user whose authentication keys were used.
user = api.get_user('FCBarcelona')
club_tweets=1
print('Name:' + user.name)
graph.cypher.execute("MERGE (user:Person {name:'"+user.screen_name+"' , id:'"+user.id_str+"' , statuses_count :'"+str(user.statuses_count)+"'})")
for tweet in tweepy.Cursor(api.user_timeline,screen_name='FCBarcelona').items(30):
	club_tweets=club_tweets+1
	if tweet.retweet_count:
		retweet=api.retweets(tweet.id,10)
		for retweets in retweet:
			text=retweets.text.encode('ascii', errors='ignore')
			graph.cypher.execute("MATCH (owner:Person {name:'"+user.screen_name+"' , id:'"+user.id_str+"', statuses_count :'"+str(user.statuses_count)+"'}) MERGE (tweet:Tweets {text:'"+text.decode('ascii').replace("'", "\\'")+"' , id:'"+tweet.id_str+"'})  MERGE (user:Person {name:'"+retweets.user.screen_name+"' , id:'"+retweets.user.id_str+"', statuses_count :'"+str(retweets.user.statuses_count)+"'}) MERGE(owner)-[:followed_by]->(user) MERGE (user)-[:"+user.screen_name+"tweets]->(tweet)")
var = raw_input("Please enter User_Screenname: ")
i=1
for users in user_list:
	print(str(i)+'.) '+users+'\n')
	i=i+1
#return render_to_response('story/base.html')



