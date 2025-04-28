from selenium import webdriver
import pandas as pd
import json
import faker


database = pd.DataFrame

url ='https://candidates.cambridgeenglish.org/Members/Register.aspx'

#ID Number = <input name="txbIdNumber" type="text" maxlength="9" id="txbIdNumber" class="mdc-text-field__input" required="required" minlength="9" pattern="^[0-9]{6}[A-Z]{3}|[A-Z]{3}[0-9]{6}$" aria-labelledby="txbIdNumber-label" aria-controls="txbIdNumber-helper" aria-describedby="txbIdNumber-helper" onblur="validateBlur(this)">
#Secret Number = <input name="txbSecretNumber" type="text" maxlength="4" id="txbSecretNumber" class="mdc-text-field__input" required="required" onblur="validateBlur(this)" pattern="[0-9]{4}" minlength="4" aria-describedby="txbSecretNumber-helper" aria-labelledby="txbSecretNumber-label" aria-controls="txbSecretNumber-helper">
#Email = <input name="txbEmailAddress" type="text" maxlength="254" id="txbEmailAddress" class="mdc-text-field__input" required="required" autocomplete="email" onblur="validateBlur(this)" pattern="(([^<>()[\]\\.,;:\s@&quot;]+(\.[^<>()[\]\\.,;:\s@&quot;]+)*)|(&quot;.+&quot;))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))" minlength="8" aria-describedby="txbEmailAddress-helper" aria-labelledby="txbEmailAddress-label" aria-controls="txbEmailAddress-helper">
#Confirm Email = <input name="txbConfirmEmailAddress" type="text" maxlength="254" id="txbConfirmEmailAddress" class="mdc-text-field__input" required="required" autocomplete="email" onblur="validateBlur(this)" pattern="(([^<>()[\]\\.,;:\s@&quot;]+(\.[^<>()[\]\\.,;:\s@&quot;]+)*)|(&quot;.+&quot;))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))" minlength="8" onpaste="return false" aria-describedby="txbConfirmEmailAddress-helper" aria-controls="txbConfirmEmailAddress-helper" aria-labelledby="txbConfirmEmailAddress-label" oncopy="return false" oncut="return false">
#Password = <input name="txbPassword" type="password" maxlength="20" id="txbPassword" class="mdc-text-field__input" required="required" autocomplete="new-password" onblur="validateBlur(this)" pattern="(?=.*[A-Za-z])(?=(.*\d){2})[A-Za-z\d]{8,20}" minlength="8" aria-describedby="txbPassword-helper" aria-controls="txbPassword-helper" aria-labelledby="txbPassword-label">
#Confirm Password = <input name="txbPasswordConfirm" type="password" maxlength="20" id="txbPasswordConfirm" class="mdc-text-field__input" required="required" autocomplete="new-password" onblur="validateBlur(this)" pattern="(?=.*[A-Za-z])(?=(.*\d){2})[A-Za-z\d]{8,20}" minlength="8" onpaste="return false" aria-describedby="txbPasswordConfirm-helper" aria-controls="txbPasswordConfirm-helper" aria-labelledby="txbPasswordConfirm-label" oncopy="return false" oncut="return false">
#I agrre terms = <input value="rdoAgree" name="RadioGroup" type="radio" id="rdoAgree" class="mdc-radio__native-control" required="required" aria-labelledby="rdoAgree-label" aria-controls="rdoAgree-helper" aria-describedby="rdoAgree-helper" onchange="validateBlur(this)">
#Submit button = <button onclick="formChecker(this); if (typeof(Page_ClientValidate) == 'function') Page_ClientValidate(''); __doPostBack('btnSubmit','')" id="btnSubmit" type="submit" class="mdc-button mdc-button--unelevated custom-filled-button mdc-ripple-upgraded"><span class="mdc-button__ripple"></span><!-- /.mdc-button__ripple --><span class="mdc-button__label">Submit</span><!-- /.mdc-button__label --></button>
<a id="hlRegister" class="mdc-button mdc-button--unelevated custom-filled-button mdc-button--icon-trailing mdc-ripple-upgraded" href="/Members/Register.aspx">
                                        <span class="mdc-button__ripple"></span>
                                        <span class="mdc-button__label">Register</span>
                                        <i class="material-icons mdc-button__icon" aria-hidden="true">arrow_forward_ios</i>
                                      </a>
text_question_element_class = "quantumWizTextinputPaperinputInput"
checkbox_question_element_class = "appsMaterialWizToggleRadiogroupOffRadio"
submit_element_class = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span'
ID_Number_input = "txbIdNumber"
Secret_Number_input = "txbSecretNumber"
Email_input = "txbEmailAddress"
Confirm_Email_input = "txbConfirmEmailAddress"
Password_input = "txbPassword"
Confirm_Password_input = "txbPasswordConfirm"
I_agree_terms = "rdoAgree"
submit_candidate = ""

def submit(driver, element_class):
    driver.find_element_by_xpath(element_class).click()
    return driver

def answerCheckBox(driver, df, element_class, user_id):
    color_answer = df["colors"][user_id]
    color_answer_index = color_index_dict[color_answer]
    driver.find_elements_by_class_name(element_class)[color_answer_index].click()
    
    return driver


def answerNameAge(driver, df, element_class, user_id):
    name = df["names"][user_id]
    age = df["ages"][user_id]
    text_answers = [name, str(age)] # following the order in the form
    text_questions = driver.find_elements_by_class_name(element_class)
    for a,q in zip(text_answers,text_questions):
        q.send_keys(a)
    
    return driver


df = pd.read_csv("./submission_form_database.csv")
text_question_element_class = "quantumWizTextinputPaperinputInput"
checkbox_question_element_class = "appsMaterialWizToggleRadiogroupOffRadio"

url = "https://forms.gle/WY7E9N8wkiMtziTD9"
driver = webdriver.Chrome(executable_path="./chromedriver")
for user_id in range(len(df)):
    driver.get(url)
    
    driver.maximize_window()
    driver = answerNameAge(driver, df, text_question_element_class, user_id)
    driver = answerCheckBox(driver, df, checkbox_question_element_class, user_id)
    driver = submit(driver, submit_element_class)