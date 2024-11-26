import unittest
import json
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        with open('test/data-test.json') as f:
            self.test_data = json.load(f)

    def test_save_contact(self):
        response = self.app.post('/save_contact', data=self.test_data['contact'])
        data = response.get_json()
        self.assertEqual(data['message'], "Contact saved successfully")

    def test_save_language(self):
        response = self.app.post('/save_language', data=self.test_data['language'])
        data = response.get_json()
        self.assertEqual(data['message'], "Language saved successfully")

    def test_save_study(self):
        response = self.app.post('/save_study', data=self.test_data['study'])
        data = response.get_json()
        self.assertEqual(data['message'], "Study saved successfully")

    def test_save_certification(self):
        response = self.app.post('/save_certification', data=self.test_data['certification'])
        data = response.get_json()
        self.assertEqual(data['message'], "Certification saved successfully")

    def test_save_skill(self):
        response = self.app.post('/save_skill', data=self.test_data['skill'])
        data = response.get_json()
        self.assertEqual(data['message'], "Skill saved successfully")


    def test_save_experience(self):
        response = self.app.post('/save_experience', data=self.test_data['experience'])
        data = response.get_json()
        self.assertEqual(data['message'], "Experience saved successfully")

    def test_save_site(self):
        response = self.app.post('/save_site', data=self.test_data['site'])
        data = response.get_json()
        self.assertEqual(data['message'], "Site saved successfully")

    def test_save_about_me(self):
        response = self.app.post('/save_about_me', data=self.test_data['about_me'])
        data = response.get_json()
        self.assertEqual(data['message'], "About Me saved successfully")

if __name__ == '__main__':
    unittest.main()