from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    matches = []
    if request.method == 'POST':
        test_string = request.form['test_string']
        regex_pattern = request.form['regex_pattern']
        
        # Perform regex matching
        matches = re.findall(regex_pattern, test_string)
    
    return render_template('index.html', matches=matches)

@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form.get('email')  # Use .get() to avoid KeyError
    # Basic email regex pattern
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    is_valid = bool(re.match(email_regex, email))
    return render_template('index.html', email=email, is_valid=is_valid)

if __name__ == '__main__':
    app.run(debug=True)
