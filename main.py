import json
from flask import Flask, request, jsonify, render_template, send_file, redirect, url_for
from models import init_app, db, ContactInfo, Language, Study, Certification, Skill, Experience, Site, AboutMe
from io import BytesIO

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cvtest:passwordtest123@localhost:5432/cvmaker'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = '/path/to/upload'  # Cambia esto a la ruta deseada

init_app(app)

@app.route('/')
def home():
    return render_template('template-only-html.html')

@app.route('/create-data')
def create_data():
    contacts = ContactInfo.query.all()
    languages = Language.query.all()
    studies = Study.query.all()
    certifications = Certification.query.all()
    skills = Skill.query.all()
    experiences = Experience.query.all()
    sites = Site.query.all()
    about_me = AboutMe.query.all()

    return render_template('form_create_data.html', 
                           contacts=contacts,
                           languages=languages, 
                           studies=studies, 
                           certifications=certifications, 
                           skills=skills, 
                           experiences=experiences, 
                           sites=sites, 
                           about_me=about_me)

@app.route('/create-cv')
def create_cv():
    contacts = ContactInfo.query.all()
    languages = Language.query.all()
    studies = Study.query.all()
    certifications = Certification.query.all()
    skills = Skill.query.all()
    experiences = Experience.query.all()
    sites = Site.query.all()
    about_me = AboutMe.query.all()

    return render_template('form_create_cv.html', 
                           contacts=contacts,
                           languages=languages, 
                           studies=studies, 
                           certifications=certifications, 
                           skills=skills, 
                           experiences=experiences, 
                           sites=sites, 
                           about_me=about_me)

@app.route('/save_contact', methods=['POST'])
def save_contact():
    data = ContactInfo(
        name=request.form.get('name'),
        title=request.form.get('title'),
        phone=request.form.get('phone'),
        email=request.form.get('email'),
        address=request.form.get('address')
    )
    db.session.add(data)
    db.session.commit()
    return jsonify({'message': 'Contact saved successfully'})

@app.route('/save_language', methods=['POST'])
def save_language():
    data = Language(
        language_name=request.form.get('language_name'),
        language_level=request.form.get('language_level')
    )
    db.session.add(data)
    db.session.commit()
    return jsonify({'message': 'Language saved successfully'})

@app.route('/save_study', methods=['POST'])
def save_study():
    data = Study(
        school=request.form.get('school'),
        career=request.form.get('career'),
        description=request.form.get('description')
    )
    db.session.add(data)
    db.session.commit()
    return jsonify({'message': 'Study saved successfully'})

@app.route('/save_certification', methods=['POST'])
def save_certification():
    data = Certification(
        certification=request.form.get('certification')
    )
    db.session.add(data)
    db.session.commit()
    return jsonify({'message': 'Certification saved successfully'})

@app.route('/save_skill', methods=['POST'])
def save_skill():
    data = Skill(
        skill=request.form.get('skill')
    )
    db.session.add(data)
    db.session.commit()
    return jsonify({'message': 'Skill saved successfully'})

@app.route('/save_experience', methods=['POST'])
def save_experience():
    data = Experience(
        company=request.form.get('company'),
        job_title=request.form.get('job_title'),
        job_description=request.form.get('job_description'),
        date1=request.form.get('date1'),
        date2=request.form.get('date2')
    )
    db.session.add(data)
    db.session.commit()
    return jsonify({'message': 'Experience saved successfully'})

@app.route('/save_site', methods=['POST'])
def save_site():
    data = Site(
        site_name=request.form.get('site_name')
    )
    db.session.add(data)
    db.session.commit()
    return jsonify({'message': 'Site saved successfully'})

@app.route('/save_about_me', methods=['POST'])
def save_about_me():
    data = AboutMe(
        description=request.form.get('description')
    )
    db.session.add(data)
    db.session.commit()
    return jsonify({'message': 'About Me saved successfully'})

@app.route('/save_cv', methods=['POST'])
def save_cv():
    cv_data = request.get_json()  # Get the received data as JSON
    print(cv_data)  # Print the received data

    json_data = json.dumps(cv_data, indent=4)
    buffer = BytesIO()
    buffer.write(json_data.encode())
    buffer.seek(0)

    return send_file(buffer, as_attachment=True, download_name='cv_data.json', mimetype='application/json')

@app.route('/import_cv')
def import_cv():
    return render_template('import_cv.html')


@app.route('/view_cv', methods=['POST'])
def view_cv():
    file = request.files['file']
    if file and file.filename.endswith('.json'):
        file_content = file.read().decode('utf-8')
        cv_data = json.loads(file_content)
        return render_template('template-only-html.html', **cv_data)
    return "Invalid file format", 400

if __name__ == '__main__':
    app.run(debug=True)
