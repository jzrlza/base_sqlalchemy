import db_connect #is from db_connect.py
import random
from datetime import datetime, timedelta
from sqlalchemy import text
from sqlalchemy.orm import Session

from tkinter import * 
from tkinter import ttk
from tktabl import *
tk_app = Tk()

db = db_connect.SessionLocal()

tk_app.title('Test')

frame = ttk.Frame(tk_app)
frame.pack(expand=YES, fill=BOTH)

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

	raw_headers = db_connect.inspector.get_columns("tasks")

	headers = []
	for raw_header in raw_headers :
		headers.append(raw_header['name']) #the other key is 'type'

	if len(result) <= 0 :
		return

	table = Table(frame, row=len(result), col=len(result[0]), headers=headers, data=result)
	for h in range(len(headers)) :
		cell = table.get_cell(0, h)
		cell.set_value(headers[h])
	for i in range(1, len(result)+1) :
		for j in range(len(result[i-1])) :
			cell = table.get_cell(i, j)
			cell.set_value(result[i-1][j])
	table.pack()

button1 = Button(tk_app, text='Add Task', width=25, command=add_task)
button1.pack()
button2 = Button(tk_app, text='Display Tasks', width=25, command=get_tasks)
button2.pack()

tk_app.mainloop()