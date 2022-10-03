
import tweepy as tw
import time



# Connecting to your Twitter Developer APIs
api_key= '' #put your api_key
api_secret= '' #put your api_secret
access_token= ''#put your acces token
access_token_secret= "" #put your acces_token_secret


bearer_token = ''

# Authenticating the APIs
auth = tw.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

def getUserFollowers(username) :
    Followers = []
    user = api.get_user(screen_name=username)
    for i, _id in enumerate(tw.Cursor(api.get_follower_ids,
                                      screen_name = username).items(400)) : # put the number of account you want to get  (here its 400)
        Followers.append(_id)


    return Followers

def followUser(screen_name) :
    api.create_friendship(screen_name = screen_name)

def unfollowUser(screen_name) :
    api.destroy_friendship(screen_name = screen_name)




friendtoadd = getUserFollowers('account') #put the name of the account you want


for i in range(len(friendtoadd)) :
    try:
        screen_name = api.get_user(user_id=friendtoadd[i]).screen_name
        followUser(screen_name)  #be careful you cant add more than 400 people a day
        print(screen_name + " a été ajouter")
        time.sleep(5)
    except:
        continue






