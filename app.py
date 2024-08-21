from flask import Flask ,request
from flask import render_template 

app = Flask(__name__)  



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


@app.route('/contact/')  
def Contact():
    
    return render_template('contact.html') 

@app.route('/temprary/')  
def Temp():
    
    return render_template('temprary.html') 


    
if __name__ == '__main__':   
    app.run(debug=True,host='0.0.0.0',port='8081')