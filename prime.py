from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
import os
import random
import math
from datetime import datetime

app=Flask(__name__)

ENV = 'dev'
app.debug=True
app.config['SECRET_KEY'] = 'awwfaw'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/todo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


@app.route('/', methods=['GET','POST'])
def home():
    session['url'] = 'all'
    compcount = db.session.query(Completed).count()
    actcount = db.session.query(Active).count()
    notcount = db.session.query(Notdone).count()
    if request.method == 'POST':
        title = request.form['title']
        task = request.form['task']
        deadline = str(request.form['deadline'])
        if deadline == '':
            deadline_format = "No Deadline"
        else:
            deadline_format = deadline[8:10]+'/'+deadline[5:7]+'/'+deadline[0:4]+' '+deadline[11::]
        data = Active(title, task, deadline_format)
        db.session.add(data)
        db.session.commit()
        flash('Added New Task!', 'success')
        return redirect(url_for('active'))
    return render_template('all.html', compcount = compcount, actcount = actcount, notcount = notcount)

class Completed(db.Model):
    __tablename__ = 'completed'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200))
    task = db.Column(db.Text())
    deadline = db.Column(db.Text())
    timecomplete = db.Column(db.Text())

    def __init__(self, id, title, task, deadline, timecomplete):
        self.id = id
        self.title = title
        self.task = task
        self.deadline = deadline
        self.timecomplete = timecomplete

@app.route('/completed', methods=['GET','POST'])
def completed():
    completedata = db.session.query(Completed).all()
    db.session.commit()
    return render_template('completed.html', completedata = completedata)

class Active(db.Model):
    __tablename__ = 'active'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200))
    task = db.Column(db.Text())
    deadline = db.Column(db.Text())

    def __init__(self, title, task, deadline):
        self.title = title
        self.task = task
        self.deadline = deadline

@app.route('/active', methods=['GET','POST'])
def active():
    activedata = db.session.query(Active).all()
    db.session.commit()
    return render_template('active.html', activedata = activedata)


class Notdone(db.Model):
    __tablename__ = 'notdone'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200))
    task = db.Column(db.Text())
    deadline = db.Column(db.Text())


    def __init__(self, id, title, task, deadline):
        self.id = id
        self.title = title
        self.task = task
        self.deadline = deadline

@app.route('/notdone', methods=['GET','POST'])
def notdone():
    notdonedata = db.session.query(Notdone).all()
    db.session.commit()
    return render_template('notdone.html', notdonedata = notdonedata)

@app.route('/accept/<id>', methods=['GET','POST'])
def accept(id):
    data_add = db.session.query(Active).filter(Active.id == id).first()
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M")
    data = Completed(id, data_add.title, data_add.task, data_add.deadline, dt_string)
    db.session.add(data)
    db.session.query(Active).filter(Active.id == id).delete()
    db.session.commit()
    flash('Task Completed!', 'success')
    return redirect(url_for('completed'))

@app.route('/decline/<id>', methods=['GET','POST'])
def decline(id):
    data_add = db.session.query(Active).filter(Active.id == id).first()
    data = Notdone(id, data_add.title, data_add.task, data_add.deadline)
    db.session.add(data)
    db.session.query(Active).filter(Active.id == id).delete()
    db.session.commit()
    flash('Task Not Done!', "danger")
    return redirect(url_for('notdone'))

@app.route('/completed/<id>', methods=['GET','POST'])
def completedundo(id):
    data_add = db.session.query(Completed).filter(Completed.id == id).first()
    data = Active(data_add.title, data_add.task, data_add.deadline)
    db.session.add(data)
    db.session.query(Completed).filter(Completed.id == id).delete()
    db.session.commit()
    flash('Completed Task has been added to back to current Tasks!', "danger")
    return redirect(url_for('active'))

@app.route('/notdone/<id>', methods=['GET','POST'])
def notdoneundo(id):
    data_add = db.session.query(Notdone).filter(Notdone.id == id).first()
    data = Active(data_add.title, data_add.task, data_add.deadline)
    db.session.add(data)
    db.session.query(Notdone).filter(Notdone.id == id).delete()
    db.session.commit()
    flash('A closed Task has been added to back to current Tasks!', "success")
    return redirect(url_for('active'))

if __name__=='__main__':
    app.run() 
