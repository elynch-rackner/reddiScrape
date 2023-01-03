import requests
import time
from pushshift.py import PushshiftAPI


def scrape_reddit(subreddit, query, after, before, size):
    try:
        api = PushshiftAPI()

        # Scrape data from subreddit
        data = api.search_submissions(subreddit=subreddit,
                                      q=query,
                                      after=after,
                                      before=before,
                                      size=size)
        return data
    except Exception as e:
        raise e
