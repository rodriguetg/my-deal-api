from flask import Flask, jsonify
from dealabs import Dealabs

app = Flask(__name__)

@app.route('/')
def index():
    return "Dealabs notifier running."

@app.route('/deals')
def deals():
    try:
        dealabs = Dealabs()
        # get_hot_deals() retourne directement la réponse JSON de l'API
        deals_response = dealabs.get_hot_deals()
        # La réponse contient déjà les données au bon format
        if 'data' in deals_response:
            return jsonify(deals_response['data'])
        else:
            return jsonify({"error": "No data found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --- Ajout endpoint healthz ---
@app.route('/healthz')
def healthz():
    return jsonify({'status': 'ok'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
