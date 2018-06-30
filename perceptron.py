

class Perceptron:

    #Konstruktør
    def __init__(self,features,actual_class):
        self._features = features
        self._actual_class = actual_class
        self.antall_features = self.antallFeatures()
        self._weights = [[0]*self.antall_features]*len(self._features)

        #Lager konstant
        for i in range(len(self._weights)):
            self._weights[i][0] = 1

    #Beregner index for ett perseptron
    def perceptron(self,unit):
        l_class = 0
        for i in range(len(self._weights)):
            l_class += self._weights[unit][i]*self._features[unit][i]
        return l_class

    #Oppdaterer vekter
    def update_weights(self,unit):
        predicted_class = self.perceptron(unit)
        for i in range(len(self._weights)):
            self._weights[unit][i] = self._weights[unit][i] + (self._actual_class[unit]-predicted_class)*self._features[unit][i]

    def update_all(self):
        for i in range(len(self._actual_class)):
            self.update_weights(i)

    #Beregner sum_feil
    def sum_error(actual_vector,predicted_vector):
        sum_ = 0



    #Printer ut
    def skrivUt(self):
        print("Features",self._features)
        print("Weights",self._weights)

    #Beregner antall features
    def antallFeatures(self):
        temp_features = [self._features]
        feat_no = 0
        i = 0
        while True:
            try:
                self._features[0][i]
                i += 1
            except:
                return i

#tester
test1 = Perceptron(([[10,3,2,4],[5,5,3,6]]),([0,1]))
assert test1.antallFeatures() == 4

test1.update_all()
test1.skrivUt()
