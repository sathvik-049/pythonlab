li = ['inches','yards','miles','millimetres','centi_meters','meters','kilo_meters']
val = [12, 1/3, 1/1580, 304.8, 30.48, 0.3048, 0.0003048]
while True:
    n =int(input("enter length in feet: "))
    conversion = int(input("1.inches\n2.yards\n3.miles\n4.millimetres\n5.centimeters\n6.meters,\n7.kilometers\nenter the conversion: "))

    match conversion:
        case 1:
            print(f"Length from feet to {li[0]}:{n*val[0]}")
        case 2:
            print(f"Length from feet to {li[1]}:{n*val[1]}")
        case 3:
            print(f"Length from feet to {li[2]}:{n*val[2]}")
        case 4:
            print(f"Length from feet to {li[3]}:{n*val[3]}")
        case 5:
            print(f"Length from feet to {li[4]}:{n*val[4]}")
        case 6:
            print(f"Length from feet to {li[5]}:{n*val[5]}")
        case 7:
            print(f"Length from feet to {li[6]}:{n*val[6]}")
        case _:
            break
