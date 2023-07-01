import numpy as np
import streamlit as st 
import pickle
import sklearn
import joblib

    
# loading in the model to predict on the data  
#open_model = open('connaitre_la_taille.pkl', 'rb')  
#load_modele= pickle.load(open_model)
model = joblib.load('connaitre_la_taille.pkl')
##chargement du Model
#model_charge=pkl.load(open('mon_model.sav','rb'))

def prix_voiture(input_data):
    input_data_numpy=np.asarray(input_data)
    input_data_reshape= input_data_numpy.reshape(1,-1)
    prediction=model.predict(input_data_reshape)
    return prediction[0]

def main():
    st.title('BIENVENUE SUR LE SITE DE PREDICTION DES PRIX DES VOITURES') 
    
    age=st.number_input('entrez L\'age')  

    predir=''
    b=0
                               
    if st.button('Resultat') :
        st.header('Votre Taille')
        predir=prix_voiture(age)
        b=predir[0]


    st.success(b)
                                    
if __name__=='__main__':
    main()