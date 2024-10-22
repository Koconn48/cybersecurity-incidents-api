[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wFWrDUK1)
# Instructions 

In this project, you are required to implement a web service for sharing cybersecurity incidents. The dataset for this project was originally obtained from [Cyber Events Database Home](https://cissm.umd.edu/research-impact/publications/cyber-events-database-home). It has been exported to you in a CSV format and is available at [data/incidents.csv](data/incidents.csv). 

Your first task is to create and activate your local virtual environment using: 

```
virtualenv .venv
source .venv/bin/activate
```

Next, install all of the required Python libraries using: 

```
pip3 install -r requirements.txt
```

Then, finish the TODO in [src/init_db.py](src/init_db.py) and populate your sqlite database with all the incidents from the CSV file.  Make sure you run **init_db.py** from the project's main folder (not from **src**). 

Next, complete the TODO in [src/init_db.py](src/init_db.py) and populate your SQLite database with all the incidents from the CSV file. Ensure you run **init_db.py** from the project's main folder (not from the **src** directory).

After you have completed the database population, finish the TODO in [src/api/models.py](src/api/models.py) where you **Incident** class model is defined. 

Next, to complete the view function **get_incidents** that returns all of the incidents that satisfy the search criteria in json format. If a valid key is not informed, an unauthorized message should be returned. If nothing is returned from the search, a 404 error message should be returned. The search criteria consists of the following parameters (none of them are required): 

* event_date
* month
* year
* actor
* actor_type
* organization
* industry_code
* industry
* motive
* eventy_type
* event_subtype
* country
* actor_country
* offset

Note that month, year, and industry_code are integers. All of the other parameters are strings. If offset is not informed, it should default to 0 (zero). 

Your final task in this assignment is to finish the implementation of a client script that asks for the following parameters, either using the command-line or asking for the user: 

* key
* year
* country

The client should then display the description of all incidents found. 

# Evaluation 

You are NOT required to deploy the API. However, I should be able to run it locally starting flask from the project's folder using: 

```
export FLASK_APP=src/api
flask run
```

# Rubric 

```
+25 data is loaded correctly from the CSV dataset 
+25 Incidents model is implemented correctly based on the incidents' table columns
+28 API works with each of the search criteria (14x2)
+6 API checks the key for authorization
+6 The API returns a 404 error when no results are found for the search.
+10 The API client
```