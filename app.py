import numpy as np
import streamlit as st 
import pickle
import sklearn
import joblib

    

model=pickle.load(open('connaitre_la_taille.pkl','rb'))

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