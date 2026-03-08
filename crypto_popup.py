import tkinter as tk
from tkinter import ttk
import hashlib


def compute_hash(text: str) -> str:
    """Return a cryptographic hash (SHA-256) of the input text."""
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    return digest


class CryptoPopupApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Crypto Popup")
        self.resizable(False, False)
        self._build_ui()

    def _build_ui(self):
        frm = ttk.Frame(self, padding=16)
        frm.grid(row=0, column=0, sticky="nsew")

        ttk.Label(frm, text="Enter text:").grid(row=0, column=0, sticky="w")
        self.input_var = tk.StringVar()
        self.input_entry = ttk.Entry(frm, textvariable=self.input_var, width=50)
        self.input_entry.grid(row=1, column=0, sticky="ew")
        self.input_entry.focus()

        self.hash_btn = ttk.Button(frm, text="Compute SHA-256", command=self.on_compute)
        self.hash_btn.grid(row=2, column=0, pady=(10, 0), sticky="ew")

        ttk.Label(frm, text="Cryptographic value:").grid(row=3, column=0, sticky="w", pady=(10, 0))
        self.output_var = tk.StringVar()
        self.output_label = ttk.Entry(frm, textvariable=self.output_var, width=50, state="readonly")
        self.output_label.grid(row=4, column=0, sticky="ew")

        # Bind Enter key to compute
        self.bind("<Return>", lambda event: self.on_compute())

    def on_compute(self):
        text = self.input_var.get()
        if not text:
            self.output_var.set("")
            return
        self.output_var.set(compute_hash(text))


if __name__ == "__main__":
    app = CryptoPopupApp()
    app.mainloop()
