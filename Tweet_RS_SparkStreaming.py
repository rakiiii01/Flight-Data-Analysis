import json
from socket import socket
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

WORDS = ['#bitcoin', '#cryptocurrency', '#crypto', '#litecoin', '#satoshi']

'''
Twitter Developer Account Credentials
'''
access_token = 'fp2FjTRyW62ftg2yGp4nBUPazQvKZBzS7LG9dEJE'
access_secret = 'F3GT0LW8m4x27UuyLsEfjmvIQUvTKrQzLyxxnDiLvOJBj'
consumer_key = '9rmQqBmcEJkNEkjSadQwBVswx'
consumer_secret = 'p7YrR3Wohr1oXRwd94JHYVC3eFla3ADS0CrmRczDrsvCXIczS3'


class TweetStreamListener(StreamListener):

    def __init__(self, csocket):
        self.client_socket = csocket

    def on_data(self, data):
        try:
            msg = json.loads(data)
            print(msg['text'].encode('utf-8'))
            self.client_socket.send(msg['text'].encode('utf-8'))
            return True
        except BaseException as be:
            print('Error on_data : %s' % str(be))
        return True

    def on_error(self, status):
        print(status)
        '''
        For not killing the tweet stream
        '''
        return True


def sendData(c_socket):
    '''
    Create Auth object
    '''
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    twitter_stream = Stream(auth, TweetStreamListener(c_socket))
    '''
    Custom Filter to pull all traffic for the said filters in english language in real time.
    '''
    twitter_stream.filter(languages=['en'],track=WORDS)


if __name__ == '__main__':
    '''
    Create a socket object
    '''
    s = socket()   
    '''
    Local machine name
    '''
    host = '127.0.0.1' 
    '''
    Reserve a port for the service.
    '''
    port = 9999    
    '''
    Bind to the port
    '''
    s.bind((host, port))       

    print('Listening on port: %s' % str(port))
    
    '''
    Waiting for client connection.
    '''
    s.listen(5) 
    '''
    Establish connection with client.
    '''
    c, addrs = s.accept()        

    print('Received request from: ' + str(addrs))

    sendData(c)
