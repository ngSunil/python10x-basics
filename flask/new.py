# import the Flask package
from flask import Flask, render_template, request

# interaction 
web = Flask(__name__) # create an object web

# mapping
@web.route('/')
@web.route('/register')
# inputs
def home():
    # return 'Welcome'
    return render_template('register.html')

@web.route('/confirmation', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        n = request.form.get('name')
        c = request.form.get('city')
        p = request.form.get('phone')
        return render_template('confirmation.html', name=n, city = c, phone=p)
        
@web.route('/second')
def second():
    return render_template('second.html')           
# MAIN
if __name__ == '__main__':
    web.run(debug=True)
