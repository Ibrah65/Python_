from datetime import datetime

# Get user inputs
bookID = input("Enter book ID: ")
dueDate = input("Enter due date (dd/mm/yyyy): ")
returnDate = input("Enter return date (dd/mm/yyyy): ")

# Convert input dates to datetime objects
dueDate = datetime.strptime(dueDate, "%d/%m/%Y")
returnDate = datetime.strptime(returnDate, "%d/%m/%Y")

# Calculate days overdue
daysOverdue = (returnDate - dueDate).days

# Determine fine rate using if-else statement
if daysOverdue <= 0:
    fineRate = 0
    fineAmount = 0
    daysOverdue = max(0, daysOverdue)  # Avoid negative overdue days for early returns
    print("The book was returned on time or early. No fine.")
else:
    if daysOverdue <= 7:
        fineRate = 20
    elif 8 <= daysOverdue <= 14:
        fineRate = 50
    else:
        fineRate = 100
    fineAmount = daysOverdue * fineRate

# Display results
print("\nBook ID:", bookID)
print("Due Date:", dueDate.strftime("%d/%m/%Y"))
print("Return Date:", returnDate.strftime("%d/%m/%Y"))
print("Days Overdue:", daysOverdue)
print("Fine Rate:", fineRate)
print("Fine Amount:", fineAmount)
