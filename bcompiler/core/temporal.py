import datetime


class FinancialYear:
    def __init__(self, year):
        if isinstance(year, int) and (year in range(150, 2100)):
            self.year = year
        else:
            raise ValueError("A year must be an integer between 1950 and 2100")
        self._generate_quarters()
        self._q1 = self.quarters[0]
        self._q2 = self.quarters[1]
        self._q3 = self.quarters[2]
        self._q4 = self.quarters[3]

        self.start_date = self.q1.start_date
        self.end_date = self.q4.end_date

    @property
    def q1(self):
        return self._q1

    @property
    def q2(self):
        return self._q2

    @property
    def q3(self):
        return self._q3

    @property
    def q4(self):
        return self._q4

    def __str__(self):
        return f"FY{str(self.year)}/{str(self.year + 1)[2:]}"

    def _generate_quarters(self):
        self.quarters = [Quarter(x, self.year) for x in range(1, 5)]



class Quarter:

    start_months = {
        1: (4, 'April'),
        2: (7, 'July'),
        3: (10, 'October'),
        4: (1, 'January')
    }

    end_months = {
        1: (6, 'June', 30),
        2: (9, 'September', 30),
        3: (12, 'December', 31),
        4: (3, 'March', 31),
    }

    def __init__(self, quarter: int, year: int):


        if isinstance(quarter, int) and (quarter >= 1 and quarter <= 4):
            self.quarter = quarter
        else:
            raise ValueError("A quarter must be either 1, 2, 3 or 4")

        if isinstance(year, int) and (year in range(1950, 2100)):
            self.year = year
        else:
            raise ValueError("Year must be between 1950 and 2100 - surely that will do?")

        self.start_date = self._start_date(self.quarter, self.year)
        self.end_date = self._end_date(self.quarter, self.year)

    def __str__(self):
        return f"Q{self.quarter} {str(self.year)[2:]}/{str(self.year + 1)[2:]}"

    def _start_date(self, q, y):
        if q == 4:
            y = y + 1
        return datetime.date(y, Quarter.start_months[q][0], 1)

    def _end_date(self, q, y):
        if q == 4:
            y = y + 1
        return datetime.date(y, Quarter.end_months[q][0], Quarter.end_months[q][2])

    def __repr__(self):
        return f"Quarter({self.quarter}, {self.year})"

    @property
    def fy(self):
        return FinancialYear(self.year)