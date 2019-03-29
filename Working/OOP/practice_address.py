class Address(object):
    """
    A class modelling a street address
    """

    def __init__(self):
        self.address_line1 = ""
        self.address_line2 = ""
        self.postal_code = ""
        self.city = ""
        self.province = ""
        self.country = "Canada"


def main():

    home_address = Address()
    home_address.address_line1 = "123 Apple street"
    home_address.address_line2 = ""
    home_address.postal_code = "L3T 3X6"
    home_address.city = "Thornhill"
    home_address.province = "Ontario"

    work_address = Address()
    work_address.address_line1 = "456 Apple street"
    work_address.address_line2 = ""
    work_address.postal_code = "L3T 4X7"
    work_address.city = "Thornhill"
    work_address.province = "Ontario"


main()


