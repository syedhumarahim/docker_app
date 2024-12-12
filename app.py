from flask import Flask, request

app = Flask(__name__)

# Dictionary mapping each painter to their top 5 paintings
paintings = {
    "Vincent van Gogh": [
        "Starry Night",
        "Sunflowers",
        "Café Terrace at Night",
        "Irises",
        "Wheatfield with Crows"
    ],
    "Diego Velázquez": [
        "Las Meninas",
        "The Surrender of Breda",
        "Portrait of Innocent X",
        "Christ Crucified",
        "Rokeby Venus"
    ],
    "Salvador Dalí": [
        "The Persistence of Memory",
        "Swans Reflecting Elephants",
        "The Elephants",
        "Lobster Telephone",
        "Christ of Saint John of the Cross"
    ],
    "Pierre-Auguste Renoir": [
        "Luncheon of the Boating Party",
        "Dance at Le Moulin de la Galette",
        "Bal du moulin de la Galette",
        "Girl with a Watering Can",
        "La Grenouillère"
    ],
    "Claude Monet": [
        "Impression, Sunrise",
        "Water Lilies",
        "Haystacks",
        "Rouen Cathedral",
        "Woman with a Parasol"
    ]
}

@app.route('/')
def home():
    # Generate dropdown options for each painter
    options_html = "\n".join([f'<option value="{painter}">{painter}</option>' for painter in paintings.keys()])

    return f'''
    <h1>Select a Painter</h1>
    <form method="POST" action="/show_paintings">
        <label for="painter">Choose a painter:</label>
        <select id="painter" name="painter">
            {options_html}
        </select>
        <br><br>
        <button type="submit">Show Top 5 Paintings</button>
    </form>
    '''

@app.route('/show_paintings', methods=['POST'])
def show_paintings():
    # Get the selected painter
    painter = request.form.get('painter')
    # Get the top 5 paintings for the selected painter
    top_paintings = paintings.get(painter, [])
    # Create a list of paintings in HTML
    paintings_list = "".join([f"<li>{painting}</li>" for painting in top_paintings])

    return f'''
    <h1>Top 5 Paintings by {painter}</h1>
    <ul>
        {paintings_list}
    </ul>
    <a href="/">Back</a>
    '''

if __name__ == '__main__':
    # Run on host 0.0.0.0 so Docker can map the container port
    app.run(host='0.0.0.0', port=5000, debug=True)







