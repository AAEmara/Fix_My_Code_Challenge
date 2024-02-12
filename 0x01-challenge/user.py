#!/usr/bin/python3
"""user module that contains User class."""


class User():
    """ User Class. """

    def __init__(self):
        """ Initializng the User's Class attributes. """
        self.__email = None

    @property
    def email(self):
        """ Returning the value of the email attribute. """
        return self.__email

    @email.setter
    def email(self, value):
        """ Giving an interface to set the email attribute. """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":
    """User Class Testing."""
    u = User()
    u.email = "john@snow.com"
    print(u.email)
