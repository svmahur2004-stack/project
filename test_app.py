from app import check_voting_eligibility

def test_eligible_voter():
    result = check_voting_eligibility("Ravi", "V123", 25, "Bangalore")
    assert "Eligible to Vote" in result

def test_not_eligible_voter():
    result = check_voting_eligibility("Anu", "V124", 16, "Mysore")
    assert "Not Eligible to Vote" in result
