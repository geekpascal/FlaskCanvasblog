## Introduction
🎨TheCanvasblog is a blog where you can write, view and post ideas on topics that interest you. Feel free to use it to share with others your ideas, research and views.
Built using the Python flask framework which is light weight and extensible.

## Tech Stack (Dependencies) 👩‍💻 

### Dependencies 
the tech stack include the following:
 * 💻 **virtualenv** as a tool to create isolated Python environments
 * 🛅 **SQLAlchemy ORM** to be our ORM library of choice
 * 📚 **PostgreSQL** as our database of choice
 * 🐍 **Python3** 
 * 🧪 **Flask** as our server language and server framework
 
You can download and install all the dependencies mentioned above using `pip install -r requirements.txt` 

## Development Setup 
1. **Download the project starter code locally**
```
git clone https://github.com/geekpascal/FlaskCanvasblog.git
cd FlaskCanvasblog/ 
```

2. **Create an empty repository in your Github account online.**

3. **Initialize and activate a virtualenv using:**

```
python -m venv env
source env/bin/activate  
```
>**Note** - In Windows, the `env` does not have a `bin` directory. Therefore, you would use the analogous command shown below:
```
source env/Scripts/activate
```

4. **Install the dependencies:** 
```
pip install -r requirements.txt
```

5. **Run the development server:**
```
export FLASK_APP=run.py
export FLASK_ENV=development # enables debug mode
python run.py
```

6. **Verify on the Browser**<br>
Navigate to project homepage [http://127.0.0.1:5000/](http://127.0.0.1:5000/) or [http://localhost:5000](http://localhost:5000)

Good luck 😊

