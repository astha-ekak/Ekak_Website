from flask import Flask ,request,flash
from flask import render_template 
from flask_wtf import CSRFProtect
from flask_wtf.csrf import CSRFError
from flask import *

from forms import ContactForm

from build_table_email import table_email
from send_telegram_msg import sending_Telegram_Message as telegram_bot

app = Flask(__name__)  

app.secret_key='bf6cc269e9594e9caef019ecdc2f4ea1'

@app.route('/') 
@app.route('/home/')  
def Home():
    
    return render_template('home.html') 

@app.route('/blog/')  
def Blog():
    
    return render_template('blog.html') 


@app.route('/about/')  
def About():
    
    return render_template('about.html') 



@app.route('/teams/')  
def Team():
    
    return render_template('teams.html') 




@app.route('/career/')  
def Career():
    
    return render_template('career.html') 


@app.route('/contact/',methods=['GET','POST'])
def contact_page():
    form=ContactForm()
    if request.method=='GET':
        return render_template("contact.html",form=form)
    elif request.method=='POST':
        if form.validate_on_submit():
            name=form.name.data
            email=form.email.data
            # print(name,email)
            mobile=form.mobile.data
            # print(mobile)
            individual=form.individual.data
            company_name=form.company_name.data
            help=form.help.data

            """
            Sending Email Start
            """
            user_data = {
                "Platform":[F"Ekak Website"],
                'Name': [F"{name}"],
                "Email": [F"{email}"],
                'Mobile': [F"{mobile}"],
                "Individual": [F"{individual}"],
                'Company Name': [F"{company_name}"],
                "Message": [F"{help}"]
            }

            table_email(user_data=user_data)
            """
            Sending Email Start
            """
            msg=F'''Platform : Ekak Website\nName: {name}\nEmail : {email}\nMobile : {mobile}\nIndividual : {individual}\nCompany Name : {company_name}\nMessage : {help}'''
            # Email Alert 
            status=telegram_bot(msg)
            print(status)
            # Telegram Bot & Send Alert
           




            flash("You were successfully submitted the form!")
            return redirect('/contact/')
        print("PPOST Request")
        print(form.errors)
        # return F'Your Contact Failed'
        return render_template("contact.html",form=form)


@app.route('/temprary/')  
def Temp():
    
    return render_template('temprary.html') 







if __name__ == '__main__':   
    app.run(debug=True)