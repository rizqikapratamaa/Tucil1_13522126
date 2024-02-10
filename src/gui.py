import tkinter as tk

def submit():
    buffer_val = int(buffer_entry.get())
    width_val = int(width_entry.get())
    height_val = int(height_entry.get())
    
    matrix = [[0 for _ in range(width_val)] for _ in range(height_val)]
    
    output_text.delete(1.0, tk.END)
    
    output_text.insert(tk.END, "Masukkan elemen matriks:\n")
    for i in range(height_val):
        row = input_entries[i].get().split()
        if len(row) != width_val:
            output_text.insert(tk.END, f"Error: Jumlah elemen pada baris {i+1} tidak sesuai dengan lebar matriks yang diinginkan.\n")
            return
        for j in range(width_val):
            matrix[i][j] = str(row[j])
    
    output_text.insert(tk.END, "\nMatriks yang diinputkan:\n")
    for i in range(height_val):
        for j in range(width_val):
            output_text.insert(tk.END, matrix[i][j] + " ")
        output_text.insert(tk.END, "\n")

# Create main window
root = tk.Tk()
root.title("Input Matrix")

# Create labels and entry widgets for buffer, width, and height
buffer_label = tk.Label(root, text="Jumlah Buffer:")
buffer_label.grid(row=0, column=0, padx=5, pady=5)
buffer_entry = tk.Entry(root)
buffer_entry.grid(row=0, column=1, padx=5, pady=5)

width_label = tk.Label(root, text="Panjang Matriks:")
width_label.grid(row=1, column=0, padx=5, pady=5)
width_entry = tk.Entry(root)
width_entry.grid(row=1, column=1, padx=5, pady=5)

height_label = tk.Label(root, text="Lebar Matriks:")
height_label.grid(row=2, column=0, padx=5, pady=5)
height_entry = tk.Entry(root)
height_entry.grid(row=2, column=1, padx=5, pady=5)

input_entries = []
for i in range(5):
    entry = tk.Entry(root)
    entry.grid(row=i+3, column=0, columnspan=2, padx=5, pady=2, sticky="ew")
    input_entries.append(entry)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=8, column=0, columnspan=2, pady=10)

# Output text area
output_text = tk.Text(root, height=10, width=40)
output_text.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
