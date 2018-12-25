from flask import Flask,redirect, render_template,Markup, flash, url_for

app =Flask(__name__, static_folder='static', template_folder='template')
app.secret_key = "sddas"
@app.template_global()
def hello():
    print("hello world")
    return 'hello world'

@app.route('/')
def index():
    return render_template('index.html', date = ['2321321','sadsadsad','dsaiufhsakfsa'])


@app.context_processor
def show():
    f = "hello world"
    return dict(f = f)

@app.template_filter()
def my_s(s):
    return str(s) + Markup(' &#9835;')

@app.template_test()
def enmptry(s):
    if s:
        return True
    else:
        return False


@app.route('/hello/<name>/')
def mytemplate(name):
    return render_template('myextend.html', name = name)


@app.route('/flash')
def myflash():
    flash("hello")
    return redirect(url_for('mytemplate', name = 'das'))


if __name__ == "__main__":
    app.run('127.0.0.1', port= 9000, debug = True)