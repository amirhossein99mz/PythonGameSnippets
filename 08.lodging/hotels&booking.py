def readHotel(hotel_file):
    try:
        
        f = open(hotel_file)
    except OSError as e:
        print(f"The error is {e}")
    
    file = f

    hotels = {}

    for line in file:
        
        hotel_name,hotel_id,number_of_rooms,price = line.strip().split(":")
        hotels[hotel_id] = {"name":hotel_name,"num_rooms":int(number_of_rooms),"num_free_rooms":int(number_of_rooms)}
    
    f.close()
    
    return hotels


def readbookingfile(booking_file):
    try:
        f = open(booking_file)
    except FileNotFoundError as e:
        print(f"The second error is {e}")
    
    file = f.read().split("\n")

    f.close()

    bookings = []

    for line in file:
        line = line.split()
        line[2] = int(line[2])
        bookings.append(line)
    
    #line[0] = booking_id
    #line[1] = hotel_id
    #line[2] = requested_rooms
        
    return bookings

def Process(hotels,bookings):

    print()

    confirmed_bookings = 0

    unconfirmed_bookings = 0

    max_free_room = 0
    
    max_free_room_hotel = None


    for line in bookings:

        booking_id  = line[0]

        hotel_id = line[1]
        
        requested_rooms = line[2]
    
        if hotel_id in hotels and hotels[hotel_id]['num_free_rooms'] > requested_rooms :
            hotels[hotel_id]['num_free_rooms'] -= requested_rooms
            confirmed_bookings += 1
        
        else:
            unconfirmed_bookings +=1

        if hotels[hotel_id]['num_free_rooms'] > max_free_room:

            max_free_room = hotels[hotel_id]['num_free_rooms']

            max_free_room_hotel  = hotels[hotel_id]['name']
            
        
    print(f"Unconfirmed booking : {booking_id}")

    print(f"Confiemd bookings:{confirmed_bookings} - unconfiemd_bookings:{unconfirmed_bookings}")
    print()
    print("Hotel status:")

    for key,value in hotels.items():

        print(f"     {value['name']} : {value['num_rooms']} ({value['num_free_rooms']} free)")
    print()
    
    print(f"Hotel with more free rooms: {max_free_room_hotel}")

    
    


def main():

    hotels = readHotel("C:/Users/javan/OneDrive/Desktop/program/7/hotels.txt")
    
    bookings = readbookingfile("C:/Users/javan/OneDrive/Desktop/program/7/bookings.txt")
    
    Process(hotels,bookings)

if __name__ == "__main__":

    main()

