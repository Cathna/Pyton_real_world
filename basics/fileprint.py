
import pandas as pd

df = pd.read_csv("C:/Users/caudww/Downloads/Examples.csv")

ID_Number_input = "txbIdNumber"
Secret_Number_input = "txbSecretNumber"
Email_input = "txbEmailAddress"
Confirm_Email_input = "txbConfirmEmailAddress"
Password_input = "txbPassword"
Confirm_Password_input = "txbPasswordConfirm"

for user_id in range(len(df)):
   #driver.get(reg_url)
   #driver.maximize_window()
   ID_num = df["ID Number"][user_id]
   Sec_num = df["Secret Number"][user_id]
   Em_in = df["Email Address"][user_id]
   Em_con = df["Email Address"][user_id]
   Ps_in = df["Password"][user_id]
   Ps_con = df["Password"][user_id]
   text_answers = [ID_num,Sec_num,Em_in,Em_con,Ps_in,Ps_con]
   elements = [ID_Number_input,Secret_Number_input,Email_input,Confirm_Email_input,Password_input,Confirm_Password_input]
   text_answers = [ID_num,str(Sec_num),Em_in,Em_con,Ps_in,Ps_con]
   for element in range(len(elements)):
        print (elements[element]+" "+text_answers[element])
   #print(text_answers)