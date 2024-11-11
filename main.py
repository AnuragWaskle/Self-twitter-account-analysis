import tweepy
import time

# Twitter API credentials
API_KEY = '3v034gLBEcGfO6MQPqbq0Q2To'
API_SECRET_KEY = '6FH9zZDmAKwoscVzUka8IlfXtM876tjSOcaNfBem5rGHwf929k'
ACCESS_TOKEN = '1855876768852566016-QGe0J9UNw3dlsYPuQwzKachoQxg6g6'
ACCESS_TOKEN_SECRET = 'Emr1emzHyonozrAQV1A5p9QnszsqKr5bLWWxXEUVqv2AI'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAIGdwwEAAAAAwDmunoT4KHh57k%2F43GlOdmjtap8%3DRPz9zcTco1LNduDq0J8l2MQhvrB3ktCJEhPmduWIKb5I0pHRrR'

# Initialize the Twitter client with the Bearer Token
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Function to get user information
def get_user_info(username):
    try:
        user = client.get_user(username=username, user_fields=["public_metrics", "description"])
        if user:
            user_data = user.data
            return {
                "username": user_data.username,
                "followers": user_data.public_metrics["followers_count"],
                "following": user_data.public_metrics["following_count"],
                "tweet_count": user_data.public_metrics["tweet_count"],
                "description": user_data.description,
            }
    except tweepy.TooManyRequests:
        print("Rate limit exceeded while fetching user info. Retrying in 60 seconds...")
        time.sleep(60)  # Sleep for 60 seconds
        return get_user_info(username)  # Retry the function
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to get recent tweets
def get_recent_tweets(username):
    try:
        user = client.get_user(username=username)
        tweets = client.get_users_tweets(id=user.data.id, max_results=5)  # Fetch up to 5 recent tweets
        tweet_texts = [tweet.text for tweet in tweets.data] if tweets.data else []
        return tweet_texts
    except tweepy.TooManyRequests:
        print("Rate limit exceeded while fetching tweets. Retrying in 60 seconds...")
        time.sleep(60)  # Sleep for 60 seconds
        return get_recent_tweets(username)  # Retry the function
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Test the functions (Uncomment these during testing)
if __name__ == "__main__":
    print("Testing get_user_info:")
    user_info = get_user_info("NehaJoshi111270")
    print("User Info:", user_info)

    print("\nTesting get_recent_tweets:")
    recent_tweets = get_recent_tweets("NehaJoshi111270")
    print("Recent Tweets:", recent_tweets)
