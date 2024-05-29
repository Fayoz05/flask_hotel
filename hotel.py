from flask import Flask, render_template, url_for, flash, redirect, session
from forms import RegistrationForm

hotel = Flask(__name__)
hotel.config['SECRET_KEY'] = 'v38yh3hv73nvc948vhg'


@hotel.route('/')
def home():
    return render_template('index.html')


@hotel.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        session['username'] = form.username.data
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@hotel.route('/remove')
def remove():
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))


hotel.run(debug=True)
