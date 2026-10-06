# Seatwork 2
from pyscript import document


def candidate_checker(e):
    club_members = ['kristine pasco', 'renn santos', 'luisito balajadia',
                    'josua ortiz', 'vivian carabot', 'jean evangelista',
                    'jubilee caballero', 'hariette onofre']

    f_name = document.getElementById('first_name').value
    l_name = document.getElementById('last_name').value
    candidate = f_name + ' ' + l_name
    member_checker = candidate.lower() in club_members

    messages = (f'Sorry {candidate}, your name is not on the list.', f'Congratulations {candidate}! You are now part of the ICT club.')  # 0 and 1, True or False

    document.getElementById('result').innerHTML = messages[member_checker]