class Payment():
    transcation_count = 0
    def __init__(self, price, create_on):
        self._price = price
        self._create_on = create_on
        self._transaction_id = Payment.transcation_count
    
class CreditPayment(Payment):
    def __init__(self, price, create_on, name_on_card, card_number, expire_date, cvv):
        super().__init__(price, create_on)
        self.__name_on_card = name_on_card
        self.__card_number = card_number
        self.__expire_date = expire_date
        self.__cvv = cvv
    
class DebitPayment(Payment):
    def __init__(self, price, create_on, name_on_card, card_number, expire_date, cvv):
        super().__init__(price, create_on)
        self.__name_on_card = name_on_card
        self.__card_number = card_number
        self.__expire_date = expire_date
        self.__cvv = cvv
        