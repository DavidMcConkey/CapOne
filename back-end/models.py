"""SQLALCHEMY models for placeholder"""
import datetime
import time
import hashlib

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

Bcrypt = Bcrypt()
db = SQLAlchemy()

class ShiftRole(db.Model):
    """How many people of certain role are needed for a shift.
    role_id / role - Role of given shift
    shift_id / shift - Shift itself
    number - Number of people required of given role for this shift
    """

    __tablename__ = "shift_roles"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    role = db.orm.relationship("Role")
    shift_id = db.Column(db.Integer, db.ForeignKey('shift.id'))
    shift = db.orm.relationship('Shift')
    number = db.Column(db.Integer)

    def __repr__(self):
        """Displays string"""
        return (
            f"Shift(id={self.id} "
            + f'role="{self.role}" '
            + f'shift="{self.shift}" '
            + f'number="{self.number}")'
        )

class Shift(db.Model):
    """Shifts to be scheduled during a certain date range
    restaurant_id / restaurant - Given restaurant for this shift
    day_of_week -The day of the week, 0 = Monday and so on
    start_time - The time the shift starts based on military time
    end-time - The time the shift ends based on military time
    priority - The Priority to fill shift
    start_date - The date this is first available
    end_date - The last date this is available
    roles - The roles needed for the shift 
    """

    __tablename__ = "shift"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    restaurant = db.orm.relationship('Restaurant')
    day_of_week = db.Column(db.Integer)
    start_time =db.Column(db.Integer)
    end_time =db.Column(db.Integer)
    priority = db.Column(db.Integer)
    start_date =db.Column(db.Integer)
    end_date =db.Column(db.Integer)
    roles = db.orm.relationship('ShiftRole', viewonly=True)

    def __repr__(self):
        """display string"""
        roles = ", ".join([f"{r.role.name} x {r.number}" for r in self.roles])
        return (
            f"Shift(id={self.id} "
            + f'day="{self.day_of_week}" '
            + f'start time="{self.start_time}" '
            + f"end time={self.end_time} "
            + f"priority={self.priority} "
            + f"start date={self.start_date} "
            + f"end date={self.end_date} "
            + f"roles={roles} "
        )
    

class UserRolePreference(db.Model):
    """The priority of a role at a restaurant for an employee in addition to Manager preference
    user_id/user - The employee
    role_id / role - The role of the employee
    priority - The Employee's priority for this role
    gm_priority - The Managers priority for this employee for this role
    """

    __tablename__ = "user_role_preference"
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.orm.relationship('User')
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    role = db.orm.relationship('Role')
    priority = db.Column(db.Float)
    gm_priority = db.Column(db.Float)

    def __repr__(self):
        """display string"""
        return (
            f'UserRolePreference(id={self.id} user="{self.user.name}" '
            f'role="{self.role.name}" @ "{self.role.restaurant.name}" '
            + f"priority={self.priority})"
        )
    
class UserExceptions(db.Model):
    """The GM's notes and hours limit for an employee
    restaurant_id - The restaurant for these limits
    user_id / user - The employee
    hours_limit - The maximum number of hours to schedule an employee
    notes - GM's notes about the employee
    """

    __tablename__ = "user_exceptions"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurant.id"))
    restaurant = db.orm.relationship("Restaurant")
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.orm.relationship("User")
    hours_limit = db.Column(db.Integer)
    notes = db.Column(db.String(50))

    def __repr__(self):
        """display string"""
        return (
            f"UserExceptions(id={self.id} "
            + f'gm="{self.gm.name}" '
            + f'user="{self.user.name}" '
            + f"hours={self.hours_limit} "
            + f"notes={self.notes})"
        )
    
class ScheduledShift(db.Model):
    """An instance of the scheduled shift
    date - The date of the given shift
    shift_id / shift - The shift that is scheduled
    role_id / role - The role for this shift
    user_id / user - The employee scheduled
    draft - If draft employees cannot see, otherwise they can
    notes - Notes to the employee from Manager pertaining to shift
    """
    
    __tablename__ = "scheduled_shift"
    id= db.Column(db.Integer, primary_key=True, autoincrement=True)
    date= db.Column(db.DateTime)
    shift_id= db.Column(db.Integer, db.ForeignKey('shift.id'))
    shift= db.orm.relationship('Shift')
    role_id=db.Column(db.Integer, db.ForeignKey('role.id'))
    role=db.orm.relationship('Role')
    user_id =db.Column(db.Integer, db.ForeignKey('user.id'))
    user=db.orm.relationship('User')
    draft= db.Column(db.Boolean, default=True)
    notes= db.Column(db.String(50))

    def __repr__(self):
        """display string"""
        return (
            f"ScheduledShift(id={self.id} "
            + f'date="{self.date}" '
            + f'shift="{self.shift}" '
            + f"role={self.role.name} "
            + f"user={self.user.name} "
            + f"draft={self.draft})"
        )

class UserAvailability(db.Model): 
    """The times available for a given employee
    user_id / user - The employee
    restaurant_id / restaurant - The restaurant
    day_of_week - The day of the week 0 = Monday
    start_time - The number of minutes since midnight that the priority starts
    end_time - The number of minutes since midnight that the priority ends
    start_date - The date this default is first available
    end_date - The last date this default is viable
    priority - Meaning of this time slot
        1 - want to work
        2 - can work
        3 - would not like to work
        4 - cant work
    note - Any notes about this given availability
    """

    __tablename__ = "user_availability"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.orm.relationship("User")
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurant.id"))
    restaurant = db.orm.relationship("Restaurant")
    day_of_week = db.Column(db.Integer)
    start_time = db.Column(db.Integer)
    end_time = db.Column(db.Integer)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    priority = db.Column(db.Float)
    note = db.Column(db.String(50))

    def __repr__(self):
        """display string"""
        return (
            f'UserAvailability(id={self.id} user="{self.user.name}" '
            + f'restaurant="{self.restaurant.name}" day={self.day_of_week} '
            + f"start_time={self.start_time} end_time={self.end_time} "
            + f'priority={self.priority} note="{self.note}")'
        )
    
class Role(db.Model):
    """The Employee roles at a restaurant
    name - The name of the role
    restuarant_id / restaurant - The restaurant for this role
    preferneces - The employee preferences for the given role
    """

    __tablename__ = 'role'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(50))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    restaurant = db.orm.relationship('Restaurant')
    preferences = db.orm.relationship('UserRolePreference', viewonly=True)

    def __repr__(self):
        """display string"""
        return (
            f'Role(id={self.id} name="{self.name}" '
            f'restaurant="{self.restaurant.name}")'
        )
    
class Restaurant(db.Model): 
    """The restaurant location
    name - the name of the restaurant
    gm_id / gm - the general manager (may be null)
    roles - list of Roles associated with the restaurant
    """

    __tablename__ = "restaurant"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    gm_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    gm = db.orm.relationship("User")
    roles = db.orm.relationship("Role", viewonly=True)
    shifts = db.orm.relationship("Shift", viewonly=True)

    def __repr__(self):
        """display string"""
        return (
            f'Restaurant(id={self.id} name="{self.name}" '
            + f'gm="{self.gm.name if self.gm else None}")'
        )
    
class User(db.Model): 
    """Represents an employee
    name - Full employee name
    email - The email to contact the employee at
    password_hash - sha256 hash of the user's password
    hours_limit - The maximum number of hours per week
    admin - true if this is an admin account
    gm_at - list of restaurants this user is a gm at
    roles - the role priorities at each restaurant
    """

    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password_hash = db.Column(db.String(64))
    hours_limit = db.Column(db.Integer)
    admin = db.Column(db.Boolean)
    gm_at = db.orm.relationship("Restaurant", viewonly=True)
    roles = db.orm.relationship("UserRolePreference", viewonly=True)
    availabilities = db.orm.relationship("UserAvailability", viewonly=True)

    @classmethod
    def hash_password(text):
        """hash some random text"""
        hasher = hashlib.new("sha256")
        hasher.update(text.encode("utf-8"))
        return hasher.hexdigest()

    def set_password(self, password):
        """Set the user password hash"""
        self.password_hash = User.__hash(password)

    def password_matches(self, password):
        """does this match the password"""
        return User.hash_password(password) == self.password_hash

    def __repr__(self):
        """display string"""
        return f'User(id={self.id} name="{self.name}" email="{self.email}")'

def connect_db(app):
    """Connects this databse to provided flask app."""
    db.app = app
    db.init_app(app)
    db.create_all()