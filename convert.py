# convert.py
import googlemaps
api_key = 'AIzaSyD2uJOj1fv9l2Dv1_Srr_mvQI36X5852vs'


def getLat(zipcode):
    gmaps = googlemaps.Client(key=api_key)
    geocode_result = gmaps.geocode(zipcode)
    ll = geocode_result[0]["geometry"]["location"]
    lat = (ll["lat"])
    return lat


def getLng(zipcode):
    gmaps = googlemaps.Client(key=api_key)
    geocode_result = gmaps.geocode(zipcode)
    ll = geocode_result[0]["geometry"]["location"]
    lng = (ll["lng"])
    return lng


def getAddress(zipcode):
    gmaps = googlemaps.Client(key=api_key)
    geocode_result = gmaps.geocode(zipcode)
    address = geocode_result[0]["formatted_address"]
    return address


def reverse(lat, lng):
    gmaps = googlemaps.Client(key=api_key)
    reverse_geocode_result = gmaps.reverse_geocode((lat, lng))
    return reverse_geocode_result
