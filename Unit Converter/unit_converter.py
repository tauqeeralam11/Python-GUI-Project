import tkinter as tk
from tkinter import ttk
class UnitConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TNotebook", tabposition='n')
        
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)
        self.create_length_tab()
        self.create_weight_tab()
        self.create_temperature_tab()
        self.create_currency_tab()

    def create_length_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Length")
        units = ["Meters", "Kilometers", "Feet", "Miles", "Inches"]
        self.build_converter_ui(tab, units, self.convert_length)

    def create_weight_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Weight")
        units = ["Kilograms", "Grams", "Pounds", "Ounces"]
        self.build_converter_ui(tab, units, self.convert_weight)

    def create_temperature_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Temp")
        units = ["Celsius", "Fahrenheit", "Kelvin"]
        self.build_converter_ui(tab, units, self.convert_temperature)

    def create_currency_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Currency")
        units = ["USD", "EUR", "GBP", "INR", "JPY"]
        self.build_converter_ui(tab, units, self.convert_currency)

    def build_converter_ui(self, parent, units, callback):
        frame = tk.Frame(parent)
        frame.pack(expand=True, fill='both', padx=20, pady=20)
        tk.Label(frame, text="Value:").grid(row=0, column=0, sticky='w', pady=5)
        amount_var = tk.DoubleVar(value=1.0)
        entry = tk.Entry(frame, textvariable=amount_var)
        entry.grid(row=0, column=1, sticky='ew', padx=5)
        tk.Label(frame, text="From:").grid(row=1, column=0, sticky='w', pady=5)
        from_var = tk.StringVar(value=units[0])
        from_menu = ttk.Combobox(frame, textvariable=from_var, values=units, state="readonly")
        from_menu.grid(row=1, column=1, sticky='ew', padx=5)
        tk.Label(frame, text="To:").grid(row=2, column=0, sticky='w', pady=5)
        to_var = tk.StringVar(value=units[1])
        to_menu = ttk.Combobox(frame, textvariable=to_var, values=units, state="readonly")
        to_menu.grid(row=2, column=1, sticky='ew', padx=5)

        result_label = tk.Label(frame, text="Result: ", font=("Helvetica", 12, "bold"), fg="#333")
        result_label.grid(row=3, column=0, columnspan=2, pady=20)

        def update_result(*args):
            try:
                val = float(entry.get())
                u1 = from_var.get()
                u2 = to_var.get()
                res = callback(val, u1, u2)
                result_label.config(text=f"{res:.4f} {u2}")
            except ValueError:
                result_label.config(text="Invalid Input")

        entry.bind("<KeyRelease>", update_result)
        from_menu.bind("<<ComboboxSelected>>", update_result)
        to_menu.bind("<<ComboboxSelected>>", update_result)
        
        update_result()

    def convert_length(self, value, from_unit, to_unit):
        factors = {
            "Meters": 1.0,
            "Kilometers": 1000.0,
            "Feet": 0.3048,
            "Miles": 1609.34,
            "Inches": 0.0254
        }
        meters = value * factors[from_unit]
        return meters / factors[to_unit]

    def convert_weight(self, value, from_unit, to_unit):
        factors = {
            "Kilograms": 1.0,
            "Grams": 0.001,
            "Pounds": 0.453592,
            "Ounces": 0.0283495
        }
        kg = value * factors[from_unit]
        return kg / factors[to_unit]
    def convert_temperature(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        celsius = value
        if from_unit == "Fahrenheit":
            celsius = (value - 32) * 5/9
        elif from_unit == "Kelvin":
            celsius = value - 273.15
        if to_unit == "Celsius":
            return celsius
        elif to_unit == "Fahrenheit":
            return (celsius * 9/5) + 32
        elif to_unit == "Kelvin":
            return celsius + 273.15
        return 0

    def convert_currency(self, value, from_unit, to_unit):
        rates = {
            "USD": 1.0,
            "EUR": 0.92,
            "GBP": 0.79,
            "INR": 83.50,
            "JPY": 155.0
        }
        usd = value / rates[from_unit]
        return usd * rates[to_unit]
if __name__ == "__main__":
    root = tk.Tk()
    app = UnitConverterApp(root)
    root.mainloop()
