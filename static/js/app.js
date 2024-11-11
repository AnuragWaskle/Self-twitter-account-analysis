document.addEventListener("DOMContentLoaded", function() {
    const userInfoContent = document.getElementById("user-info-content");
    const tweetsList = document.getElementById("tweets-list");

    // Fetch user info and display it
    fetch("/api/user_info")
        .then(response => response.json())
        .then(data => {
            if (data) {
                userInfoContent.innerHTML = `
                    <div class="info-item"><i class="fas fa-user"></i><span>${data.username}</span></div>
                    <div class="info-item"><i class="fas fa-users"></i><span>Followers: ${data.followers}</span></div>
                    <div class="info-item"><i class="fas fa-user-plus"></i><span>Following: ${data.following}</span></div>
                    <div class="info-item"><i class="fas fa-pen"></i><span>Tweets: ${data.tweet_count}</span></div>
                    <div class="info-item"><i class="fas fa-info-circle"></i><span>Description: ${data.description}</span></div>
                `;
            } else {
                userInfoContent.innerHTML = "<p>Could not fetch user info.</p>";
            }
        });

    // Fetch recent tweets and display them
    fetch("/api/recent_tweets")
        .then(response => response.json())
        .then(data => {
            tweetsList.innerHTML = data.length ? data.map(tweet => `<li>${tweet}</li>`).join('') : "<li>No recent tweets found.</li>";
        });
});
