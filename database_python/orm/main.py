import peewee
from models import User, Store, Product, Category , Categories_Products

def create_tables():
  if Categories_Products.table_exists():
    Categories_Products.drop_table()

  if Category.table_exists():
    Category.drop_table()

  if Product.table_exists():
    Product.drop_table()

  if Store.table_exists():
    Store.drop_table()

  if User.table_exists():
    User.drop_table()

  User.create_table()
  Store.create_table()
  Product.create_table()
  Category.create_table()
  Categories_Products.create_table()

def insert_users():
  User.create(username='eduardo_cf', password='password', email='eduardocf@codigofacilito.com')
  User.create(username='eduardo_gpg', password='password', email='eduardo@codigofacilito.com')

def insert_stores():
  Store.create(admin_id=1, name='tienda facilita uno', address='Oficinas')
  Store.create(admin_id=2, name='tienda facilita dos', address='Oficinas')

def insert_products():
  Product.create(store_id=1, name='Pan', description='Pan integral', price=5.5, stock=50)
  Product.create(store_id=1, name='Leche', description='Baja en gradas', price=15.5, stock=100)
  Product.create(store_id=1, name='Jamon', description='de pavo', price=30.9, stock=80)
  Product.create(store_id=1, name='mayonesa', description='mayonesa', price=30.9, stock=80)

  Product.create(store_id=2, name='Soda', description='Dieta', price=10.0, stock=50)
  Product.create(store_id=2, name='Fritura', description='Frituras de papa', price=20.5, stock=100)
  Product.create(store_id=2, name='Salsa', description='chile habanero', price=29, stock=80)
  Product.create(store_id=2, name='Mostaza', description='Mostaza', price=30.9, stock=80)

def insert_categories():
  Category.create(name='Liquidos', description='liquidos')
  Category.create(name='Embutidos', description='embutidos')
  Category.create(name='Snacks', description='snacks')
  Category.create(name='Aderezos', description='aderezos')
  Category.create(name='Carnes', description='carnes')

def insert_categories_products():
  Categories_Products.create(category_id='3', product_id='1')
  Categories_Products.create(category_id='1', product_id='2')
  Categories_Products.create(category_id='2', product_id='3')
  Categories_Products.create(category_id='4', product_id='4')
  Categories_Products.create(category_id='3', product_id='5')

def create_schema():
  create_tables()
  insert_users()
  insert_stores()
  insert_products()
  insert_categories()
  insert_categories_products()

if __name__ == '__main__':
  create_schema()

"""
  ###INSERT DATA (5 WAYS)
  #1
  user = User()
  user.username = 'Felicie'
  user.password = '123'
  user.email = 'felicie@prueba.com'
  user.save()
  
  #2
  user = User(username='Vivianne',password='123456')
  user.save()

  #3
  user = {'username':'Feli', 'password': '1234'}
  user = User(**user)
  user.save()

  #4
  user = User.create(username='Vivi',password='123456789', email='hola@prueba.com')

  #5
  query = User.insert(username='Feli_V',password='123', email='hola2@prueba.com')
  query.execute()

  ###GET DATA (2 wAYS)
  #1
  user = User.get(User.id==1)

  #2
  users = User.select() #SELECT * FROM users
  users = User.select().where(User.id > 2) #SELECT * FROM users WHERE id>2

  ###UPDATE DATA (2 WAYS)
  #1
  user.username = 'username_updated'
  user.save()
  
  #2
  query = User.update(password='0000').where(User.id==1)
  query.execute()

  ###DELETE DATA (2 WAYS)
  #1
  user.delete_instance()
  user.delete_instance(recursive=True) #Cascada

  #2
  query = User.delete().where(User.id==1)
  query.execute()
"""
