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

    def print_address(self, addr):
        self.address_line1 = addr




street address line 1
street address line 2 (if it has a value)
city, province, postalcode
Counry