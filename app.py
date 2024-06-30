from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.app_context().push()

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(25), nullable=False)
    desc = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, default = datetime.now)
    
    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}" 
    
# for add 
@app.route('/', methods=['GET','POST'])
def hello_world():
    if request.method=="POST":
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
    allTodo = Todo.query.all()
    return render_template("index.html",allTodo=allTodo)

# for search
@app.route('/search', methods=["GET"])
def search():
    if request.method == 'GET':
        query = request.args.get('query') 
        results = Todo.query.filter(Todo.title.contains(query)).all()  
        return render_template('search.html', results=results, query=query)

# for update
@app.route('/update/<int:sno>', methods=['GET','POST'])
def update(sno):
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
    todo = Todo.query.filter_by(sno=sno).first()
    return render_template("update.html",todo=todo)

#for delete
@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")


if __name__== "__main__":
    app.run(debug=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
