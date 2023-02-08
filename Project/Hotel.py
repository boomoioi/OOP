class Hotel():
    def __init__(self, hotel_name, facility, address, map, policies, nearby_place):
        self.__hotel_name = hotel_name 
        self.__facility = facility
        self.__address = address
        self.__map = map
        self.__policies = policies
        self.__nearby_place = nearby_place
        self.__room_types = []
        self.__comment = []
        self.__rating = []

