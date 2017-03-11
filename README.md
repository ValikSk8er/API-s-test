### APIs automation tests and data mining ###
Task from anonymous company (original code with all comments in my hidden bitbucket (ValikSk8er) repo).

Task for APIs test:
- Test the server that allow methods: GET, GET -id, POST, DELETE.
- Verify the server response codes is correct and information that was added.
- Verify that all methods working as expected.
- All data is correctly added to server.
- Create a DB using Redis in which candidate names and positions will be stored. In order to accomplish this task:
	1. Redis should be installed on local machine.
	2. All requests to server that require passing names and positions within your test should take that data from Redis.
	3. All comparisons that touch verification of the names and positions you have in test should be done using data from Redis.

Tips:
- POST request accepts name and position in body;
-  Body is expected to be in JSON format;
- All requests with body should contain correct “Content-Type” header;
- Not all methods might work as expected;
- In this section you do not need to parse response, only to verify that “some” data was uploaded to server.

Unix task:
Use existing datamining.log to receive next information:
- 1.1 Count # of successful requests per hour.
- 1.2 Results should be stored in file.
- 2.1 Count % of successful requests per hour.
- 2.2 Results should be stored in file.

Tips:
- Log contains data only per 1 day;
- Successful request should have response code 200;


* Repo divided to the two part it's folders "APIs test" and "Unix scripts".

APIs test contain:

- config.py				- main file that defines an API url and the ability to use or not a database
- "tests" 				- folder with pytest
-	tests_to_api.py 	- the file with main tests methods and the setup and teardown methods
- "data" 					- folder with data for test
-	test_data.py 		- file with test data
- 	driven_test_data.py - file that have methods to driven by test data
-	redis_db.py 		- file that have methods for acces to the Redis database 
- "pages"					- folder with API methods
-	candidates.py		- main file that describes the API methods

Unix_tasks contain:
- datamining.log			- file with log from that need to receive an information
- coutn_p_h-script.sh		- file that contain the script to receive # of successful requests per hour
- percent_p_h-script.sh	- file that contain the script to receive % of successful requests per hour
- count_per_hours.txt		- file that contain the saved information about # of successful requests per hour
- percent_per_hours.txt	- file that contain the saved information about % of successful requests per hour

### How do I get set up? ###
###For API test:###
- Download all files.
- Install Redis DB to local machine.
- Install pytest to local machine.
- Also you can add downloaded files like a progect to PyCharm IDE or similar.
- Install libraries to IDE:
	* pytest
	* redis
	* requests
	* json
	* random
- Configure a running the progect from pytest.
- Run file tests_to_api.py 

###For Unix task:###
- Download all files.
- Set access rules to scripts, using chmod command:
	* chmod 755 coutn_p_h-script.sh
	* chmod 755 percent_p_h-script.sh
- Run scripts:
	* ./coutn_p_h-script.sh
	* ./percent_p_h-script.sh


### Valentyn Chereshnevyi ###
* email: valiksk8@gmail.com
* skype: valiksk
