from countryinfo import CountryInfo
import random

all_countries = CountryInfo().all()
exclude = ['american samoa', 'anguilla', 'aruba', 'bermuda', 'british indian ocean territory', 'cayman islands', 'christmas island', 
           'cocos (keeling) islands', 'republic of the congo', 'falkland islands', 'faroe islands', 'french southern and antarctic lands', 
           'gibraltar', 'greenland', 'guadeloupe', 'guam', 'guernsey', 'heard island and mcdonald islands', 'hong kong', 'jersey', 'macau', 'isle of man', 'martinique', 'mayotte', 
           'montserrat', 'norfolk island', 'northern mariana islands', 'pitcairn islands', 'réunion', 'saint helena', 'saint pierre and miquelon', 
           'south georgia', 'scotland', 'svalbard and jan mayen', 'taiwan', 'tokelau', 'wales', 'wallis and futuna', 'western sahara']


countries = [country for country in all_countries if country not in exclude]
country = random.choice(countries)

capitals = [data['capital'] for country, data in all_countries.items() if country in countries and 'capital' in data]

print(CountryInfo('El Salvador').info())
print(CountryInfo('Burundi').info())