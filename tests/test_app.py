import pytest
from fastapi.testclient import TestClient
from app import app

@pytest.fixture
def client():
    return TestClient(app)

def test_index_page(client):
    """Test the index page loads successfully."""
    response = client.get("/")
    assert response.status_code == 200
    assert "Sarthak Singh Gaur" in response.text

def test_portfolio_api(client):
    """Test the portfolio API endpoint."""
    response = client.get("/api/portfolio")
    assert response.status_code == 200
    data = response.json()
    assert "education" in data
    assert "skills" in data
    assert "projects" in data
    assert "achievements" in data
    
    # Check required fields
    assert 'name' in data
    assert 'education' in data
    assert 'skills' in data
    assert 'projects' in data
    assert 'achievements' in data
    
    # Check education data
    education = data['education']
    assert 'degree' in education
    assert 'institution' in education
    assert 'duration' in education
    
    # Check skills data
    skills = data['skills']
    assert 'languages' in skills
    assert 'technologies' in skills
    assert 'machine_learning' in skills
    assert 'data_analysis' in skills 