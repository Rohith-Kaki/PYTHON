from collections import deque

class TicketSystem:
    def __init__(self):
        self.tickets = deque()

    def submit_ticket(self, customer_name, issue_description, priority=False):
        ticket = {"customer_name": customer_name, "issue_description": issue_description, "priority": priority}
        self.tickets.append(ticket)

    def display_tickets(self):
        print("Current Tickets:")
        for i, ticket in enumerate(self.tickets, start=1):
            print(f"{i}. Customer: {ticket['customer_name']}, Issue: {ticket['issue_description']}, Priority: {ticket['priority']}")

    def process_tickets(self):
        if not self.tickets:
            print("No tickets to process.")
            return
        ticket = self.tickets.popleft()
        print(f"Processing ticket - Customer: {ticket['customer_name']}, Issue: {ticket['issue_description']}, Priority: {ticket['priority']}")

# Example usage:
if __name__ == "__main__":
    ticket_system = TicketSystem()
    # Submit tickets
    ticket_system.submit_ticket("John Doe", "Internet connectivity issue")
    ticket_system.submit_ticket("Jane Smith", "Software installation problem", priority=True)
    ticket_system.submit_ticket("Bob Johnson", "Hardware malfunction")
    # Display current tickets
    ticket_system.display_tickets()
    # Process tickets
    print("\nProcessing Tickets:")
    ticket_system.process_tickets()
    ticket_system.process_tickets()
    ticket_system.process_tickets()
    ticket_system.process_tickets()
