class Room():
    id_count = 0
    def __init__(self):
        self.__reservation = []
        self.__id = Room.id_count

        Room.id_count += 1