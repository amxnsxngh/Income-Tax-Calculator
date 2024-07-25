from tkinter import *


def tax_calculator():
    income = int(salary_entry.get())*12
    tax = 0
    if 1 < income <= 237100:
        tax = income * (18 / 100)
    elif 237101 <= income <= 370500:
        tax = 42678 + (income - 237100) * (26 / 100)
    elif 370501 <= income <= 512800:
        tax = 77362 + (income - 370500) * (31 / 100)
    elif 512801 <= income <= 673000:
        tax = 121475 + (income - 512800) * (36 / 100)
    elif 673001 <= income <= 857900:
        tax = 179147 + (income - 673000) * (39 / 100)
    elif 857901 <= income <= 1817000:
        tax = 251258 + (income - 857900) * (41 / 100)
    elif 1817001 <= income:
        tax = 644489 + (income - 1817000) * (45 / 100)

    tax = round(tax, 2)
    monthly_tax = tax/12
    monthly_tax = round(monthly_tax, 2)
    if tax_period.get() == 1:
        income_tax.config(text=monthly_tax)
    elif tax_period.get() == 2:
        income_tax.config(text=tax)


def taxing_period():
    print(tax_period.get())


window = Tk()
window.title("Income Tax Calculator")
window.minsize(width=300, height=250)
window.config(padx=50, pady=50)

monthly_salary = Label(text="Please enter your monthly salary:", font=30)
monthly_salary.grid(column=0, row=0)
salary_entry = Entry(width=10)
salary_entry.grid(column=1, row=0)


tax_label = Label(text='Tax period:')
tax_label.grid(column=0, row=1, sticky=W)

tax_period = IntVar()
monthly = Radiobutton(text="Monthly", value=1, variable=tax_period, command=taxing_period)
yearly = Radiobutton(text="Yearly", value=2, variable=tax_period, command=taxing_period)
monthly.grid(column=1, row=1, sticky=W)
yearly.grid(column=1, row=2, sticky=W)


calculate = Button(text='Calculate Income Tax', command=tax_calculator)
calculate.grid(column=0, row=3)

tax_output = Label(text='Income tax:')
tax_output.grid(column=0, row=4)
income_tax = Label(width=10, bd=1, relief='sunken')
income_tax.grid(column=1, row=4)

window.mainloop()


