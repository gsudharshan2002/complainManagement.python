import tkinter as tk

# Initialize the complaint list with dictionaries to store more details
complaints = []

# Function to submit a complaint
def submit_complaint():
    complaint_text = entry_complaint.get()
    if complaint_text:
        complaint = {
            'text': complaint_text,
            'status': 'Pending' # Default status is 'Pending'
        }
        complaints.append(complaint)
        update_complaint_list()
        entry_complaint.delete(0, tk.END)

# Function to mark a complaint as resolved
def resolve_complaint():
    selected_index = listbox_complaints.curselection()
    if selected_index:
        selected_index = int(selected_index[0])
        complaints[selected_index]['status'] = 'Resolved'
        update_complaint_list()

# Function to update the list of complaints
def update_complaint_list():
    listbox_complaints.delete(0, tk.END)
    for i, complaint in enumerate(complaints, start=1):
        listbox_complaints.insert(tk.END, f"{i}. {complaint['text']} - Status: {complaint['status']}")

# Create the main tkinter window
root = tk.Tk()
root.title("Complaint Management System")

# Create and configure a listbox to display complaints
listbox_complaints = tk.Listbox(root, width=60, height=15)
listbox_complaints.pack(pady=10)

# Create an entry field for entering complaints
entry_complaint = tk.Entry(root, width=60)
entry_complaint.pack()

# Create a "Submit" button to submit complaints
submit_button = tk.Button(root, text="Submit Complaint", command=submit_complaint)
submit_button.pack()

# Create a "Resolve" button to mark complaints as resolved
resolve_button = tk.Button(root, text="Mark as Resolved", command=resolve_complaint)
resolve_button.pack()

# Start the tkinter main loop
root.mainloop()

