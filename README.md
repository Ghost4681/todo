# To-Do

This is a To-Do app with python and sql as its back end and HTML as its frontend.

#How To Get it to work on your PC!

These are the following things you need to do before running it on your PC:
- Import the the code onto your computer by clicking on the green button "Code"
-   Either click on the opy button next to the url and paste it on your cmd to clone it or
-   Click on Download Zip and extract it on to your PC.
- Open the repository on your cmd
- Run the following commands: (you could optionally also create a virtual environment before installing these modules)
> \>>>pip install flask
> 
> \>>>pip install psycopg2
> 
> \>>>pip install psycopg2-binary
> 
> \>>>pip install flask-sqlalchemy
> 
> \>>>pip install gunicorn
> 
> \>>>pip install functools
- This application stores its information in a database using **SQL** (preferably postgresql)
-   Postgresql can be can be download from the following [link](https://www.postgresql.org/download/)
-   Create and enter necessary credentials and create a new database of your choice
- Open prime.py
-   In line 14 replace os.environ\['secret'] with "postgresql://\<username>:<password>@localhost/<database_name>"

That's all you need to do to enjoy this minimalistic TO-DO App!
