import random

def generate_lottery_tickets(num_tickets, ticket_length):
    tickets = set()
    while len(tickets) < num_tickets:
        ticket = ''.join(random.choices('0123456789', k=ticket_length))
        tickets.add(ticket)
    return list(tickets)

def pick_winners(tickets, num_winners):
    return random.sample(tickets, num_winners)

# Generate 100 unique lottery tickets
lottery_tickets = generate_lottery_tickets(100, 10)

# Pick 2 lucky winners
winners = pick_winners(lottery_tickets, 2)

print("Lottery Tickets:")
print(lottery_tickets)
print("\nLucky Winners:")
print(winners)