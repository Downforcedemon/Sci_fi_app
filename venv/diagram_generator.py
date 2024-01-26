from flask import Flask, jsonify
from Search_new import process_star, fetch_all_star_data

app = Flask(__name__)

current_star_index = 0
all_stars = fetch_all_star_data()
star_viewed = True  # Flag to track whether the current star's diagrams have been viewed

@app.route('/process_next_star', methods=['GET'])
def process_next_star():
    global current_star_index, star_viewed
    if current_star_index >= len(all_stars):
        return jsonify({"status": "error", "message": "No more stars to process."}), 404

    if not star_viewed:
        return jsonify({"status": "error", "message": "Please view the current star before proceeding."}), 400

    ticid = all_stars[current_star_index][0]
    diagrams = process_star(ticid)
    current_star_index += 1
    star_viewed = False  # Reset the flag for the next star

    return jsonify({
        "status": "success",
        "ticid": ticid,
        "diagrams": diagrams
    })

@app.route('/confirm_viewed', methods=['POST'])
def confirm_viewed():
    global star_viewed
    star_viewed = True
    return jsonify({"status": "success", "message": "View confirmed. Ready for the next star."})

if __name__ == '__main__':
    app.run(debug=True)
