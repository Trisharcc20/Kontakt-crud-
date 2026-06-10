from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'supersecretkey'

db = SQLAlchemy(app)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    role = db.Column(db.String(80), nullable=True)
    status = db.Column(db.String(20), default='Active')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone or '',
            'role': self.role or '',
            'status': self.status,
            'created_at': self.created_at.strftime('%b %d, %Y')
        }


with app.app_context():
    db.create_all()
    # Seed sample data if empty
    if Contact.query.count() == 0:
        samples = [
            Contact(name='Arjun Sharma', email='arjun.sharma@example.com', phone='+91 98765 43210', role='Developer', status='Active'),
            Contact(name='Priya Mehta', email='priya.mehta@example.com', phone='+91 91234 56789', role='Designer', status='Active'),
            Contact(name='Rahul Das', email='rahul.das@example.com', phone='+91 87654 32109', role='Manager', status='Inactive'),
        ]
        db.session.bulk_save_objects(samples)
        db.session.commit()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/contacts', methods=['GET'])
def get_contacts():
    search = request.args.get('search', '').strip()
    query = Contact.query
    if search:
        query = query.filter(
            db.or_(
                Contact.name.ilike(f'%{search}%'),
                Contact.email.ilike(f'%{search}%'),
                Contact.role.ilike(f'%{search}%')
            )
        )
    contacts = query.order_by(Contact.created_at.desc()).all()
    return jsonify([c.to_dict() for c in contacts])


@app.route('/api/contacts', methods=['POST'])
def create_contact():
    data = request.get_json()
    if not data.get('name') or not data.get('email'):
        return jsonify({'error': 'Name and Email are required.'}), 400
    if Contact.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already exists.'}), 409
    contact = Contact(
        name=data['name'],
        email=data['email'],
        phone=data.get('phone', ''),
        role=data.get('role', ''),
        status=data.get('status', 'Active')
    )
    db.session.add(contact)
    db.session.commit()
    return jsonify(contact.to_dict()), 201


@app.route('/api/contacts/<int:contact_id>', methods=['GET'])
def get_contact(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    return jsonify(contact.to_dict())


@app.route('/api/contacts/<int:contact_id>', methods=['PUT'])
def update_contact(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    data = request.get_json()
    if not data.get('name') or not data.get('email'):
        return jsonify({'error': 'Name and Email are required.'}), 400
    existing = Contact.query.filter_by(email=data['email']).first()
    if existing and existing.id != contact_id:
        return jsonify({'error': 'Email already in use by another contact.'}), 409
    contact.name = data['name']
    contact.email = data['email']
    contact.phone = data.get('phone', '')
    contact.role = data.get('role', '')
    contact.status = data.get('status', 'Active')
    db.session.commit()
    return jsonify(contact.to_dict())


@app.route('/api/contacts/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    db.session.delete(contact)
    db.session.commit()
    return jsonify({'message': 'Contact deleted successfully.'})


if __name__ == '__main__':
    app.run(debug=True)
