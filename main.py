
class Auto():

    def __init__(self, barvy, motor, rok, karoserie, tachometr):
        self.barvy=barvy
        self.__motor=motor
        self.barvy=barvy
        self.__rok=rok
        self.__karoserie=karoserie
        self.tachometr=tachometr
    #Getter
    def get_motor(self):
        return self.__motor
    
    #Setter
    def set_motor(self, motor):
        self.__motor=motor
        return 


    def get_tachometr(self):
        return self.tachometr


    def lower_tachometr(self, percent):
        self.tachometr *= ((100-percent)/100)

    


        


if __name__=="__main__":

    auto1 = Auto("modra", "1.1",2019,"sedan", 150000)

    barvy = ["zluta", "modra", "fialova", "cervena"]
    motor = ["1.0", "1.4", "2.0", "1.7"]
    rok = [2000,2005,2010,2020]
    karoserie = ["sedan","limuzina", "combi","coupe"]
    for i in range(len(barvy)):
        print("auto ma barvu {}, motorizaci {}, rok vyroby {} a karoserii {}.".format(barvy[i],motor[i], rok[i], karoserie[i]))
    
    print(auto1.barvy)

    auto1.barvy = "zelena"
    print(auto1.barvy)

    print(auto1.get_motor())

    auto1.set_motor("2.0")
    print(auto1.get_motor())



    print(auto1.get_tachometr())
    auto1.lower_tachometr(50)
    print(auto1.get_tachometr())
