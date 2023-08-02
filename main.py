import os
from model.deepdives import DeepDives, Type, Variant
from service.drg import DRGService
from service.reddit import RedditService
import datetime


# Initialize services
drgService = DRGService()
redditService = RedditService()

# Get the last weekly deep dives thread url
last_thread_url: str = redditService.get_last_weekly_deep_dives_thread_url()

# Get the current weekly deep dive data
deepdives: DeepDives = drgService.get_deepdives()
dd: Variant = deepdives.get_variant(Type.DEEP_DIVE)
edd: Variant = deepdives.get_variant(Type.ELITE_DEEP_DIVE)

# Create the post title
date = datetime.datetime.strptime(deepdives.startTime, "%Y-%m-%dT%H:%M:%SZ")
day = date.day
suffix = "th"
if 11 <= day <= 13:
    suffix = "th"
elif day % 10 == 1:
    suffix = "st"
elif day % 10 == 2:
    suffix = "nd"
elif day % 10 == 3:
    suffix = "rd"
else:
    suffix = "th"
formatted_date = date.strftime(f"%-d{suffix} %B %Y")
thread_title: str = f"Weekly Deep Dives Thread - {formatted_date}"

# Create the post text
thread_text: str = f"""
Please use this thread to discuss the deep dives of the week.
___
**{str(dd)}**

|**Stage**|**Primary**|**Secondary**|**Anomaly**|**Warning**|
|:-|:-|:-|:-|:-|
{dd.get_stage(1)}
{dd.get_stage(2)}
{dd.get_stage(3)}

**{str(edd)}**

|**Stage**|**Primary**|**Secondary**|**Anomaly**|**Warning**|
|:-|:-|:-|:-|:-|
{edd.get_stage(1)}
{edd.get_stage(2)}
{edd.get_stage(3)}
___
Other resources:

* See last week's thread [here]({last_thread_url})
* Watch the GSG team undertake the dives on their [Twitch channel](https://www.twitch.tv/ghostship_games)
  * Deep Dive: Thursday @ 11am UTC
  * Elite Deep Dive: Friday @ 11am UTC
* Get weekly deep dive info and more in JSON format from [DRG API](https://drgapi.com/)
* Post weekly deep dive info and more in your Discord server with [Bosco](https://discord.com/api/oauth2/authorize?client_id=1097476432579539026&permissions=2147485696&scope=bot)
"""

# Post the weekly deep dives thread to Reddit
redditService.post_weekly_deep_dives_thread(thread_title, thread_text)
