from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def my_home_page():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def log_the_user_in(param):
    pass


def write_to_file(data: dict):
    email = data.get("email")
    subject = data.get('subject')
    message = data.get('message')
    with open("database.txt", mode='a') as database:
        file = database.write(f"\n{email},{subject},{message}")
    with open("database.csv", newline='', mode='a') as database2:
        csv_write = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data=data)
            return redirect('/thankyou.html')
        except Exception:
            return 'did not save to DB!'
    else:
        return 'something went wrong!'
        # if valid_login(request.form['username'],
        #                request.form['password']):
        #     return log_the_user_in(request.form['username'])
        # else:
        #     error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    # return render_template('login.html', error=error)
