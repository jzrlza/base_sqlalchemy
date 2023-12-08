import db_connect #is from db_connect.py
import random
from datetime import datetime, timedelta
from sqlalchemy import text
from sqlalchemy.orm import Session

from tkinter import * 
tk_app = Tk()

db = db_connect.SessionLocal()

tk_app.title('Test')

def add_task() :
	now = datetime.now()
	date_time = now.strftime("%Y-%m-%d %H:%M:%S")
	the_task_model = db_connect.Tasks()
	the_task_model.name = "test"+str(random.randint(1, 1000))
	the_task_model.date_created = str(date_time)
	db.add(the_task_model)
	db.commit()

def get_tasks() :
	raw_sql = text('SELECT * FROM tasks WHERE is_deleted = :deletion_bool ORDER BY id')
	result = db.execute(raw_sql, {"deletion_bool": False}).fetchall()
	print(result)

button1 = Button(tk_app, text='Add Task', width=25, command=add_task)
button1.pack()
button2 = Button(tk_app, text='Display Tasks', width=25, command=get_tasks)
button2.pack()

tk_app.mainloop()