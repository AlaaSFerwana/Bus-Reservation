class Bus:
    def __init__(self,BusNo,Allseats,Availseat,Bookedseat,From,To):
        self.__BusNo=BusNo
        self.__Allseats=Allseats
        self.__Availseat=Availseat
        self.__Bookedseat=Bookedseat
        self.__From=From
        self.__To =To
        self.__lst = [0] * Allseats

    def getList(self):
        return self.__lst

    def setBusNo(self, lst):
        self.__lst = lst

    def getBusNo(self):
        return self.__BusNo

    def setBusNo(self, BusNo):
        self.__BusNo = BusNo
    def getAllseats(self):
        return self.__Allseats
    def setAllseats(self,Allseats):
         self.__Allseats=Allseats
    def getAvailseat(self):
        return self.__Availseat
    def setAvailseat(self,Availseat):
        self.__Availseat=Availseat
    def getBookedseat(self):
        return self.__Bookedseat
    def setBookedseat(self,Bookedseat):
        self.__Bookedseat=Bookedseat
    def getFrom(self):
        return self.__From
    def setFrom(self,From):
        self.__From=From
    def getTo(self):
        return self.__To
    def setTo(self,To):
        self.__To=To





###############
#obj1=Bus(1,20,30,"Gaza","Rafah")
#print(obj1.getBusNo())
#obj1.setBusNo(2)
#print(obj1.getBusNo())
#print(obj1.getAvailseat())
#obj1.setAvailseat(14)
#print(obj1.getAvailseat())
#obj1.setTo("deer")
#print(obj1.getTo())