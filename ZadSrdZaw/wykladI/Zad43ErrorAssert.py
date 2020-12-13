'''
import datetime

netto = 1000
brutto = 120
# netto must be less or equal to brutto

assert netto <= brutto, "Netto can't be greater than brutto"


orderDate = datetime.date(2022, 10, 13)
deliveryDate = datetime.date(2022, 10, 18)
# order data should be earlier than the delivery date

assert orderDate <= deliveryDate, "Order date con't be later than delivery date"
'''

import datetime as dt


class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end

    def check_data(self):
        assert len(self.title) > 0, "Title is empty!"
        assert self.start <= self.end, "Start date is later than end date!"

    @classmethod
    def publishOffer(cls, listWithTrip):
        listOfErrors = []
        for trip in listWithTrip:

            try:
                trip.check_data()

            except ValueError as e:
                listOfErrors.append("{} : {} \n".format(trip.symbol, e))

            except Exception as e:
                listOfErrors.append("{} : {} \n".format(trip.symbol, e))

        assert listOfErrors == 0,"The list of trips has errors: \n {}".format(listOfErrors)
        print("The offer will be published...")


trips = [
    Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
    Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
    Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
]

try:
    print("Start check a offer")
    Trip.publishOffer(trips)
    print("Done")

except Exception as e:
    print("Error: {}".format(e))
