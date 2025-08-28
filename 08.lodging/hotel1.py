def read_hotels_file(file_name):
    #open,read and convert first fillr to dinctionary
    try:
        hotels = {}
        with open(file_name) as file:
            for line in file:
                hotel_name,hotel_id,number_of_rooms,price = line.strip().split(":")
                hotels[hotel_id] = {"hotel name":hotel_name,"number of rooms":int(number_of_rooms),"free_rooms":int(number_of_rooms)}
        return hotels

    except OSError as err:
        print(err)

def read_booking_file(file_name):
    #open,read and convert second file to matrix
    try:
        bookings = []
        with open(file_name) as file:
            f = file.read().split("\n")
            for line in f:
                line = line.split()
                line[-1] = int(line[-1])
                bookings.append(line)
        
        return bookings

    except FileNotFoundError as err:
        print(err)

def process(hotels,bookings):

    confirmed = 0
    unconfirmed = 0
    unconfirmed_id = None
    hotel_with_max_free_rooms = None
    max_free_rooms = 0
    
    #find the outputs 

    for i in range(len(bookings)):
        booking_id = bookings[i][0]
        name_of_hotel = bookings[i][1]
        requested_rooms = bookings[i][2]
        
        if name_of_hotel not in hotels:
            continue
        
        elif name_of_hotel in hotels:
            if hotels[name_of_hotel]['free_rooms'] >= requested_rooms:
                hotels[name_of_hotel]['free_rooms'] -= requested_rooms
                confirmed += 1
            else:
                unconfirmed  += 1
                unconfirmed_id = booking_id
        
        if  hotels[name_of_hotel]['free_rooms'] >= max_free_rooms:
            max_free_rooms = hotels[name_of_hotel]['free_rooms']
            hotel_with_max_free_rooms = hotels[name_of_hotel]["hotel name"]

    
    #print result
    
    print("Unconfirmed booking: ",unconfirmed_id)
    print(f"Confirmed bookings: {confirmed} - Unconfirmed bookings: {unconfirmed}")
    print()
    print("Hotel status:")
    for key,value in hotels.items():
        print(f"    {value['hotel name']}: {value['number of rooms']} rooms ({value['free_rooms']} free)")
    print()
    print("Hotel with more free rooms: ",hotel_with_max_free_rooms)


def main():

    hotels = read_hotels_file("hotels.txt")
    
    bookings = read_booking_file("bookings.txt")
    
    process(hotels,bookings)

if __name__ == "__main__":
    main()