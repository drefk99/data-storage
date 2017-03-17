import json                                                                                                     
import tweepy                                                      
from tweepy import Stream                                             
from tweepy.streaming import StreamListener                           
from tweepy import OAuthHandler                                       
import pandas as pd                                                   
import pickle                                                                                                                                
consumer_key = 'QvyttUNFpYvpf05FiSrsFOjZz'                            
consumer_secret = '0yvZMOrq0qKwz1dcKhzKB04RinFdxZYqYOghQr1mNtg612AX6g'                                          
access_token = '227835837-WD07ixlyOeLqkeywbnMYzk5dnebJjd1pA4sKpOjl'
access_secret = '6utbaX2ab3UrpL4PpfSx6ToCuuQZgZ5zDDqKQq2albTLL'  
                                                                                                                 
auth = OAuthHandler(consumer_key, consumer_secret)                                                              
auth.set_access_token(access_token, access_secret)                                                              
                                                                                                                 
api = tweepy.API(auth)
datos_tweets={}                                                       
datos_tweets.setdefault('date',[])                                    
datos_tweets.setdefault('texts',[])                                   
datos_tweets.setdefault('user_id',[])                                 
datos_tweets.setdefault('retweet_count',[])                           
                                                                          
#print(place_id)                                                      
for tweet in tweepy.Cursor(api.search, q="Bancomer", lang="es", since="2017-03-10", until="2017-03-11").items():
     if not hasattr(tweet,'retweeted_status'):                      
         datos_tweets['date'].append(tweet.created_at.isoformat())
         datos_tweets['texts'].append(tweet.text)                                                                
         datos_tweets['user_id'].append(tweet.user.id)                                                           
         datos_tweets['retweet_count'].append(tweet.retweet_count)                                               
print(pd.DataFrame(datos_tweets))


es.index(index='skynet_beeva', doc_type='bancomer', id='2017-03-09', body= datos_tweets) 
es.get(index='skynet_beeva', doc_type='bancomer', id='2017-03-16')

ela_bancomer = es.get(index='skynet_beeva', doc_type='bancomer', id='2017-03-15')

with open('andrea_prueba.json', 'w') as fp:                                                                     
         json.dump(ela_bancomer, fp)
