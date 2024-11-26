from .models import db, ContactInfo, Language, Study, Certification, Skill, Experience, Site, AboutMe

def init_app(app):
    db.init_app(app)
    with app.app_context():
        # db.create_all()
        pass