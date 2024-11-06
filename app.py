from flask import Flask, render_template, request

app = Flask(__name__)


notes = []

@app.route('/')
def index():
    return render_template('index.html', notes=notes)

@app.route('/add_note', methods=['POST'])
def add_note():
    note_text = request.form['note_text']
    note_color = request.form['note_color']
    notes.append({'text': note_text, 'color': note_color})
    return render_template('index.html', notes=notes)

@app.route('/delete_note/<int:note_id>', methods=['POST'])
def delete_note(note_id):
    if 0 <= note_id < len(notes):
        del notes[note_id]
    return render_template('index.html', notes=notes)

if __name__ == '__main__':
    app.run(debug=True)
