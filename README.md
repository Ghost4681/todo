# To-Do

This is a To-Do app with python and sql as its back end and HTML as its frontend.

# Tutorial
## Homepage
On running the app the first screen to be seen should be the **Home** page where you can add new tasks. On scrolling one can also see a **Statistic** Heading where there is a pie chart of the task distributions based on the number of tasks the user has pending, completed, and not done.

## Creating a new Task
The task title, task description and a deadline can be set by typing on the respective fields. Note that all these fields are optional. On filling required fields and clicking **Add Task** the user is redirected to the **Active Tasks** page.

## Viewing Active Tasks
The **Active Tasks** page shows the list of the tasks you are yet to complete. This page only shows the task Title at first. On clicking the Task title, the task description appears. Clicking it again, hides the task description.

## Completing a Task
If you have completed a task and you want to mark it in your app, simply click the green button "Completed" and this will redirected you to the **Completed Tasks** page. Here you can view all the tasks you have completed along with the time when the user has completed the task. There is also a red "Undo" button next to each task which puts the corrresponding task back to active task if in case the Completed button was pressed by mistake.

## Task Not Done
There are tasks that after a point are just not that important. Such tasks which when missed can be added to the **Not Done** task list. This can be done in the **Active Tasks** page by clicking on the red **Not Done** button. This redirects the user to the **Not Done** page. Here, corresponding to every task title there is a green "undo" button, that can be used when the task has been added to the Not Done list by mistake or if the user has reconsidered to work on that task again.

## Navigating Task Lists
Apart from the implicit redirection that the app does when an task is completed, the user can also navigate between different task list as and when they please. This can be done by clicking the links **Home**, **Completed**, **Active Tasks**, **Not Done** given below the heading of the page the user is in.

# How To Get it to work on your PC!

These are the following things you need to do before running it on your PC:
- Import the the code onto your computer by clicking on the green button "Code"
    - Either click on the copy button next to the url and paste it on your cmd to clone it or
    - Click on Download Zip and extract it on to your PC.
- Open the repository on your cmd
- Run the following commands: (you could optionally also create a virtual environment before installing these modules)
```
>>>pip install flask
>>>pip install psycopg2
>>>pip install psycopg2-binary
>>>pip install flask-sqlalchemy
>>>pip install gunicorn
```
- This application stores its information in a database using **SQL** (preferably postgresql)
    - Postgresql can be can be download from the following [link](https://www.postgresql.org/download/)
    - Create and enter necessary credentials and create a new database of your choice
    - Open prime.py
    - In line 14 replace os.environ\['secret'] with "postgresql://<username>:<password>@localhost<database_name>"
- On cmd run the following commands:
```
>python3
>>>from prime import db
>>>db.create_all()
>>>exit()
```

That's all you need to do to enjoy this minimalistic TO-DO App!

# Developer's Note
## How Its Made!
This is the third website I have made at this point with HTML, CSS and JS and hence I was pretty well equipped with the basics of setting up a new website, such as creating a python file and writing a standard code for a url. Then I created looked for todo app templates on the web (cause its not that unique of a project🙄), and sure enough there was a bootstrap template for it. So i decided to work on it at the start and later change the design elements to the way I like. I almost instantly removed the js part from the bootstrap template because I prefer writing my own js scripts. After that it was just all about making things happen. I wanted the task title to strike off when it is completed and then go into the completed tasks page, but that seemed a little overkill for a "minimalistic" todo app. After tweaking and experimenting with the templates I was ready with 4 URL's. Since there was a need for the integration of a database in the app, I felt there was a need to set up 4 tables, one for all tasks, one for active ones, one for completed and one for not done but later decided all tasks was not needed. I have worked with postgresql before and I was comfortable with it so I went with that, after configuring and setting up my database, I connected it to my app and created all the tables required by the app.

Next was adding buttons in each page. The "Add Task" button in the homepage works in a slightly different manner than the rest of the buttons. The Add Task button changes the method to POST which is checked by the python app and then the data enterred is collected and added in the database before redirecting the user to active tasks page. The rest of the buttons could not be made to work in a similar function because there are multiple buttons in other pages all expected to do a similar kind of function. This was worked around by setting each button to redirect to a completely new link (namely accept, decline, completed, not done) corresponding to different functions. The different buttons in each page where differentiated by each one of them redirecting to a url based on the id of their task. Once those worked, the basic functionality of the app was complete.

The next part was to add a few features. But this is a never ending process and hence the final stage of the project. The first part was to add a hidden description that reveals itself when the title is clicked. This took a while as when the descriptions get longer the text continues to appear as one line the whole table would get extended and hence look ugly. This was later on  worked around by setting a maximum length of the column to 400px always. With that all major parts of the project was done. So I decided to work on the animations next. I have worked with them before and hence it was just about adding them at the right places, and I just decided to go with a simple "FadeInUp" for all text animations and incorporated a dropdown animation for the description to appear when the title is clicked. With that working as intended, the project was complete.

## Future Prospects
A strikethrough animation can be added when a task is completed. A drop up animation can be added when the revealed description is hidden again. A feature can be added to give the option of grouping tasks. A checkbox can be added while adding tasks that says "Automatically send it to Not Done when deadline is over?" More statistics can also perhaps be added. All the 4 different links can be combined into one single link using javascript