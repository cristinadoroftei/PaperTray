class Machine:

    def __init__(self, modelnumber):
        self.__modnr = modelnumber
        self.__power = False

    @property
    def modnr(self):
        return self.__modnr
    
    @modnr.setter 
    def modnr(self, modnr):
        self.__modnr = modnr
    
    @property
    def power(self):
        return self.__power
    
    @power.setter 
    def power(self, value):
        self.__power = value


class Printer(Machine):
    def __init__(self, modelnumber, papertray):
        super().__init__(modelnumber)
        self.papertray = papertray
       # Machine.__init__(self,modelnumber)
    
    @property
    def papertray(self):
        return self.__papertray
    
    @papertray.setter 
    def papertray(self, papertray):
        self.__papertray = papertray

    def printToConsole(self, attr):
        if self.power == True:
            self.papertray.checkPaper() 
            print("Cristina is beautiful " + attr)
            self.papertray.paper -= 1
        else:
            print("Pls turn me on.", end='')
            print("Do you want to turn me on? y/n:", end='')
            if input() == 'y':
                self.power = True



class Papertray:
    def __init__(self, paper):
        self.__paper = paper
    
    @property
    def paper(self):
        return self.__paper
    
    @paper.setter 
    def paper(self, paper):
        self.__paper = paper
    
    def checkPaper(self):
        if(self.__paper == 0):
            self.__paper = int(input('Papertray out on pap3r.\n How many pages of pap3r do you n33d:'))
        
    
