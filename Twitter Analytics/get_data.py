import tweepy

# Replace with your API keys from the X Developer platform
API_KEY = 'q4pub27C4j9crIokIfjqEIjrD'
API_SECRET_KEY = 'GUFxJi1ITjxIf2RZ5eBepobJSSF4DVt6Sr9pLxtTc20zBKUMIk'
ACCESS_TOKEN = '324357139-plxMCV3KjYrKGEimFcR1QaasdOem1bQlFTEhlMhx'
ACCESS_TOKEN_SECRET = 'cy6XPi3VNSbRMiGQgN2fyzi7UPWyKuGF2YhKDuwcdhVrQ'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAALgswgEAAAAAtbxfjj3NKlNDvYNyIytq7AMfVgc%3DXlFwTploJjDxoFkFETBjB43SVUFme1rNbLPLyGBi1puBZmYaLK'


# Authenticate with the Twitter API (v1.1)
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def get_trending_topics(woeid=1):
    """
    Fetches trending topics from Twitter based on WOEID (Where On Earth ID).
    Default is WOEID 1, which is Worldwide.
    """
    try:
        # Get trending topics for the specified WOEID
        trends = api.get_place_trends(id=woeid)
        
        if trends:
            print(f"Trending Topics for WOEID {woeid}:")
            for trend in trends[0]["trends"]:
                topic = trend['President Putin']
                tweet_volume = trend['tweet_volume'] if trend['tweet_volume'] else "Not available"
                print(f"Topic: {topic}, Tweet Volume: {tweet_volume}")
        else:
            print("No trending topics found.")

    except tweepy.errors.TweepyException as e:
        print(f"An error occurred: {e}")

# Example usage:
# WOEID 1 is for worldwide trends. You can replace it with other location-specific WOEIDs.
get_trending_topics(woeid=1)