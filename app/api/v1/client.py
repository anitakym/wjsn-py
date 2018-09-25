from app.libs.redprint import Redprint

api = Redprint('client')


@api.route('/register')
def create_client():
    return 'create book'
