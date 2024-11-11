# Self-twitter-account-analysis

# Twitter User Info and Recent Tweets Viewer

A simple web application built using Flask and Tweepy that allows users to fetch and display basic information about a Twitter user, such as followers count, following count, tweet count, and description, along with the user's most recent tweets.

This project was developed for a friend to provide a quick and easy way to view Twitter user details and recent tweets directly from a web interface.

## Features

- **User Information**: Displays the username, followers count, following count, tweet count, and description.
- **Recent Tweets**: Shows the most recent 5 tweets from the user.
- **Responsive Design**: Works on both desktop and mobile devices.
- **Modern UI**: A clean, modern, and attractive UI using CSS gradients, cards, and Font Awesome icons.

## Tech Stack

- **Backend**: Python with Flask framework
- **Twitter API**: Tweepy library
- **Frontend**: HTML, CSS, and JavaScript
- **Fonts**: Google Fonts (Roboto and Ubuntu)
- **Icons**: Font Awesome for icons
- **Responsive Design**: CSS Media Queries for mobile-friendly layout

## Prerequisites

- Python 3.x
- Flask (`pip install flask`)
- Tweepy (`pip install tweepy`)

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/twitter-user-info.git
    ```

2. Navigate to the project folder:
    ```bash
    cd twitter-user-info
    ```

3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Add your Twitter API credentials:
    - Open `main.py`.
    - Replace the placeholders for `API_KEY`, `API_SECRET_KEY`, `ACCESS_TOKEN`, `ACCESS_TOKEN_SECRET`, and `BEARER_TOKEN` with your own Twitter API credentials.
    - If you don't have Twitter API credentials, you can get them by creating a Twitter Developer account and creating an app [here](https://developer.twitter.com/en/apps).

5. Run the Flask app:
    ```bash
    python app.py
    ```

6. Visit `http://127.0.0.1:5000/` in your web browser to view the app.

## How It Works

- The backend uses Flask to serve the web pages and interact with the Twitter API through Tweepy to fetch user information and tweets.
- The frontend fetches data from the Flask API endpoints and displays it in a user-friendly format.
- The page is fully responsive, ensuring a good user experience across devices.

## Endpoints

1. **GET /api/user_info**: Returns the basic user information (username, followers, following, tweet count, description).
2. **GET /api/recent_tweets**: Returns the most recent 5 tweets from the specified Twitter user.

## Folder Structure

```
/your-project
    /templates
        index.html           # Main HTML template
    /static
        /css
            styles.css       # CSS file for styling
        /js
            app.js           # JavaScript file for front-end functionality
    app.py                   # Flask application
    main.py                  # Contains Twitter API functions
    requirements.txt         # List of dependencies
    README.md                # This file
```

## License

This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgements

- **Tweepy**: For interacting with the Twitter API.
- **Flask**: For building the backend web application.
- **Font Awesome**: For the icons used in the frontend.
- **Google Fonts**: For the custom typography.

---

You can now create the `requirements.txt` file, which lists the dependencies for your project. Here’s a simple one:

```
Flask==2.2.2
tweepy==4.12.1
```

Feel free to modify this README file according to any additional details you'd like to include about your project. Let me know if you need help with anything else!
