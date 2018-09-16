from app import app
from app.models import User

if __name__ == '__main__':
	#creation of admin user for first user and tests
	admin_user = User.objects(username='admin').first()
	if admin_user is None:
		admin_user = User(username='admin', email='admin@admin.com', first_name='App', last_name='Administrator', phone_number='admin')
		admin_user.set_password('admin')
		admin_user.set_unique_id('admin')
		admin_user.save()

	#runs app to be located from any device in the local network
	app.run(host='0.0.0.0', debug=True)
