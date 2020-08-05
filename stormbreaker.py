from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


##### to dynamically render html templates
@app.route('/<string:page_name>')
def general(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    error = None
    if request.method == 'POST':
        data = request.form.to_dict()
        write_data(data)
        write_csv(data)
        return redirect("thankyou.html")
    else:
        error = 'something went wrong'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    # return render_template('index.html', error=error)


def write_data(data):
    with open("database.txt", "a") as db:
        email = data['email']
        subject = data['text']
        message = data['message']
        file = db.write(f'\n{email}, {subject}, {message}')


def write_csv(data):
    with open("database.csv", "a", newline='') as db:
        email = data['email']
        subject = data['text']
        message = data['message']
        csv_writer = csv.writer(db, delimiter=',', quotechar='|', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])