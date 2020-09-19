from flask import Flask, render_template, request

app = Flask(__name__)
app.env = "development"
app.jinja_env.globals['zip'] = zip
app.jinja_env.globals['enumerate'] = enumerate


# flaskKwargs = {'debug': True}


@app.route('/')
def get_home_page():
    context = {
        'title': 'Mahmud\'s Homepage',
        'heading': 'About Me'
    }
    return render_template('home.html', **context)


@app.route('/resume')
def get_resume_page():
    context = {
        'title': 'Mahmud\'s Homepage',
        'heading': 'Resume'
    }
    return render_template('resume.html', **context)


@app.route('/research')
def get_research_page():
    context = {
        'title': 'Mahmud\'s Homepage',
        'heading': 'Research'
    }
    return render_template('home.html', **context)


@app.route('/projects')
def get_projects_page():
    context = {
        'title': 'Mahmud\'s Homepage',
        'heading': 'Projects'
    }
    return render_template('home.html', **context)


if __name__ == '__main__':
    app.run()
