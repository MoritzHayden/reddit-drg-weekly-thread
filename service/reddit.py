import os
from dotenv import load_dotenv
import praw


class RedditService:
    def __init__(self):
        load_dotenv()
        self.client_id: str | None = os.getenv('REDDIT_CLIENT_ID')
        self.client_secret: str | None = os.getenv('REDDIT_CLIENT_SECRET')
        self.username: str | None = os.getenv('REDDIT_USERNAME')
        self.password: str | None = os.getenv('REDDIT_PASSWORD')
        self.user_agent: str = "MoritzHayden:reddit-drg-weekly-thread"
        self.check_for_async: bool = False

    def get_last_weekly_deep_dives_thread_url(self) -> str:
        reddit = praw.Reddit(
            client_id=self.client_id,
            client_secret=self.client_secret,
            user_agent=self.user_agent,
            check_for_async=self.check_for_async
        )
        threads = reddit.subreddit("DeepRockGalactic").search(query="Weekly Deep Dives Thread",
                                                              sort="hot",
                                                              time_filter="week")
        return next(threads).url

    def post_weekly_deep_dives_thread(self, thread_title: str, thread_text: str) -> None:
        reddit = praw.Reddit(
            client_id=self.client_id,
            client_secret=self.client_secret,
            username=self.username,
            password=self.password,
            user_agent=self.user_agent,
            check_for_async=self.check_for_async
        )
        reddit.subreddit("DeepRockGalactic").submit(
            title=thread_title,
            selftext=thread_text,
            flair_text="Discussion",
            flair_id="31a3bce6-8a6d-11e8-981e-0ef3b3afe88e"
        )
        return None
