ID_Number_input = "txbIdNumber"
Secret_Number_input = "txbSecretNumber"
Email_input = "txbEmailAddress"
Confirm_Email_input = "txbConfirmEmailAddress"
Password_input = "txbPassword"
Confirm_Password_input = "txbPasswordConfirm"

#ID_num = "ID Number"
#Sec_num = "Secret Number"
#Em_in = "Email Address"
#Em_con = "Email Address"
#Ps_in = "Password"
#Ps_con = "Password"

df = pd.read_csv("C:/Users/caudww/Downloads/Examples.csv")

elements = [ID_Number_input,str(Secret_Number_input),Email_input,Confirm_Email_input,Password_input,Confirm_Password_input]
text_answers = [ID_num,Sec_num,Em_in,Em_con,Ps_in,Ps_con]

for element in range(len(elements)):
    print (elements[element]+" "+text_answers[element])