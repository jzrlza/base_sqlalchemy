import db_connect
import random

import tkinter as tk
tk_app = tk.Tk()

db = db_connect.SessionLocal()

def add_task() :
	the_task_model = db_connect.Tasks()
	the_task_model.name = "test"+str(random.randint(1, 1000))
	the_task_model.date_created = "tba"+str(random.randint(1, 1000))
	db.add(the_task_model)
	db.commit()

tk_app.title('Test')
button = tk.Button(tk_app, text='Add Task', width=25, command=add_task)
button.pack()

tk_app.mainloop()