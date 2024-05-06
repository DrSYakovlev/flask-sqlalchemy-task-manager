from taskmanager import db


class Category(db.Model):
    #Schema for the Category model
    id = db.Column(db.Integer, primary_key = True) #Unique ID, acting as a primary key
    category_name = db.Column(db.String(25), unique = True, nullable = False)#25 is the maximum character count
    tasks = db.relationship("Task", backref = "category", cascade = "all, delete", lazy = True) #Targeting the "Task" table
    def __repr__(self): #__repr__ is for represent
        return self.category_name
    



class Task(db.Model): # Table for each task created
    #Schema for the Task model:
    id = db.Column(db.Integer, primary_key = True)
    task_name = db.Column(db.String(50), unique = True, nullable = False)
    task_description = db.Column(db.Text, nullable = False)
    is_urgent =  db.Column(db.Boolean, default = False, nullable = False)
    due_date = db.Column(db.Date, nullable = False)
    category_id = db.Colums(db.Integer, db.Foreignkey("category.id", ondelete = "CASCADE"), nullable = False)


    def __repr__(self): #__repr__ is for represent
        return "#{0} - Task: {1} | Urgent: {2}".format(self.id, self.task_description, self.task_urgent, self.due_date, self.is_urgent)