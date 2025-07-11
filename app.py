from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to connect

@app.route('/submit', methods=['POST'])
def handle_form():
    # Get data from the form
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    service = request.form.get('service')
    message = request.form.get('message')

    # Save to text file
    with open('messages.txt', 'a') as f:
        f.write(f"\nName: {name}\nEmail: {email}\nPhone: {phone}\nService: {service}\nMessage: {message}\n{'-'*30}\n")

    return jsonify({'status': 'success', 'message': 'Message received'})

if __name__ == '__main__':
    app.run(debug=True)
