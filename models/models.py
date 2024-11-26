from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ContactInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(30), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'title': self.title,
            'phone': self.phone,
            'email': self.email,
            'address': self.address
        }

class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    language_name = db.Column(db.String(100), nullable=False)
    language_level = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'language_name': self.language_name,
            'language_level': self.language_level
        }

class Study(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    school = db.Column(db.String(100), nullable=False)
    career = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(400), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'school': self.school,
            'career': self.career,
            'description': self.description
        }

class Certification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    certification = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'certification': self.certification
        }

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skill = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'skill': self.skill
        }

class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    job_title = db.Column(db.String(100), nullable=False)
    job_description = db.Column(db.String(400), nullable=False)
    date1 = db.Column(db.String(100), nullable=False)
    date2 = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'company': self.company,
            'job_title': self.job_title,
            'job_description': self.job_description,
            'date1': self.date1,
            'date2': self.date2
        }

class Site(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    site_name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'site_name': self.site_name
        }

class AboutMe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(400), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description
        }