from bus import Bus
print("***  Welcome Dear Customer in Buses Booking company   ***")
print("-"*50)
Customer_Name=(input("Enter your Name : " ))
#Customer_Password=input("Enter Your Password : ")

class Busreservation():

      def chooseBus(self,choice):
        if choice == '1':
            Busreservation().book(bus1)
        elif choice == '2':
            Busreservation().book(bus2)
        else:
           print("No Bus Found ")

      def book(self, busType):
           availabelseat = busType.getAvailseat()
           totalseats=busType.getAllseats()
           bookedseat=busType.getBookedseat()
           if totalseats == bookedseat:
               print("Sorry, No Seat Available ")
           else:
             busType.setAvailseat(availabelseat-1)
             busType.setBookedseat(bookedseat+1)
             lst=busType.getList()
             for i in range(len(lst)):
                 seatNum=i+1
                 if lst[i] == 0:
                    lst[i] = "B"
                    break
             print("Thanks", Customer_Name, "!! Your seat has been booked successfully, your specific seat number is",seatNum ,'\n')
            # print(lst)
             inputi=input("Do You want to book another seat? Enter Y:N ")
             if inputi == 'Y' or inputi == 'y':
              inputNum = input("Please, Enter bus number again:  ")
              Busreservation.chooseBus(self,inputNum)
             else:
                 print('Thanks for you')


bus1 = Bus(1, 30,30, 0, "Gaza", "Rafah")
bus2 = Bus(2, 50, 50, 0, "Gaza", "Rimal")
print('\n')
print("_____________Buses And Their Destinations_____________\n")
print("   Bus Type""    ""Total Seats""     ""Available Seats""   ""Booked Seats""    ""From""    ""-""    ""To \n")
print("     ", bus1.getBusNo(),"         ",bus1.getAllseats(),"              ",bus1.getAvailseat(),"              ",bus1.getBookedseat(),"        ",bus1.getFrom(),"     ",bus1.getTo())
print("     ", bus2.getBusNo(), "         ", bus2.getAllseats(), "              ", bus2.getAvailseat(),"              ", bus2.getBookedseat(), "        ", bus2.getFrom(), "     ", bus2.getTo() )




choice= input("To book any free seat, Enter bus number: ")
Busreservation().chooseBus(choice)







