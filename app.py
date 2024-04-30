from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# Define database models
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)



# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_student', methods=['POST'])
def add_student():
    with app.app_context():  # Ensure operations are performed within the app context
        name = request.form['name']
        new_student = Student(name=name)
        db.session.add(new_student)
        db.session.commit()
    return 'Student added successfully!'

@app.route('/add_hostel', methods=['POST'])
def add_hostel():
    with app.app_context():  # Ensure operations are performed within the app context
        name = request.form['name']
        new_hostel = Hostel(name=name)
        db.session.add(new_hostel)
        db.session.commit()
    return 'Hostel added successfully!'

@app.route('/students')
def get_students():
    with app.app_context():  # Ensure operations are performed within the app context
        students = Student.query.all()
    return render_template('students.html', students=students)


# Run Flask app
if __name__ == '__main__':
    with app.app_context():  # Ensure operations are performed within the app context
        db.create_all()
    app.run(debug=True)
