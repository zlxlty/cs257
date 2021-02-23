'''
Author: Duc, Sky
Description: 
Date: 2021-02-23 17:41:16
LastEditors: Tianyi Lu
LastEditTime: 2021-02-23 17:41:47
'''
import sys
import flask
import json
import config
import psycopg2

api = flask.Blueprint('api', __name__)

@api.route('/cats/') 
def get_cats():
    # Of course, your API will be extracting data from your postgresql database.
    # To keep the structure of this tiny API crystal-clear, I'm just hard-coding data here.
    cats = [{'name':'Emma', 'birth_year':1983, 'death_year':2003, 'description':'the boss'},
            {'name':'Aleph', 'birth_year':1984, 'death_year':2002, 'description':'sweet and cranky'},
            {'name':'Curby', 'birth_year':1999, 'death_year':2000, 'description':'gone too soon'},
            {'name':'Digby', 'birth_year':2000, 'death_year':2018, 'description':'the epitome of Cat'},
            {'name':'Max', 'birth_year':1998, 'death_year':2009, 'description':'seismic'},
            {'name':'Scout', 'birth_year':2007, 'death_year':None, 'description':'accident-prone'}]
    return json.dumps(cats)

@api.route('/dogs/') 
def get_dogs():
    dogs = [{'name':'Ruby', 'birth_year':2003, 'death_year':2016, 'description':'a very good dog'},
            {'name':'Maisie', 'birth_year':2017, 'death_year':None, 'description':'a very good dog'}]
    return json.dumps(dogs)