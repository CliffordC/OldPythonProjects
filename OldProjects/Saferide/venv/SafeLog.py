class SafeLog:
    """This class creates a file that will be used to
    save data for a given day's 'saferides' """

    def __init__(self, filename, listOfRides):
        """ Constructor for the Class """
        self.filename = filename
        self.listOfRides = listOfRides
        self.makefile(filename,listOfRides)


    def makefile(self, filename, listOfRides ):
        #file = open(filename, "w")
        file = open("~/Users/cliffordchi/Documents/ " + filename, "w+")
        n = 0
        for word in listOfRides:
            if n % 3 == 0:
                file.write(word + "\n")
            else:
                file.write(word)

        file.close()


class DataForLogs:
    """ This class collects data for a given days
    Saferide trips"""

    date = " "

    def __init__(self):
        self.date = "date"
        self.getData()



    def getData(self):
        date = input("Hello, please enter the date. Format (00/00/0000)\n")
        pick_up_loc = input("What is the pickup location?\n")
        drop_up_loc = input("What is the drop off location?\n")
        listInfo = []
        listInfo.append(date)
        listInfo.append(pick_up_loc)
        listInfo.append(drop_up_loc)
        self.makeTheFile(date, listInfo)

    def makeTheFile(self, name, list):
        mk = SafeLog(name,list)


def main():
    DataForLogs()

if __name__ == "__main__":
    main()
