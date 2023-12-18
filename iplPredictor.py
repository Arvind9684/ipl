import streamlit as st 
import pandas as pd
import numpy as np
import pickle
import sklearn
file=open("Logistic_model.pkl",'rb')
Logistic_model=pickle.load(file)


st.title("IPL Predictor")
df=pd.read_csv('Final_data.csv')
columens_name=df.columns
cities=df['City'].unique()  
teams=df['BattingTeam'].unique()



# Create Select teams Row and columns
col1,col2=st.columns(2)
with col1:
    batting_team = st.selectbox("Select the beating Team",sorted(teams))
if batting_team:
    bowling_team=np.delete(teams,np.where(teams==batting_team))
   

with col2:
    bowling_team = st.selectbox("Select the bowling Team",sorted(bowling_team))
selected_city= st.selectbox("Select the host city",cities)

# create input box for targets runs
target=int(st.number_input("Target Runs"))
col3,col4,col5=st.columns(3)
with col3:
    score=st.number_input("Score")
with col4:
    overs=st.number_input("Overs Completed",max_value=20)
with col5:
    wickets=st.number_input("Wickets Out",max_value=10)
if st.button("Predict Probability"):
    runs_left = int(target-score)
    balls_left=int(120-(overs*6))
    wickets=int(10-wickets)
    crr="{:.2f}".format(score/overs)
    rrr="{:.2f}".format((runs_left*6)/balls_left)

    input_df=pd.DataFrame({"BattingTeam":[batting_team],
                       "BallingTeam":[bowling_team],
                       "City":[selected_city],
                       "Left_run":[runs_left],
                       "Ball_left":[balls_left],
                       "Left_wicket":[wickets],
                       "total_run_x":[target],
                       "crr":[crr],
                       "rrr":[rrr]})
    st.subheader(":green[SHOW RESULT]",divider="rainbow")
    st.table(input_df)
    result=Logistic_model.predict_proba(input_df)
    show_result=pd.DataFrame({"BattingTeam Winning Probability":[result[0][0]],
                              "BallingTeam Winning Probability":[result[0][1]]})
    st.subheader("Probability")
    st.table(show_result)
   

