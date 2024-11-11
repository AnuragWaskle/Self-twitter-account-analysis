from flask import Flask, jsonify, render_template
from main import get_user_info, get_recent_tweets

app = Flask(__name__)

# Replace with the Twitter username you want to analyze
TWITTER_USERNAME = "NehaJoshi111270"  # Change this to your desired Twitter username

# Route for the main page (index.html)
@app.route("/")
def home():
    return render_template("index.html")  # This should point to 'templates/index.html'

# API route to get user info
@app.route("/api/user_info")
def user_info():
    info = get_user_info(TWITTER_USERNAME)
    return jsonify(info)

# API route to get recent tweets
@app.route("/api/recent_tweets")
def recent_tweets():
    tweets = get_recent_tweets(TWITTER_USERNAME)
    return jsonify(tweets)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
