class Clock:
    """
    The clock class representing the time in both 12 hour h:mm:ss AM/PM
    and 24 hour hh:mm:ss
    """

    def __init__(self, hours, minutes, seconds):
        """
        Constructor
        :param hours: the initial hours
        :param minutes: the initial minutes
        :param seconds: the initial seconds
        """
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def add_hour(self):
        """
        Add an hour to the clock
        """
        if self.hours >= 23:
            self.hours = 0
        else:
            self.hours += 1

    def add_minute(self):
        """
        Add a minute to the clock
        """
        if self.minutes >= 59:
            self.minutes = 0
            self.add_hour()
        else:
            self.minutes += 1

    def add_second(self):
        """
        Add a second to the clock
        """
        if self.seconds >= 59:
            self.seconds = 0
            self.add_minute()
        else:
            self.seconds += 1

    def get_suffix(self):
        """
        Get the suffix
        """
        if self.hours < 12:
            suffix = 'AM'
        else:
            suffix = 'PM'

        return suffix

    def pad(self, value):
        """
        Pads a value as a two-digit representation.
        e.g. 9 is "09"
        :param value: the value to pad
        :return: the value as two-digits
        """
        if value <= 9:
            padded_value = '0' + str(value)
        else:
            padded_value = str(value)

        return padded_value

    def get_24_hour_format(self):
        """
        Get the 24-hour format: hh:mm:ss
        :return: the-24 hour format
        """
        format24 = self.pad(self.hours) + ":" + self.pad(self.minutes) + ":" + self.pad(self.seconds)

        return format24

    def get_12_hour_format(self):
        """
        Get the 12-hour format: h:mm:ss AM/PM
        :return: the-12 hour format
        """
        display_hours = self.hours
        if display_hours == 0:
            display_hours = 12
        elif display_hours > 12:
            display_hours -= 12

        format12 = str(display_hours) + ":" + self.pad(self.minutes) + ":" + self.pad(self.seconds) + " " + self.get_suffix()

        return format12
