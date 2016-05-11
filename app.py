from flask import Flask, render_template, request

import requests




app = Flask(__name__)

# Mailgun Base URL
URL = 'https://api.mailgun.net/v3/goldenstaffing.ca/messages'
MAILGUN_API_KEY = 'key-a6678793f067234695575a791ddffb75'


@app.route('/')
def index():
	return render_template('bc.html')




@app.route('/contact', methods=['POST','GET'])
def contact():

	if request.method == 'POST':

		params = request.form
		print params
		text = params['message']
		phone = params['phone'] 
		name = params['name']
		email = params['email']
		resume = request.files['resume']
		resume.name = resume.filename
		
		text =  text  + make_footer(name,phone,email)
		if resume:
			send_mail(text,resume)
		else:
			send_mail(text)
		return render_template('bc.html',message='Thank You for the Inquiry!')




def send_mail(text,resume=None):
	
       

		if resume:
			files = [('attachment',resume)]

		else:
			files = []
		return requests.post(URL,
        auth = ("api", MAILGUN_API_KEY),
         files=files,
        data = {"from": "Golden Staffing Services <postmaster@goldenstaffing.ca>",
               "to": ['navjotbabrah27@gmail.com'],
               "subject": 'Golden Staffing Inquiry',
               "text": text
               })


def make_footer(name,number,email):
	t = '\n\nRegards,\n'
	t += name+ '\n'
	t += number + '\n'
	t += email + '\n'

	return t

@app.route('/contact', methods=['POST'])
def redirect():
	if request.method == 'POST':
		if request.form('search' ,None) == "Like":
			return redirect(url_for('bc.html'))
		elif request.form('search',None) == "Dislike":
			return redirect(url_for('bc.html'))

if __name__ == '__main__':
	app.run(debug=True)
