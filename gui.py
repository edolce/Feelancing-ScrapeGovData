import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

def run_python_script():
    file_path = filedialog.askopenfilename(title="Select Excel File", filetypes=[("Excel Files", "*.xlsx")])
if file_path:
        try:
            # Run the standalone executable with the selected file as a parameter
            subprocess.run(["dist/main.exe", file_path], capture_output=True)
            messagebox.showinfo("Success", "Processing completed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

app = tk.Tk()
app.title("Excel Processing Tool")

btn_run = tk.Button(app, text="Run Python Script", command=run_python_script)
btn_run.pack(pady=20)

app.mainloop()
