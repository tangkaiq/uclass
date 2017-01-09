import random

class Seat:
    '''An airplane seat'''
    
    # The Seat class is optional and you can implement the reservation system 
    # without it. But it makes the main ReservationClass neater and easier.
    
    def __init__(self, seat_name, class_type):
        ''''(Seat, str, str) '''
        
        self.name = seat_name
        self.class_type = class_type
        self.reserved = False

    #Like __str__
    def __repr__(self):
        '''(Seat) -> str''' 
        
        return 'Seat {0} {1}'.format(self.name, self.class_type)
    
    
class ReservationSystem:
    '''An airline reservation system'''
    
    def __init__(self, business_seats, economy_seats):
        '''(ReservationSystem, list of Seats, list of Seats)'''
        
        self.all_b_seats = business_seats[:]
        self.all_e_seats = economy_seats[:]        

        self.vacant_b_seats = business_seats[:]
        self.vacant_e_seats = economy_seats[:]
        
        self.reserved_b_seats = []
        self.reserved_e_seats = []
        
        self.booking_ids = []
        
        
    def make_reservation(self, preference):
        '''(ReservationSystem, str) -> str
        
        Book a random seat in the given preference class and return the seat 
        number and booking id if booking is successful. Otherwise, return an
        error message.
        '''
        
        #generate a random booking id
        booking_id = ''.join(random.choice('123456789ABCDEF') for i in range(4))
        while booking_id in self.booking_ids:
            booking_id = ''.join(random.choice('123456789ABCDEF') for i in range(4))
        
        if preference == "business" and self.vacant_b_seats != []:
            seat = self.vacant_b_seats.pop(0)
            seat.class_type = "business"
            seat.reserved = True
            self.reserved_b_seats.append(seat) 
            print( "You have successfully reserved seat " + str(seat) + ". Your\
            reservation id is: " + booking_id)
        
        elif preference == "economy" and self.vacant_e_seats != []:
            seat = self.vacant_e_seats.pop(0)
            seat.class_type = "economy"
            seat.reserved = True
            self.reserved_e_seats.append(seat)   
            print( "You have successfully reserved seat " + str(seat) + ". Your\
            reservation id is: " + booking_id)
        
        else:
            print( "Reservation was unsuccessful as no seats are avaiable for \
            the specified preference")     
        
        
    def get_reservation_percentage(self, seat_class):
        '''(ReservationSystem, str) -> str
        
        Return the percentage of seats booked in the specified seat_class
        
        Precondition: seat_class has one of three values: "all", "economy", 
        oe "business"
        '''
        
        if seat_class == "all":
            num = len(self.reserved_b_seats)+len(self.reserved_e_seats)
            denom = len(self.all_b_seats)+len(self.all_e_seats)
            
        elif seat_class == "business":
            num = len(self.reserved_b_seats)
            denom = len(self.all_b_seats)
            
        else:
            num = len(self.reserved_e_seats)
            denom = len(self.all_e_seats)

        return str(num/denom*100) + "%"

    
    
    def __repr__(self):
        '''(ReservationSystem) -> str'''
        
        aircraft = ""
        for seat in self.all_b_seats:
            aircraft += str(seat) + (" Reserved" if seat.reserved else " Avaialble")
            aircraft +=   "\n"

        for seat in self.all_e_seats:
            aircraft += str(seat) + (" Reserved" if seat.reserved else " Avaialble")
            aircraft +=   "\n"
            
        return aircraft[:-1]
    

if __name__ == "__main__":
    
    business_seats = [Seat('1A', 'business'), Seat('1B', 'business'), \
                  Seat('1C', 'business'), Seat('1D', 'business')]
    
    economy_seats = [Seat('2A', 'economy'), Seat('2B', 'economy'), \
                     Seat('2C', 'economy'), Seat('2D', 'economy'), \
                     Seat('3A', 'economy'), Seat('3B', 'economy'), \
                     Seat('3C', 'economy'), Seat('3D', 'economy')]
    
    reservation_system = ReservationSystem(business_seats, economy_seats)

    '''
    reservation_system.make_reservation("business")
    reservation_system.make_reservation("economy")
    reservation_system.make_reservation("economy")
    reservation_system.make_reservation("economy")
    reservation_system.make_reservation("business")
    '''

    #make sure you type something like "business"
    while(1):
        
        c=input("type seat class \n")
        reservation_system.make_reservation(c)


    
        print("Percentage of booked seats: ", \
          reservation_system.get_reservation_percentage("all"))
    
        print("Percentage of booked business seats: ", \
          reservation_system.get_reservation_percentage("business"))
    
        print("Percentage of booked economy seats: ", \
          reservation_system.get_reservation_percentage("economy"))
    
