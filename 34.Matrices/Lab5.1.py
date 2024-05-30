#ATM and pin
#work with while without for

def ATM():
    attemp = 3
    correct_pin = 1234

    while attemp > 0:
        pin = int(input(f"Enter your pin:"))
        if pin != correct_pin:
            print(f"wrong pin (more{attemp-1} attemp)")
        else:
            print("correct pin")
            break

        attemp -= 1




ATM()