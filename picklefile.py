import pickle

#write pickle to memory
with open('abc.pkl','wb') as f:
    pickle.dump(lr,f)
    
    #read abc.pkl back to memory
    
with open('abc.pkl','rb') as f:
    lr = pikle.load(f)