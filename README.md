# Data-Engineer-Technical-Challenge-Solution

First this project, I decided to write two scripts. A person class script to create the person objects as well as a main script to run all other functions necessary to complete the challenge. 
I opted not to create a database class as in my opinion the only benefit in creating it would be for cosmetic reasons to reduce the amount of text in the main file. 
Clear commenting and 
The packages I chose were csv and psycopg2. The csv package allows for easy manipulation of csv files and I opted to use a postgresql database as Postgres gives the ability to store data in XML and arrays. Though postgres may take longer to process queries compared to other databases as the database being used is a smaller database, the difference in speeds to process queries will be negligible. Also, my prefered python IDE (pycharm) has a plugin for postgresql.  
As I was using postgresql, I used pgAdmin 4 to create the tables raw and clean and to do exploratory querying of the data.
To clean the data, I chose to filter by who had .edu email or was under the age of 25. I chose this criteria as these are people in my experience are pretty new to credit.
I included the input statement to give more flexiblity to user when requesting a query.
In the display, I chose only to show the last 4 digits of the card to add a layer of security.
