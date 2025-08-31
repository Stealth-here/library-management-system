from flask import Flask,render_template,request,redirect,url_for
import dp
import functions
app = Flask(__name__)

@app.route('/')
# app = Flask(_)

def home():
    books = functions.view_book()
    return render_template('home.html',books=books)

@app.route("/add", methods=['GET','POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        isbn = request.form['isbn']

        functions.insert_book(title, author, year, isbn)
        return redirect(url_for('home'))
    return render_template('add_book.html')

@app.route('/delete/<int:book_id>',methods=['POST'])
def delete_book(book_id):
    functions.delete_book_from_db(book_id)
    return redirect(url_for('home'))
if __name__ == '__main__':
    app.run(debug=True)
