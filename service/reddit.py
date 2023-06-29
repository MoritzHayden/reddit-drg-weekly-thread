import os
from dotenv import load_dotenv
import praw


class RedditService:
    def __init__(self):
        load_dotenv()
        self.reddit = praw.Reddit(client_id=os.getenv('REDDIT_CLIENT_ID'),
                                  client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
                                  username=os.getenv('REDDIT_USERNAME'),
                                  password=os.getenv('REDDIT_PASSWORD'),
                                  user_agent="MoritzHayden:reddit-drg-weekly-thread",
                                  check_for_async=False)

    def get_last_weekly_deep_dives_thread_url(self) -> str:
        threads = self.reddit.subreddit("DeepRockGalactic").search(query="Weekly Deep Dives Thread",
                                                                   sort="hot",
                                                                   time_filter="week")
        return next(threads).url

    def post_weekly_deep_dives_thread(self, thread_title: str, thread_text: str) -> None:
        self.reddit.subreddit("DeepRockGalactic").submit(
            title=thread_title,
            selftext=thread_text,
            flair_text="Discussion",
            flair_id="31a3bce6-8a6d-11e8-981e-0ef3b3afe88e"
        )
        return None
