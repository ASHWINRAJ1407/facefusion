from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import db, EngagementResult
from analysis import get_engagement_result

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///engagement.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Initialize database
def init_db():
    with app.app_context():
        db.create_all()

@app.route('/')
def home():
    engagement_percentage = get_engagement_result()
    not_engaged_percentage = 100 - engagement_percentage
    
    result = EngagementResult(engagement_percentage=engagement_percentage, not_engaged_percentage=not_engaged_percentage)
    db.session.add(result)
    db.session.commit()
    
    return render_template('index.html', engaged=engagement_percentage, not_engaged=not_engaged_percentage)

@app.route('/dashboard')
def dashboard():
    results = EngagementResult.query.order_by(EngagementResult.timestamp.desc()).all()
    return render_template('dashboard.html', results=results)

# Route to handle deleting an engagement history entry
@app.route('/delete/<int:id>', methods=['POST'])
def delete_entry(id):
    entry_to_delete = EngagementResult.query.get_or_404(id)
    
    try:
        db.session.delete(entry_to_delete)
        db.session.commit()
        return redirect(url_for('dashboard'))
    except:
        return "There was a problem deleting the entry."

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
