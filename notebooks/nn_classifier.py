import torch
import torch.nn as nn
import torch.nn.functional as F

class NNClassifier(nn.Module):
    def __init__(self):
        super(NNClassifier, self).__init__()
        self.hidden1 = nn.Linear(8, 12)
        self.hidden2 = nn.Linear(12, 8)  
        self.output = nn.Linear(8, 1)    

    def forward(self, x):
        x = F.relu(self.hidden1(x)) 
        x = F.relu(self.hidden2(x))  
        x = torch.sigmoid(self.output(x))  
        return x
