#ver.1
import numpy as np
class LunerRegression:
    x = None
    theta = None
    y = None

    def fit(self,x,y):
        pass

    def preddict(self,x):
        pass

    def score(self,x,y):
        pass

    #ver.2

    def fit(self,x,y):
        temp = np.linalg.inv(np.dot(x.T,x))
        self.theta = np.dot(np.dot(temp,x.T),y)

    #ver.3
    def preddict(self,x):
        return np.dot(x,self.theta)
    
    #ver.4
    def score(self,x,y):
        error = self.preddict(x) - y
        return (error**2).sum()