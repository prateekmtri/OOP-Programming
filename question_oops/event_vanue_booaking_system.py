from abc import ABC, abstractmethod

class VenueBooking(ABC):
    def __init__(self, host_name, booking_id, rate_per_hour, hours_booked):
        self.host_name = host_name
        self.__booking_id = booking_id
        self.rate_per_hour = rate_per_hour
        self.hours_booked = hours_booked

    def get_booking_id(self):
        return self.__booking_id

    # NEW CONCEPT 1: Setter Validation (a simple if/else check)
    def set_hours_booked(self, hours_booked):
        if hours_booked > 0:
            self.hours_booked = hours_booked
        else:
            print("Invalid hours! Must be greater than 0.")

    def show_booking_details(self):
        print("Host Name:", self.host_name)
        print("Booking ID:", self.get_booking_id())
        print("Rate Per Hour:", self.rate_per_hour)
        print("Hours Booked:", self.hours_booked)
        print("Final Total:", self.calculate_total_cost())

    @abstractmethod
    def calculate_total_cost(self):
        pass


# No extra inputs needed -> No __init__ needed (just like before!)
class StandardHall(VenueBooking):
    def calculate_total_cost(self):
        return self.rate_per_hour * self.hours_booked


# NEW CONCEPT 2: Extra input (catering_fee) -> Needs __init__ and super()
class BanquetHall(VenueBooking):
    def __init__(self, host_name, booking_id, rate_per_hour, hours_booked, catering_fee):
        # Pass the 4 common values up to the Parent class
        super().__init__(host_name, booking_id, rate_per_hour, hours_booked)
        # Save the 1 extra value here in the Child class
        self.catering_fee = catering_fee

    def calculate_total_cost(self):
        combined_total = (self.rate_per_hour * self.hours_booked) + self.catering_fee
        if self.hours_booked >= 6:
            discount = combined_total * 10 / 100
            return combined_total - discount
        else:
            return combined_total


# Same pattern as BanquetHall, just with av_equipment_fee
class ConferenceHall(VenueBooking):
    def __init__(self, host_name, booking_id, rate_per_hour, hours_booked, av_equipment_fee):
        super().__init__(host_name, booking_id, rate_per_hour, hours_booked)
        self.av_equipment_fee = av_equipment_fee

    def calculate_total_cost(self):
        combined_total = (self.rate_per_hour * self.hours_booked) + self.av_equipment_fee
        gst = combined_total * 18 / 100
        return combined_total + gst


# --- Testing the code ---
obj1 = StandardHall("Prateek", 901, 2000, 4)
obj2 = BanquetHall("Shivam", 902, 3000, 6, 5000)
obj3 = ConferenceHall("Manish", 903, 2500, 4, 2000)

obj1.set_hours_booked(-2)   # Rejected by the if-check
obj1.set_hours_booked(5)    # Accepted

obj1.show_booking_details()
print()
obj2.show_booking_details()
print()
obj3.show_booking_details()