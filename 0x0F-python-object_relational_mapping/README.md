# 0x0F Python Object-Relational Mapping

This project explores Object-Relational Mapping (ORM) in Python, focusing on the use of MySQLDB and SQLAlchemy.

## File Implementations

- **0-select_states.py:** The primary script that connects to a MySQL database and fetches all states from the `states` table.
- **1-filter_states.py:** A script that lists all states with a name starting 
with N (upper N) from the database `hbtn_0e_0_usa`.
- **2-my_filter_states.py:** A script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
- **3-my_safe_filter_states.py:** A a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. It is a script that is safe from MySQL injections
- **4-cities_by_state.py:** A script that lists all cities from the database hbtn_0e_4_usa
- **5-filter_cities.py:** A script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
- **model_state.py:** A a python file that contains the class definition of a State and an instance Base = declarative_base()
- **7-model_state_fetch_all.py:** A script that lists all State objects from the database hbtn_0e_6_usa.
- **8-model_state_fetch_first.py:** A script that prints the first State object from the database hbtn_0e_6_usa.
- **9-model_state_filter_a.py:** A script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa
- **10-model_state_my_get.py:** A script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa.
- **11-model_state_insert.py:** A script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
- **12-model_state_update_id_2.py:** A script that changes the name of a State object from the database hbtn_0e_6_usa
- **13-model_state_delete_a.py:** A script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa
- **model_cities.py:** A Python file similar to model_state.py named model_city.py that contains the class definition of a City.
- **14-model_city_fetch_by_state.py:** A  script 14-model_city_fetch_by_state.py that prints all City objects from the database hbtn_0e_14_usa
- **100-relationship_states_cities.py:** A script that creates the State “California” with the City “San Francisco” from the database hbtn_0e_100_usa
- **101-relationship_states_cities_list.py:** A script that lists all State objects, and corresponding City objects, contained in the database hbtn_0e_101_usa