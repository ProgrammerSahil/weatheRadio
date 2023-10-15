from . import weather
from . import recommendor
from . import get_spotifyID

def fetchRecommendation():
    coords = weather.getCoords()
    keywords = weather.get_city_weather(coords[0], coords[1])
    recommendation = recommendor.generate_song_recommendations(keywords)
    return recommendation

def getSong():
    spotifyID = get_spotifyID.search_for_song(fetchRecommendation())['id']
    return spotifyID

