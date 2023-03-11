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
        self.result_widgets = []

        btn_choose_dir = tk.Button(self.window, text="Wähle Verzeichnis", command=self.choose_directory)
        btn_choose_dir.grid(row=0, column=1)
        self.widgets["BTN_CHOOSE_DIR"] = btn_choose_dir
        lbl_path = tk.Label(self.window, textvariable=self.path)
        lbl_path.grid(row=0, column=2, columnspan=3)
        self.widgets["LBL_PATH"] = lbl_path

        txt_results = tk.Text(self.window, width=80, height=2, state="disabled")
        scroll_results = ttk.Scrollbar(self.window, command=txt_results.yview)
        txt_results.configure(yscrollcommand=scroll_results.set)
        txt_results.grid(row=1, column=1, rowspan=1, columnspan=4)
        scroll_results.grid(row=1, column=4, rowspan=1, sticky="NSE")
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
        dir_sizes = calculate_sizes(self)
        dir_sizes = self.sort_sizes(dir_sizes)
        self.create_result_table(dir_sizes)

    def sort_sizes(self, dir_sizes):

        for i in range(len(dir_sizes)):
            print(i)
        dir_sizes.sort(key=lambda a: a[1], reverse=True)

        return dir_sizes

    def create_result_table(self, dir_sizes):
        start_row = 3
        if len(dir_sizes) == 0:
            self.write_to_txt_results("Keine Unterordner...")
            return
        total_rows = len(dir_sizes)
        print(dir_sizes)
        for i in range(total_rows):
            print(i)
            new_cell = tk.Entry(self.window, width=100)
            new_cell.grid(row=start_row+i, column=1)
            new_cell.config(state="normal")
            new_cell.insert(tk.END, str(dir_sizes[i][0]))
            new_cell.config(state="disabled")
            self.result_widgets.append(new_cell)
            new_cell = tk.Entry(self.window, width=8)
            new_cell.grid(row=start_row+i, column=2)
            new_cell.config(state="normal")
            new_cell.insert(tk.END, str(dir_sizes[i][1]))
            new_cell.config(state="disabled")
            self.result_widgets.append(new_cell)

        self.widgets["BTN_START_CALCULATION"].grid(row=start_row+i+2)
        self.widgets["BTN_EXIT"].grid(row=start_row+i+2)


if __name__ == "__main__":
    app = MainApp()
