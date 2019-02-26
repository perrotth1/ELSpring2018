# Tutorial for Creating a Database and Writing to it Using Python

This is a tutorial for creating and modifying databases with python, the same process
that is done in the blinkTemp.py program. 


1. The first step is to create the database file. In this case we are using Sqlite3. Move
to the directory that you want to store the database in and enter this command (using your 
own database name):

	sqlite3 [databaseName]

This command will create the database and also open the Sqlite3 command line for sql commands.

2. After that you will want to create a table that can have values written to it. You will want
to construct the table in the format that data will be coming in. For example: 

	CREATE TABLE clearence(name text, num integer);

The name of the table is clearence. Inside the table you specify the variables included on each
row by putting the name of the variable followed by the type. For example, text means a string.

3. After the table is created, use .quit to exit out of Sqlite3. In a python program, in order to
write to the database you must first import sqlite3 library and then create an object used to 
execute Sql commands. For example:

	con = sqlite3.connect('/home/henry/clear.db')

The path will be the path to your database file. 

4. Now we create a cursor object able to execute sql commands. Example:

	cur = con.cursor()

5. Now we can execute commands to fill the table. You can enter values manually or use other 
sources of data. To enter a row of values you would do this:

	#The SQL command would be: INSERT INTO clearence VALUES("Jack", 3);
	#The python code would be:

	cur.execute("INSERT INTO clearence VALUES(?,?)", ("Jack",3))

The execute method of the cursor object allows you to execute any Sql command. 

6. With this you can enter values into the database and the changes are instantly written to disk.
To view all the rows of your table you could do something like this:

	for row in cur.execute("SELECT * FROM clearence"):
		print row
