from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/tourism'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class local_vendors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String(100))
    city = db.Column(db.String(100))
    slogan = db.Column(db.String(100))
    exact_address = db.Column(db.String(100))
    special_offers = db.Column(db.String(100))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        vendors = local_vendors.query.filter_by(city=city).all()
        return render_template('index2.html', vendors=vendors)
    return render_template('index2.html', vendors=[])

if __name__ == '__main__':
    app.run(debug=True)
