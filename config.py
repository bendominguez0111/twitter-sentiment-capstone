from dotenv import load_dotenv
import os

env_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '.env')

load_dotenv(env_path)

class Config:
    TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
    TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
    TWITTER_CONSUMER_KEY = os.getenv('TWITTER_CONSUMER_KEY')
    TWITTER_CONSUMER_SECRET_KEY = os.getenv('TWITTER_CONSUMER_SECRET_KEY')

    TWITTER_SEARCH_BASE_URL = "https://api.twitter.com/1.1/search/tweets.json"

    #add more analysts here.
    ANALYSTS = {
        'Matthew Berry': 'MatthewBerryTMR',
        'Field Yates': 'FieldYates',
        'NFL Fantasy Football': 'NFLFantasy',
        'PFF Fantasy Football': 'PFF_Fantasy',
        'FantasyPros': 'FantasyPros',
        'Bleacher Report': 'BleacherReport'
    }
