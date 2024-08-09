from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for characters
characters = []

@app.route('/')
def index():
    sort_by = request.args.get('sort', 'name')  # Default to 'name' if not provided

    # Sort characters by initiative if 'initiative' is selected
    if sort_by == 'initiative':
        try:
            sorted_characters = sorted(characters, key=lambda x: int(x['initiative']), reverse=True)
        except ValueError:
            sorted_characters = characters  # Default sorting if initiative is not a number
    else:
        sorted_characters = characters

    return render_template('index.html', characters=sorted_characters)

@app.route('/add', methods=['POST'])
def add_character():
    name = request.form.get('name')
    ac = request.form.get('ac')
    initiative = request.form.get('initiative')
    weapon = request.form.get('weapon')
    weapon_damage = request.form.get('weapon_damage')
    hp = request.form.get('hp')
    
    characters.append({
        'name': name,
        'ac': ac,
        'initiative': initiative,
        'weapon': weapon,
        'weapon_damage': weapon_damage,
        'hp': hp
    })
    return redirect(url_for('index'))

@app.route('/update/<int:index>', methods=['POST'])
def update_character(index):
    hp = request.form.get('hp')
    characters[index]['hp'] = hp
    return redirect(url_for('index'))

@app.route('/delete/<int:index>', methods=['POST'])
def delete_character(index):
    if 0 <= index < len(characters):
        characters.pop(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
    app.run(debug=True)