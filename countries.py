from countryinfo import CountryInfo
import random
from tkinter import *

def start_quiz():
    welcome_label.grid_forget()
    start_button.grid_forget()
    generate_country()

def generate_country():    
    all_countries = CountryInfo().all()
    exclude = ['american samoa', 'anguilla', 'aruba', 'bermuda', 'british indian ocean territory', 'cayman islands', 'christmas island', 
           'cocos (keeling) islands', 'republic of the congo', 'falkland islands', 'faroe islands', 'french southern and antarctic lands', 
           'gibraltar', 'greenland', 'guadeloupe', 'guam', 'guernsey', 'heard island and mcdonald islands', 'hong kong', 'jersey', 'macau', 'isle of man', 'martinique', 'mayotte', 
           'montserrat', 'norfolk island', 'northern mariana islands', 'pitcairn islands', 'réunion', 'saint helena', 'saint pierre and miquelon', 
           'south georgia', 'scotland', 'svalbard and jan mayen', 'taiwan', 'tokelau', 'wales', 'wallis and futuna', 'western sahara']
    countries = [country for country in all_countries if country not in exclude]
    country = random.choice(countries).title()
    country_label = Label(root, text=country, font=("Arial", 22))
    country_label.grid(column=1,row=1)
    generate_capitals(all_countries, countries, country)
    return all_countries, countries, country

def generate_capitals(all_countries, countries, country):
    correct_capital = all_countries[country.lower()]['capital']
    capitals = [data['capital'] for country, data in all_countries.items() if country in countries and 'capital' in data]
    wrong_capitals = []

    while len(wrong_capitals) < 3:
        capital = random.choice(capitals).title()
        wrong_capitals.append(str(capital))
    
    choices = [str(capital) for capital in wrong_capitals] + [str(correct_capital)]
    random.shuffle(choices)
    choices_buttons = []
    for idx, choice in enumerate(choices):
        button = Button(root, text=choice, width=20)
        button.grid(column=1, row=2+idx)
        choices_buttons.append(button)
    


root = Tk()
root.title('Capital Cities Quiz by Cindy Bond')
root.config(padx=100, pady=50, bg='#0487bf')

welcome_label = Label(root, text='Welcome to the Capital Cities Quiz! See how many capitals you can answer correctly in 2 minutes!', bg='#0487bf')
welcome_label.grid(column=1, row=1)

start_button = Button(root, text='Start Quiz', command = start_quiz)
start_button.grid(column=1, row=2)


root.mainloop()

