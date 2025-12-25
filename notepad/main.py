import customtkinter as ctk
from tkinter import filedialog, messagebox


class ModernNotepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Nikopad")
        self.root.geometry("700x500")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")


        self.label = ctk.CTkLabel(root, text="My Notes", font=("Helvetica", 24, "bold"))
        self.label.pack(pady=10)

        self.textbox = ctk.CTkTextbox(root, width=600, height=300, corner_radius=10)
        self.textbox.pack(padx=20, pady=10, fill="both", expand=True)

        self.button_frame = ctk.CTkFrame(root, fg_color="transparent")
        self.button_frame.pack(pady=20)

        self.save_button = ctk.CTkButton(self.button_frame, text="Save File", command=self.save_file)
        self.save_button.pack(side="left", padx=10)

        self.clear_button = ctk.CTkButton(self.button_frame, text="Clear All", fg_color="#d9534f",
                                          hover_color="#c9302c", command=self.clear_text)
        self.clear_button.pack(side="left", padx=10)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )

        if file_path:
            try:
                content = self.textbox.get("1.0", "end-1c")
                with open(file_path, "w") as file:
                    file.write(content)
                messagebox.showinfo("Success", "File saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {e}")

    def clear_text(self):
        if messagebox.askyesno("Confirm", "Clear everything?"):
            self.textbox.delete("1.0", "end")


if __name__ == "__main__":
    root = ctk.CTk()
    app = ModernNotepad(root)
    root.mainloop()
