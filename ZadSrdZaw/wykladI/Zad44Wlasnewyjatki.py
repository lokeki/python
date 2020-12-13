'''
class BITExcption(Exception):

    def __init__(self, text, area):
        super().__init__(text)
        self.area = area

    def __str__(self):
        return "{}, area {}".format(super().__str__(), self.area)

class BITSecurityException(BITExcption):
    pass

class BITDataFormatException(BITExcption):
    pass

try:
    # do anything
    raise BITExcption("file format is incoreect", "Financial data")

except BITSecurityException as e:
    print("Application security error {}".format(e))

except BITDataFormatException as e:
    print("Application data error {}".format(e))

except BITExcption as e:
    print("Application error {}".format(e))

except Exception as e:
    print("General error {}".format(e))
'''

import datetime as dt


class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end

    def check_data(self):
        if len(self.title) == 0:
            raise Exception("Title is empty!")
        if self.start > self.end:
            raise ValueError("Start date is later than end date!")

    @classmethod
    def publish_offer(cls, trips):

        list_of_errors = []

        for trip in trips:
            try:
                trip.check_data()
            except ValueError as e:
                list_of_errors.append("{}: {}".format(trip.symbol, str(e)))
            except Exception as e:
                list_of_errors.append("{}: {}".format(trip.symbol, str(e)))

        if len(list_of_errors) > 0:
            raise Exception("The list of trips has errors: {}".format(list_of_errors))
        else:
            print('the offer will be published...')

class TripException(Exception):

    def __init__(self, text, description):
        super().__init__(text)
        self.description = description

    def __str__(self):

        return "{}, Description: {}".format(super().__str__(), self.description)

class TripNameException(TripException):

    def __init__(self, text):
        super().__str__(text, 'Name of the trip is missing. You need to name the trip somehow...')


trips = [
    Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
    Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
    Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
]

try:
    print('Publishing trips...')
    Trip.publish_offer(trips)
    print('... done')
except Exception as e:
    print('THERE ARE ERRORS')
    print(e)
    print('THE OFFER CANNOT BE PUBLISHED')