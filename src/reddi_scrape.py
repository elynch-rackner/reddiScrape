!pip install requests pushshift.py
import requests
import time
from pushshift.py import PushshiftAPI


def scrape_reddit(subreddit, query, after, before, size):
  api = PushshiftAPI()

  # Scrape data from subreddit
  data = api.search_submissions(subreddit=subreddit,
                                q=query,
                                after=after,
                                before=before,
                                size=size)
  return data

subreddit = "medicaldevices"
query = "issues OR problems"
after = "2020-01-01"
before = "2020-12-31"
size = 1000

data = []

while True:
  try:
    # Scrape data from subreddit
    submissions = scrape_reddit(subreddit, query, after, before, size)
   
    # Add submissions to data list
    data.extend(submissions)
   
    # Get timestamp of last submission
    after = submissions[-1]["created_utc"]
   
    # Delay next iteration
    time.sleep(5)
  except Exception as e:
    raise e
