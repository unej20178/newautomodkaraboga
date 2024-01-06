import praw

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    password="",
    user_agent="",
    username="",
)




text = "hi favorite (i hope so) balkan bot here, here's some links for some reason \n\n [imageboard](http://balkansirl.net) [discord](https://discord.gg/balkansirl) \n\n also you can click [here](https://www.reddit.com/message/compose/?to=/r/balkans_irl) to contact the mods. \n\n Also, \n\n\n\n K"


for submission in reddit.subreddit("balkans_irl").stream.submissions():
    submission.reply(text)
