import numpy as np
trainingData = [
    [2,2,1,2],  
    [2,2,1,1],  
    [2,2,0,2],  
    [2,1,1,2],  
    [1,1,1,2],  
    [1,2,1,1],  
    [1,0,0,1],  
    [1,0,1,0],  
    [2,1,1,1],  
    [2,0,1,2],  
    [0,0,0,0],  
    [0,0,0,1],  
    [0,0,0,2],  
    [0,1,0,1],  
    [0,0,1,0],  
    [0,0,0,0],  
    [0,0,0,0],  
    [1,0,0,0],  
    [2,0,0,0],  
    [2,2,1,2],  
]
labels= [3,3,3,3,2,2,2,2,2,2,1,1,1,1,1,0,0,1,2,3]
class ANN:
    def __init__(self):
        """Initialize netwrok with Random weights"""
        self.w1=np.random.randn(4,8)*0.1
        self.w2=np.random.randn(8,6)*0.1
        self.w3=np.random.randn(6,4)*0.1
        self.b1=np.zeros((1,8))
        self.b2=np.zeros((1,6))
        self.b3=np.zeros((1,4))
    def relu(self,x):
        """Activation Function"""
        return np.maximum(0,x)
    def softmax(self,x):
        """Output activation - probolities"""
        expX=np.exp(x-np.max(x))
        return expX/expX.sum()
    def forward(self,x):
        """Forward pass through netword"""
        self.z1=np.dot(x,self.w1)+self.b1
        self.a1=self.relu(self.z1)
        self.z2=np.dot(self.a1,self.w2)+self.b2
        self.a2=self.relu(self.z2)
        self.z3=np.dot(self.a2,self.w3)+self.b3
        self.a3 = self.softmax(self.z3)
        return self.a3
    def train(self, X, y, epochs=1000, lr=0.01):
        """Train network using backpropagation
        X = input data
        y = labels
        epochs = kitni baar train karo
        lr = learning rate
        """
        for epoch in range(epochs):
            totalLoss=0
            for i in range(len(X)):
                inputData=X[i].reshape(1, -1)
                output=self.forward(inputData)
                target=np.zeros((1, 4))
                target[0][y[i]]=1
                loss=-np.sum(target*np.log(output+1e-8))
                totalLoss+=loss
                d3=output-target
                dw3=np.dot(self.a2.T,d3)
                db3=d3
                d2=np.dot(d3,self.w3.T)*(self.a2>0)
                dw2=np.dot(self.a1.T,d2)
                db2=d2
                d1=np.dot(d2,self.w2.T)*(self.a1>0)
                dw1=np.dot(inputData.T,d1)
                db1=d1
                self.w3-=lr*dw3
                self.b3-=lr*db3
                self.w2-=lr*dw2
                self.b2-=lr*db2
                self.w1-=lr*dw1
                self.b1-=lr*db1
            if epoch % 100 == 0:
                print(f"Epoch {epoch} Loss: {totalLoss:.4f}")
    def predict(self,x):
        """
        Predict priority for new input
        Returns: priority label
        """
        inputData=np.array(x).reshape(1,-1)
        output=self.forward(inputData)
        priorityMap={0:"Low",1:"Normal",2:"High",3:"Critical"}
        return priorityMap[np.argmax(output)]
vehicleMap = {
    "Ambulance":2,"Fire Truck":2,
    "Police Car":1, "Car":0,
    "Bus":0,"Motorcycle":0
}
X=np.array(trainingData,dtype=float)
y = labels
model=ANN()
model.train(X,y)
severityMap={"High":2,"Medium":1,"Low":0,"None":0}
trafficMap={"High":2,"Medium":1,"Low":0}
def predictPriority(vehicle, severity, timeSensitive, traffic):
    """Main function to predict priority"""
    inputData = [
        vehicleMap[vehicle],
        severityMap[severity],
        1 if timeSensitive else 0,
        trafficMap[traffic]
    ]
    return model.predict(inputData)