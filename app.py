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

@app.route('/contact/')  
def Contact():
    
    return render_template('contact.html') 

if __name__ == '__main__':   
    app.run(debug=True)