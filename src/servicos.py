import tweepy

from typing import Any, Dict, List
# from matplotlib.pyplot import get
from src.chaves import *

def get_trends(woe_id: int) -> List[Dict[str, Any]]:
    
    auth = tweepy.OAuth1UserHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    
    api = tweepy.API(auth)

    trends = api.get_place_trends(woe_id)

    return trends[0]["trends"]

