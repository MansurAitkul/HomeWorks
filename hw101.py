class MainClass:
    def __init__(self, text):
        self.text_field = text

    def set_text(self, text=None):
        if text is not None:
            self.text_field = text
        else:
            self.text_field = ""

class ChildClass(MainClass):
    def __init__(self, text, number):
        super().__init__(text)
        self.number_field = number


main_obj = MainClass("Hello")
print(main_obj.text_field)  

main_obj.set_text("World")
print(main_obj.text_field)  

main_obj.set_text()
print(main_obj.text_field)  

child_obj = ChildClass("Inheritance", 42)
print(child_obj.text_field)  
print(child_obj.number_field)  

########

class MainClass:
    def __init__(self, text):
        self._text_field = text

    def set_text(self, text=None):
        if text is not None:
            self._text_field = text
        else:
            self._text_field = ""

    def print_info(self):
        print("Text:", self._text_field)


class ChildClass(MainClass):
    def __init__(self, text, number):
        super().__init__(text)
        self._number_field = number

    def print_info(self):
        super().print_info()
        print("Number:", self._number_field)


    obj.print_info()


main_obj = MainClass("Hello")
child_obj = ChildClass("Inheritance", 42)

process_object(main_obj)
process_object(child_obj)

#####

class Roman:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Roman):
            return Roman(self.value + other.value)
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, Roman):
            return Roman(self.value - other.value)
        else:
            raise TypeError("Unsupported operand type for -")

    def __mul__(self, other):
        if isinstance(other, Roman):
            return Roman(self.value * other.value)
        else:
            raise TypeError("Unsupported operand type for *")

    def __truediv__(self, other):
        if isinstance(other, Roman):
            return Roman(self.value // other.value)
        else:
            raise TypeError("Unsupported operand type for /")

    @staticmethod
    def to_roman(number):
        pass

    @staticmethod
    def from_roman(roman_number):
        pass



roman1 = Roman(10)
roman2 = Roman(5)


result_add = roman1 + roman2
result_sub = roman1 - roman2
result_mul = roman1 * roman2
result_div = roman1 / roman2


print(result_add.value)  #Вывод 15
print(result_sub.value)  #Вывод 5
print(result_mul.value)  # ывод 50
print(result_div.value)  #Вывод 2

#######

import sqlite3

class Ticket:
    def __init__(self, destination, price, date):
        self.destination = destination
        self.price = price
        self.date = date

class TicketRegistrationBot:
    def __init__(self):
        self.available_tickets = []
        self.registered_tickets = []

    def fetch_available_tickets(self):
        conn = sqlite3.connect('tickets.db')
        cursor = conn.cursor()

        cursor.execute("SELECT destination, price, date FROM tickets")

        rows = cursor.fetchall()

        for row in rows:
            ticket = Ticket(row[0], row[1], row[2])
            self.available_tickets.append(ticket)

        conn.close()

    def display_available_tickets(self):
        print("Available Tickets:")
        for index, ticket in enumerate(self.available_tickets, start=1):
            print(f"{index}. Destination: {ticket.destination} | Price: {ticket.price} | Date: {ticket.date}")


bot = TicketRegistrationBot()

bot.fetch_available_tickets()

bot.display_available_tickets()
