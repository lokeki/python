'''
def ProcessInvoice(netto, brutto):
    if netto >= brutto:

        raise ValueError("Netto should be lover or equal to brutto")

    else:
        print("Procesing invoice.")


def EndOfMonth():

    netto = 1230
    brutto = 10000

    try:

        ProcessInvoice(netto, brutto)

    except ValueError as e:

        print("The values on invoice are incorrect: {}".format(e))
        raise ValueError("Error when processing invoices") from e

    except Exception as e:

        print("Error processing invoice: {}".format(e))
        raise Exception("General error when processing invoices")

EndOfMonth()
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
    def publishOffer(cls, listWithTrip):
        listOfErrors = []
        for trip in listWithTrip:

            try:
                trip.check_data()

            except ValueError as e:
                listOfErrors.append("{} : {} \n".format(trip.symbol, e))

            except Exception as e:
                listOfErrors.append("{} : {} \n".format(trip.symbol, e))

        if len(listOfErrors) > 0:
            raise Exception("The list of trips has errors: \n {}".format(listOfErrors))
        
        else:
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
