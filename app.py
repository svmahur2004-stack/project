def check_voting_eligibility(name, voter_id, age, constituency):
    if age >= 18:
        status = "Eligible to Vote"
    else:
        status = "Not Eligible to Vote"

    return (
        f"Name: {name}\n"
        f"Voter ID: {voter_id}\n"
        f"Age: {age}\n"
        f"Constituency: {constituency}\n"
        f"Status: {status}"
    )


if __name__ == "__main__":
    name = input("Enter Name: ")
    voter_id = input("Enter Voter ID: ")
    age = int(input("Enter Age: "))
    constituency = input("Enter Constituency: ")

    print(check_voting_eligibility(name, voter_id, age, constituency))
