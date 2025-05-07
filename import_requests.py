import requests
import json
from datetime import datetime, timedelta

countries=('Afghanistan','Albania','Algeria','Andorra','Angola','Antigua and Barbuda',
'Argentina','Armenia','Australia','Austria','Azerbaijan','Bahamas','Bahrain','Bangladesh',
'Barbados','Belarus','Belgium','Belize','Benin','Bhutan','Bolivia','BosniaandHerzegovina',
'Botswana','Brazil','Brunei','Bulgaria','BurkinaFaso',
'Burundi','CaboVerde(CapeVerde)','Cambodia','Cameroon','Canada','CentralAfricanRepublic',
'Chad','Chile','China','Colombia','Comoros','DemocraticRepublicoftheCongo','RepublicoftheCongo',
'CostaRica',"Côted'Ivoire(IvoryCoast)",'Croatia','Cuba','Cyprus','CzechRepublic','Denmark',
'Djibouti','Dominica','DominicanRepublic','Ecuador','Egypt','ElSalvador','EquatorialGuinea',
'Eritrea','Estonia','Eswatini(Swaziland)','Ethiopia','Fiji','Finland','France','Gabon','Gambia',
'Georgia','Germany','Ghana','Greece','Grenada','Guatemala','Guinea','Guinea-Bissau','Guyana',
'Haiti','Honduras','Hungary','Iceland','India','Indonesia','Iran','Iraq','Ireland','Israel',
'Italy','Jamaica','Japan','Jordan','Kazakhstan','Kenya','Kiribati','Kuwait','Kyrgyzstan',
'Laos','Latvia','Lebanon','Lesotho','Liberia','Libya','Liechtenstein','Lithuania','Luxembourg')

array_of_json_objects = []
for country in countries:
    url=f'''https://disease.sh/v3/covid-19/countries/{country}'''
    response=requests.get(url)
    if response.status_code == 200:
        array_of_json_objects.append(response.json())
    else:
        print(f"Error fetching data from API for country {country}")

# Extracting the required data
file_path=f"extracted_data/covid_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
with open(file_path, 'w') as file:
    json.dump(array_of_json_objects, file, indent=2)
    
print(f"Data extracted and saved to {file_path}")
