from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Db
Db = SQLAlchemy()

class KamUser( Db.Model ):

	# Ref. to table
	__tablename__ = 'kam_users'

	# Class fields match columns
	id = Db.Column( Db.Integer, primary_key=True, autoincrement=True )
	category = Db.Column( Db.String(64), nullable=False )
	rang = Db.Column( Db.String(64), nullable=False )
	full_name = Db.Column( Db.String(64), nullable=False )
	age_year = Db.Column( Db.Integer, nullable=False )
	location = Db.Column( Db.String(64), nullable=False )
	total_time = Db.Column(Db.DateTime,nullable=False )
	run_link = Db.Column( Db.String(256), nullable=False )
	run_year = Db.Column( Db.Integer, nullable=False )
