import streamlit as st
import pickle
import numpy as np
import pandas as pd

#Data importing and processing

train=pd.read_csv(r"C:\Users\teymur.mahmudov\Desktop\Kaggle\train.csv")
train=train.drop("id",axis=1) 
train["c"]=train.target>=train.target.mean() # Adding target column
train["counting"]=1 # Adding a column that counts rows that categories match


# First, we need to create Chi-square table that includes degree of freedom and respective critical values (rounded)

Chisquaretable={

    "1":"4",
    "2":"6",
    "3":"8",
    "4":"9",
    "5":"11",
    "6":"13",
    "7":"14",
    "8":"16",
    "9":"17",
    "10":"18",
    "11":"20",
    "12":"21",
    "13":"22",
    "14":"24",
    "15":"25",
    "16":"26",
    "17":"28",
    "18":"29",
    "19":"30",
    "20":"31"
}


# Defining a function that would calculate expected values, chi-square value and return the final result by comparing observed and expected values

def show_predict_page():
    st.title("Chi-square Independence Test Software")

    st.write("""### Please, select the variables you want to test""")

    variable=(train.columns) #features to test with target variable

    target=(train.columns) #target variable


    #UI side: Adding dropdown menus

    variables = st.selectbox("Variable", variable)
    targets = st.selectbox("Target", target)


    #defining action button

    ok = st.button("Calculate ChiSquae")

    #setting action that will be generated once clicking on action button (ok)
    if ok:


        #creating the observed values table

        table=train.pivot_table(values='counting', index=[variables], columns=targets, aggfunc='count')
        expecteds=[]
        result=[]


        #itterating over observed table to calculate expected values
        
        for col in range(len(table.columns)):

            for rows in range(len(table.iloc[:,0])):
                expecteds.append(round(table.iloc[rows,:].sum()*table.iloc[:,col].sum()/sum(table.iloc[:,0]+table.iloc[:,1]),0))
    
        
        #chi square values calculation based on observed and expected values

        for iter in range(len(expecteds)):
            result.append(round((expecteds[iter]-table.unstack().values[iter])**2/expecteds[iter],2))
        

        #sum of chi square value 

        for res in range(1,len(result)):
            result[res]+=result[res-1]
        result=result[len(result)-1]


        #defining the condition that would tell us the final result

        if int(result)<=int(Chisquaretable[str((len(table.iloc[1,:])-1)*(len(table.iloc[:,0])-1))]):

            result="Your variables are ### Independent of each others"
        else:
            
            result="Your variables are ### Dependent of each others"

        result
        
        








show_predict_page()




