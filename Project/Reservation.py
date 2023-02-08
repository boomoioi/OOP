class Reservation():
    def __init__(self, check_in_date, check_out_date, hotel_name, room_type, refundble, price):
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__hotel_name = hotel_name
        self.__room_type = room_type
        self.__refundable = refundble
        self.__price = price