class Address:
    def __init__(self, street, city, state, postcode, street2=''):
        self.street = street
        self.street2 = street2
        self.city = city
        self.state = state
        self.postcode = postcode

    def __str__(self):
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f"{self.city}, {self.state}, {self.postcode}")
        return "\n".join(lines)

class AddressBook:
    def __init__(self):
        self._employee_addresses = {
            1: Address("121 Admin Road", "Concord", "London", "CN1 2BT"),
            2: Address("67 Paperwork Avenue", "Hounslow", "London", "TW2 2XY"),
            3: Address("15 Rose Street", "Twickenham", "London", "TW7 7BW"),
            4: Address("39 Sole Road", "Ealing", "London", "W4 7BM"),
            5: Address("45 main street", "Barking", "London", "E23 7CD")
        }

    def get_employee_address(self, employee_id):
        address = self._employee_addresses.get(employee_id)
        if not address:
            raise ValueError(employee_id)
        return address