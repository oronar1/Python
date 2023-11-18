from flask import Flask, render_template,redirect,url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField , URLField,TimeField,SelectField
from wtforms.validators import DataRequired, InputRequired, URL,Length
import csv

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe_name = StringField('Cafe name',
                       validators=[DataRequired(),
                                   InputRequired(),
                                   Length(1, 128)])
    cafe_location = URLField('Cafe Location on Google Maps (URL)',
                        validators=[DataRequired(),
                                    URL(True,
                                        message="Field must be a URL.")])
    open_time = TimeField('Opening Time e.g. 8:00AM',
                           validators = [DataRequired()],
                           format = ["%H:%M"])
    close_time = TimeField('Closing Time e.g. 5:30PM',
                            validators=[DataRequired()],
                            format="%H:%M")
    coffee_rating = SelectField('Coffee Rating',
                               validators=[DataRequired()],
                               choices=['☕',
                                        '☕☕',
                                        '☕☕☕',
                                        '☕☕☕☕',
                                        '☕☕☕☕☕'])
    wifi_strength = SelectField('Wifi Strength Rating',
                               validators=[DataRequired()],
                               choices=['✘',
                                        '💪',
                                        '💪💪',
                                        '💪💪💪',
                                        '💪💪💪💪',
                                        '💪💪💪💪💪'])
    power_socket = SelectField('Power Socket Availability',
                              validators=[DataRequired()],
                              choices=['✘',
                                       '🔌',
                                       '🔌🔌',
                                       '🔌🔌🔌',
                                       '🔌🔌🔌🔌',
                                       '🔌🔌🔌🔌🔌'])
    submit = SubmitField('Submit')

    def write_to_file(self):
        with open("cafe-data.csv", "a", encoding="utf8") as file:
            file.write(f"\n{self.cafe_name.data},"
                       f"{self.cafe_location.data},"
                       f"{self.open_time.data.strftime('%I:%M %p')},"
                       f"{self.close_time.data.strftime('%I:%M %p')},"
                       f"{self.coffee_rating.data},"
                       f"{self.wifi_strength.data},"
                       f"{self.power_socket.data}")

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    cafe_form = CafeForm()
    if cafe_form.validate_on_submit():
        cafe_form.write_to_file()
        return redirect(url_for('cafes'))
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=cafe_form)


@app.route('/cafes', methods=['GET', 'POST'])
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True, port=5002)
