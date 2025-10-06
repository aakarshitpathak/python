from random import randint 

class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book (nik, fro, to):
        print(f"Ticket is booked in Train no: {nik.trainNo} from {fro} to {to} ")

    def getStatus(self):
       print(f"TrainNo: {self.trainNo} is running on time")   

    def getFare(self, fro , to):
        print(f"TIcket fare in TrainNo: {self.trainNo} from {fro} to {to} is {randint (222, 5555)} ") 


t= Train(11220)
t.book("Lucknow" , "Katra")
t.getStatus()
t.getFare("Lucknow" , "Katra")