## Indicateurs page monde

#url des données utilisées pour les indicateurs : cas,décès,
covid_monde_url = (
    "https://covid19.who.int/WHO-COVID-19-global-data.csv"
    )

covid_monde = pd.read_csv(covid_monde_url, sep=",")

#url des données utilisées pour les indicateurs de vaccination
covid_monde_vaccination_url = (
        "https://covid19.who.int/who-data/vaccination-data.csv"
        )

covid_monde_vaccination = pd.read_csv(covid_monde_vaccination_url, sep=",")

#somme des cas depuis le début de la pandémie
sum_cases = covid_monde['New_cases'].sum() 

#somme des décès depuis le début de la pandémie
sum_deaths = covid_monde['New_deaths'].sum()

#somme des vaccinations depuis le début de la pandémie
sum_vaccination = covid_monde_vaccination['TOTAL_VACCINATIONS'].sum()

#il s'agit de la dernière date renseignées dans la base de données
date_recente = max(covid_monde['Date_reported'])

#nouvelle base de données contenant uniquement les données de la dernière date
covid_monde_last_day = covid_monde[covid_monde.Date_reported == date_recente]

# somme des cas pour le dernier jour renseigné dans la base
sum_cases_last_day = covid_monde_last_day['New_cases'].sum()

# somme des décès pour le dernier jour renseigné dans la base
sum_deaths_last_day = covid_monde_last_day['New_deaths'].sum()

#Voir pour l'indicateur de vaccination au jour le jour car les données ne le permettent pas
