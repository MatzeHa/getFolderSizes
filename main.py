import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory
from calculate_sizes import calculate_sizes


class MainApp:
    def __init__(self):
        # create and configure  window
        self.window = tk.Tk()
        self.window.title("Verzeichnis-Größen-Rechner")
        self.window.geometry("800x600")
        self.window.resizable(True, True)

        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.window.columnconfigure(2, weight=10)
        self.window.columnconfigure(3, weight=1)
        self.window.columnconfigure(4, weight=1)

        # define variables
        self.path = tk.StringVar(self.window, "/")

        # create widgets
        self.widgets = {}

        btn_choose_dir = tk.Button(self.window, text="Wähle Verzeichnis", command=self.choose_directory)
        btn_choose_dir.grid(row=0, column=1)
        self.widgets["BTN_CHOOSE_DIR"] = btn_choose_dir
        lbl_path = tk.Label(self.window, textvariable=self.path)
        lbl_path.grid(row=0, column=2, columnspan=3)
        self.widgets["LBL_PATH"] = lbl_path

        txt_results = tk.Text(self.window, width=100, height=30, state="disabled")
        scroll_results = ttk.Scrollbar(self.window, command=txt_results.yview)
        txt_results.configure(yscrollcommand=scroll_results.set)
        txt_results.grid(row=1, column=1, rowspan=3, columnspan=4)
        scroll_results.grid(row=1, column=4, rowspan=3, sticky="NSE")
        self.widgets["TXT_RESULTS"] = txt_results
        self.widgets["SCROLL_RESULTS"] = scroll_results

        btn_start_calculation = tk.Button(self.window, text="Starte Berechnung", state="disabled",
                                          command=self.start_calculation)
        btn_start_calculation.grid(row=5, column=1)
        self.widgets["BTN_START_CALCULATION"] = btn_start_calculation
        btn_exit = tk.Button(self.window, text="Beende Programm", command=self.quit_app)
        btn_exit.grid(row=5, column=3)
        self.widgets["BTN_EXIT"] = btn_exit

        self.window.mainloop()

    def choose_directory(self):
        new_path = askdirectory()
        if new_path != "":
            self.path.set(new_path)
            self.widgets["BTN_START_CALCULATION"].config(state="normal")

    def write_to_txt_results(self, text):
        self.widgets["TXT_RESULTS"].config(state="normal")
        self.widgets["TXT_RESULTS"].insert(tk.END, text + "\n")
        self.widgets["TXT_RESULTS"].see(tk.END)
        self.widgets["TXT_RESULTS"].config(state="disabled")

    def quit_app(self):
        self.window.destroy()

    def start_calculation(self):
        calculate_sizes(self)


if __name__ == "__main__":
    app = MainApp()
