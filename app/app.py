from flask import Flask, request, jsonify
from models import db, Message
import config

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route('/messages', methods=['POST'])
    def add_message():
        data = request.get_json() or {}
        text = data.get('text', '').strip()
        if not text:
            return jsonify({'error': 'text required'}), 400
        m = Message(text=text)
        db.session.add(m)
        db.session.commit()
        return jsonify({'id': m.id, 'text': m.text}), 201

    @app.route('/messages', methods=['GET'])
    def list_messages():
        messages = Message.query.all()
        return jsonify([{'id': m.id, 'text': m.text} for m in messages]), 200

    @app.route('/')
    def index():
        return "Simple Flask app running with PostgreSQL!"

    @app.route('/health')
    def health():
        return jsonify({'status': 'healthy'}), 200

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)