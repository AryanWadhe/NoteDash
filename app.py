from flask import Flask, render_template, request
import json

app = Flask(__name__)

notes = []

def delete_note(note_id):
    if request.method == 'POST':
        # Delete the note with the given ID from the list of notes
        del notes[note_id]
        save_notes() # Save notes to file
    # Return the updated index page
    return index()

def load_notes():
    global notes
    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []

def save_notes():
    with open('notes.json', 'w') as file:
        json.dump(notes, file, indent=4)

if __name__ == '__main__':
    app.run(debug=True)