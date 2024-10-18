'''
CS 3700 - Networking & Distributed Computing - Fall 2024
Instructor: Thyago Mota
Student(s):
Description: Project 02 - Incidents WS (routes)
'''

from api import app, db
from api.models import Incident, Key
from flask import request, jsonify

# TODO #3: complete the view function that returns a json with all of the incidents that satisfy the search criteria
@app.get('/incidents')
def get_incidents():
    """
    Returns a list of incidents that satisfy a search criteria
    """
    return 'working in progress...'