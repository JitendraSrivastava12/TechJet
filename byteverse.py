from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

# Set the template folder (make sure 'appli1.html' exists in this folder)
app.template_folder = 'template'

# Database configuration
host = '127.0.0.1'
user = 'root'
password = 'Jsking@981'
database = 'byteverse'
auth_plugin='mysql_native_password'
# Define routes and handle form submissions
@app.route("/")
def home():
    image_path = 'static/images/my_image.jpg'  # Path to your image
    return render_template('log.html', image_path=image_path)
@app.route('/submit', methods=['POST'])
def submit():
    connection = None
    cursor = None  # Initialize cursor outside the try block

    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            auth_plugin='mysql_native_password'
        )
        cursor = connection.cursor()

        if request.method == 'POST':
            name = request.form['name']
            user_password = request.form['password']
            email = request.form['email']
            phone = request.form['phonenumber']

            # Insert data into the database
            cursor.execute(
                'INSERT INTO byteverse (username, password, email, number) VALUES (%s, %s, %s, %s)',
                (name, user_password, email, phone))
            connection.commit()

    except mysql.connector.Error as err:
        # Handle database connection errors
        flash(f"Database error: {err}", 'error')
        return render_template('log.html')

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
    return render_template("thanks.html")

@app.route('/login', methods=['POST'])
def do_login():
    try:
        connection = None
        cursor = None  # Initialize cursor outside the try block

        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            auth_plugin='mysql_native_password'
        )
        cursor = connection.cursor()

        username = request.form['username']
        user_password = request.form['password']  # Renamed the variable to avoid conflict

        # Query the database to validate user credentials
        cursor.execute('SELECT username, password FROM byteverse WHERE username = %s', (username,))
        result = cursor.fetchone()

        if result and result[1] == user_password:
            session['logged_in'] = True
            image_paths = ['images/man.jpg', 'images/man2.jpg', 'images/laundry1.jpeg', 'images/messfood1.jpeg', 'images/offerelectronics2.jpg', 'images/offerfood.jpeg', 'images/shops1.jpeg', 'images/Vendor1.jpg', 'images/yellowphoto.jpeg']
            return render_template("home.html", image_paths=image_paths)
        else:
            flash('Invalid username or password!', 'error')
            return render_template('log.html')


    except mysql.connector.Error as err:
        # Handle database connection errors
        flash(f"Database error: {err}", 'error')
        return render_template('log.html')

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('home'))
@app.route("/appli.html")
def index():
    image_path = 'static/images/my_image.jpg'  # Path to your image
    return render_template('sinuo.html', image_path=image_path)


@app.route("/mainpage.html")
def abd():
            image_paths = ['images/man.jpg', 'images/man2.jpg', 'images/laundry1.jpeg', 'images/messfood1.jpeg', 'images/offerelectronics2.jpg', 'images/offerfood.jpeg', 'images/shops1.jpeg', 'images/Vendor1.jpg', 'images/yellowphoto.jpeg','images/1712775458831.jpg', 'images/exotic.png', 'images/fruits.png', 'images/fruitvendor1.jpeg', 'images/fruitvendor2.jpeg', 'images/fruitvendor3.jpeg', 'images/juice.png', 'images/loginpageImage.jpg', 'images/nonveg.png''images/offerfood1.jpeg', 'images/streetfood.png','images/streetfood1.jpeg', 'images/tea.png', 'images/vegies.png', 'images/vegvendor1.jpg', 'images/vegvendor2.jpeg', 'images/vegvendor3.webp', 'images/vendorillustration.jpeg', 'images/washermen.png', 'images/yellow.jpeg', 'images/rating.png','images/washerman1.jpg']
            return render_template('mainpage.html', image_paths=image_paths)
 


@app.route("/home.html")
def avd():
    return render_template("home.html")
@app.route("/index4.html")
def avd1():
    return render_template("payment.html")
@app.route("/index5.html")
def avd12():
    return render_template("confirm.html")
@app.route("/index6.html")
def avd123():
    return render_template("paid.html")


if __name__ == '__main__':
    app.run(debug=True)