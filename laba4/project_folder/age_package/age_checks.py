# age_checks.py
def check_kindergarten(age):
    return 0 <= age < 7

def check_school(age):
    return 7 <= age < 18

def check_college(age):
    return 18 <= age < 25

def check_work(age):
    return 25 <= age < 60

def check_choice(age):
    return 60 <= age <= 120

def check_invalid(age):
    return age < 0 or age > 120
