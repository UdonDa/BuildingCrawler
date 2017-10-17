

from urllib.request import *
from urllib.parse import *
from keyHolder import keyHolder


class GooglePlacesCrawler():
    def __init__(self):
        self.G_APIKEY = keyHolder.apiKey()
        self.G_base = "https://maps.googleapis.com/maps/api/place/"
        self.G_sensor = "false"

    def send_req(self, url):
        try:
            response = urlopen(url)
            doc = response.read()
            return doc
        except HTTPErrorProcessor:
            print("404")
            return None

    def make_textsearch_req(self, query):
        url = "{}textsearch/xml?".format(self.G_base)
        url += "&query={}".format(quote(query.replace(" ", "+")))
        url += "&sensor={}".format(self.G_sensor)
        url += "&key={}".format(self.G_APIKEY)
        return url

    def make_radarsearch_req(self, location, radius, seachitems):
        # ここでURL作成！！！！！！
        url = "{}search/json?".format(self.G_base)
        url += "location={}".format(location)
        url += "&radius={}".format(str(radius))

        try:
            url += "&types={}".format(quote(seachitems["types"]))
        except:
            pass

        url += "&language=ja"
        url += "&sensor={}".format(self.G_sensor)
        url += "&key={}".format(self.G_APIKEY)
        return url

    def make_search_req(self, location, radius, searchitems):
        url = self.G_base + "search/xml?"
        url += "location=" + location
        url += "&radius=" + str(radius)
        try:
            url += "&keyword=" + quote(searchitems["keyword"])
        except:
            pass
        try:
            url += "&name=" + quote(searchitems["name"])
        except:
            pass
        try:
            url += "&types=" + quote(searchitems["types"])
        except:
            pass
        url += "&sensor=" + self.G_sensor
        url += "&key=" + self.G_API_key
        return url

    def make_details_req(self, reference):
        url = self.G_base + "details/xml?"
        url += "&reference=" + reference
        url += "&sensor=" + self.G_sensor
        url += "&key=" + self.G_API_key
        return url

    def send_textsearch(self, query):
        # Search by text query
        url = self.make_textsearch_req(query)
        return self.send_req(url)

    def G_radarsearch(self, location, radius, searchitems):
        """
        :param location: (ex)"35.562479,139.716051"
        :param radius: (ex)1000
        :param searchitems: (ex) {"types": "atm"}  下の表参考
        :return: request
        """
        url = self.make_radarsearch_req(location, radius, searchitems)
        return self.send_req(url)

    def G_search(self, location, radius, searchitems):
        url = self.make_search_req(location, radius, searchitems)
        return self.send_req(url)

    def G_details(self, reference):
        url = self.make_details_req(reference)
        return self.send_req(url)


def main():
    googlePlacesCrawler = GooglePlacesCrawler()
    #TODO: 下の３つの値を欲しいものに変える
    location = "35.562479,139.716051"
    radius = 1000
    searchitems = {"types": "atm"}

    b = googlePlacesCrawler.G_radarsearch(location=location, radius=radius, searchitems=searchitems)
    print(b)

if __name__ == "__main__":
    main()

    """
accounting
airport
amusement_park
aquarium
art_gallery
atm
bakery
bank
bar
beauty_salon
bicycle_store
book_store
bowling_alley
bus_station
cafe
campground
car_dealer
car_rental
car_repair
car_wash
casino
cemetery
church
city_hall
clothing_store
convenience_store
courthouse
dentist
department_store
doctor
electrician
electronics_store
embassy
establishment（サポート終了）
finance（サポート終了）
fire_station
florist
food（サポート終了）
funeral_home
furniture_store
gas_station
general_contractor（サポート終了）
grocery_or_supermarket（サポート終了）
gym
hair_care
hardware_store
health（サポート終了）
hindu_temple
home_goods_store
hospital
insurance_agency
jewelry_store
laundry
lawyer
library
liquor_store
local_government_office
locksmith
lodging
meal_delivery
meal_takeaway
mosque
movie_rental
movie_theater
moving_company
museum
night_club
painter
park
parking
pet_store
pharmacy
physiotherapist
place_of_worship（サポート終了）
plumber
police
post_office
real_estate_agency
restaurant
roofing_contractor
rv_park
school
shoe_store
shopping_mall
spa
stadium
storage
store
subway_station
synagogue
taxi_stand
train_station
transit_station
travel_agency
university
veterinary_care
zoo
      """
