from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def company_profile():
    # ...
    return render_template('index.html', company_info=company_info)

@app.route('/about')
def about_us():
    # ...
    return render_template('about.html', company_info=company_info)

@app.route('/contact')
def contact_us():
    # ...
    return render_template('contact_ui.html', company_info=company_info)

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    #Handle the contact form submission
    #You can process the form data here
    return 'Contact form submitted successfully!'

if __name__ == '__main__':
    app.run()