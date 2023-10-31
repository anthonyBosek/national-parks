import re


class NationalPark:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @classmethod
    def most_visited(cls):
        park_obj = None
        max_vis = 0
        for park in cls.all:
            if park.total_visits() > max_vis:
                park_obj = park
                max_vis = park.total_visits()
        return park_obj
        # return max(cls.all, key=lambda park: park.total_visits())

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_val):
        if not isinstance(new_val, str):
            raise TypeError("Park name must be of type String.")
        elif len(new_val) < 3:
            raise ValueError("Park name must be greater than 2 characters.")
        elif hasattr(self, "name"):
            raise AttributeError("Park name cannot be changed after birth.")
        else:
            self._name = new_val

    def trips(self):
        return [trip for trip in Trip.all if trip.national_park is self]

    def visitors(self):
        return list({trip.visitor for trip in self.trips()})

    def total_visits(self):
        return len(self.trips())

    def best_visitor(self):
        visitors = [trip.visitor for trip in self.trips()]
        return max(set(visitors), key=visitors.count)


class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        type(self).all.append(self)

    # use regex to check if date is in format "September 1st"
    def date_check(date):
        regex = r"^[A-Z][a-z]+ [0-9]+[a-z]{2}$"
        if re.search(regex, date):
            return True

    @property
    def visitor(self):
        return self._visitor

    @visitor.setter
    def visitor(self, new_val):
        if not isinstance(new_val, Visitor):
            raise TypeError("Visitor must be of type Visitor class.")
        else:
            self._visitor = new_val

    @property
    def national_park(self):
        return self._national_park

    @national_park.setter
    def national_park(self, new_val):
        if not isinstance(new_val, NationalPark):
            raise TypeError("National Park must be of type NationalPark class.")
        else:
            self._national_park = new_val

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, new_val):
        if not isinstance(new_val, str):
            raise TypeError("Start date must be of type String.")
        elif len(new_val) < 7:
            raise ValueError("Start date must be greater than 7 characters.")
        elif not Trip.date_check(new_val):
            raise ValueError("Start date must be in format 'September 1st'.")
        else:
            self._start_date = new_val

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, new_val):
        if not isinstance(new_val, str):
            raise TypeError("End date must be of type String.")
        elif len(new_val) < 7:
            raise ValueError("End date must be greater than 7 characters.")
        elif not Trip.date_check(new_val):
            raise ValueError("End date must be in format 'September 1st'.")
        else:
            self._end_date = new_val


class Visitor:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_val):
        if not isinstance(new_val, str):
            raise TypeError("Visitor name must be of type String.")
        elif not 1 <= len(new_val) <= 15:
            raise ValueError("Visitor name must be between 1-15 characters.")
        else:
            self._name = new_val

    def trips(self):
        return [trip for trip in Trip.all if trip.visitor is self]

    def national_parks(self):
        return list({trip.national_park for trip in self.trips()})

    def total_visits_at_park(self, park):
        return len([trip for trip in self.trips() if trip.national_park is park])
