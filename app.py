from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Data based on your resume
portfolio_data = {
    "name": "Sarthak Singh Gaur",
    "education": {
        "degree": "BS In Data science and Application",
        "institution": "IIT Madras",
        "duration": "Sep. 2021 - Dec 2025"
    },
    "skills": {
        "languages": ["Python", "C++", "SQL", "JavaScript", "HTML/CSS"],
        "technologies": ["Flask", "Vue.js", "Linux", "Git", "Redis", "Celery"],
        "machine_learning": ["Supervised Learning", "Unsupervised Learning", "Deep Learning"],
        "data_analysis": ["Pandas", "NumPy", "Scikit-Learn", "PyTorch"]
    },
    "projects": [
        {
            "name": "Influencer Connect V2",
            "technologies": ["Flask", "VueJS", "SQLite", "Redis", "Celery"],
            "description": "Developed a Full-Stack Influencer Engagement and Sponsorship Coordination Platform."
        },
        {
            "name": "CrimeCast: Forecasting Crime Categories using ML",
            "technologies": ["Python", "Scikit-Learn", "XGBoost"],
            "description": "Developed a supervised learning model to forecast crime categories, leveraging ensemble learning techniques."
        },
        {
            "name": "EcoConnect",
            "technologies": ["Vue.JS", "Flask", "SQLite"],
            "description": "Developed a community-driven web application to promote sustainability."
        },
        {
            "name": "End to End ML Deployment on Amazon Elastic Beanstalk",
            "technologies": ["Python", "Scikit-learn", "CatBoost", "AWS Elastic Beanstalk"],
            "description": "Developed an end-to-end machine learning pipeline to predict diabetes."
        }
    ],
    "achievements": [
        "Secured 4th place in the CodeChef Python Coding Competition by IIT Madras.",
        "Secured Runner-up position in the Tech for Social Good category at Hacksprint Hackathon for developing EcoConnect.",
        "Headed a 3-tier team of 25+ Coordinators and Junior Executives for Cultural Events in Paradox '23."
    ]
}

@app.route('/')
def index():
    """Renders the landing page."""
    return render_template('index.html')

@app.route('/api/portfolio')
def get_portfolio_data():
    """Serves portfolio data as JSON."""
    return jsonify(portfolio_data)

if __name__ == '__main__':
    app.run(debug=True)