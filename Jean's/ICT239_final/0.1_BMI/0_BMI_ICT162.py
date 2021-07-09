import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
#from SU5.bmiCalculator import BMICalculator

class InvalidDataError(Exception):
    '''Raised when data is out of range'''

class BMICalculator:
    @classmethod
    def heightInRange(cls, height):
        if height < 0.5:
            raise InvalidDataError('Height must be at least 0.5 meters')
        if height > 2.6:
            raise InvalidDataError('Height must not be more than 2.6 meters')
        return True
    
    @classmethod
    def weightInRange(cls, weight):
        if weight < 10:
            raise InvalidDataError('Weight must be at least 10 kilograms')
        if weight > 150:
            raise InvalidDataError('Weight must not be more than 150 kilograms')
        return True
    
    @classmethod
    def bmi(cls, height, weight):
        if cls.heightInRange(height) and cls.weightInRange(weight):
            return weight/(height * height)


class BMIGui:
    def __init__(self):
        self.win = tk.Tk()
        self.win.resizable(False, False)
        # Add a title
        self.win.title("BMI Calculator")
        self.create_widgets()
        self.win.mainloop()
        
    def create_widgets(self):
        
        #Reference Figure 5.4 
    
        # dataFrame (self.win row 0)
        dataFrame = ttk.Frame(self.win) 
        dataFrame.grid(column=0, row=0)    
    
        # (dataFrame row 0)
        wt_lbl = ttk.Label(dataFrame, text="Weight (kilogram):")
        wt_lbl.grid(column=0, row=0, sticky='W')    
        self.weight = tk.StringVar()
        self.wt_Ety = ttk.Entry(dataFrame, width=18, textvariable=self.weight)
        #self.wt_Ety.grid(column=1, row=0, columnspan=2)
        self.wt_Ety.grid(column=1, row=0)
        
        # (dataFrame row 1)
        ht_lbl = ttk.Label(dataFrame, text="Height:")
        ht_lbl.grid(column=0, row=1, sticky='W')

        self.height = tk.StringVar()
        self.ht_Ety = ttk.Entry(dataFrame, width=18, textvariable=self.height)
        #self.ht_Ety.grid(column=1, row=1, columnspan=2)
        self.ht_Ety.grid(column=1, row=1)
        self.radValue = tk.IntVar()
        self.radValue.set(0)
        
        #(dataFrame row 2)
        radioFrame = ttk.Frame(dataFrame)
        radioFrame.grid(column=1, row=2)
        self.ht_m_rdbtn = ttk.Radiobutton(radioFrame, text = 'm', variable=self.radValue, value=0)
        self.ht_cm_rdbtn = ttk.Radiobutton(radioFrame, text = 'cm',
        variable=self.radValue, value=1)
        self.ht_m_rdbtn.grid(column=0, row=0, sticky=tk.W)
        self.ht_cm_rdbtn.grid(column=1, row=0, sticky=tk.W)
        
        #(dataFrame row 3)
        actionFrame = ttk.Frame(dataFrame)
        actionFrame.grid(column=1, row=3, padx=8, pady=4)     
        
        #Within actionFrame, using pack method for layout

        self.calc_btn = ttk.Button(actionFrame, text="Calculate")
        #Event Binding 
        self.calc_btn.bind('<Button-1>', self.calcBMI)
        self.calc_btn.pack(side = tk.LEFT)
    
        self.clear_btn = ttk.Button(actionFrame, text="Clear")
        #Event Binding
        self.clear_btn.bind('<Button-1>', self.clear)
        self.clear_btn.config(state = tk.DISABLED)
        self.clear_btn.pack(side = tk.LEFT)

        # outputFrame (self.win row 1)
        outputFrame = ttk.Frame(self.win)
        outputFrame.grid(column=0, row=1, padx=8, pady=4, columnspan=2)
        scrol_w = 50
        scrol_h = 5
        self.scrol_stxt = scrolledtext.ScrolledText(outputFrame,
        width=scrol_w, height=scrol_h, wrap=tk.WORD)
        self.scrol_stxt.grid(column=0, row=0, sticky='WE', columnspan=2)
        self.scrol_stxt.config(state = tk.DISABLED)
        self.wt_Ety.focus()
    
    def calcBMI(self, event):
        self.scrol_stxt.config(state = tk.NORMAL)
        try:
            h = float(self.height.get())
            if self.radValue.get() == 1:
                h = h/100
            w = float(self.weight.get())
            result = BMICalculator.bmi(h, w)
        except Exception as e:
            self.scrol_stxt.insert('end', str(e) + '\n')
        else:
            self.scrol_stxt.insert('end', f'Weight = {w:.1f}kg, Height = {h:.2f}m, BMI = {result:.2f}\n')
        finally:
            self.scrol_stxt.see('end')
            self.scrol_stxt.config(state = tk.DISABLED)
            self.height.set("")
            self.weight.set("")
            self.wt_Ety.focus()
            self.clear_btn.config(state = tk.NORMAL)
    
    def clear(self, event):
        self.scrol_stxt.config(state = tk.NORMAL)
        print(self.scrol_stxt.get("1.0",tk.END))
        self.scrol_stxt.delete(1.0,tk.END)
        self.scrol_stxt.config(state = tk.DISABLED)
        self.wt_Ety.focus()
        self.clear_btn.config(state = tk.DISABLED)

GUI = BMIGui()
