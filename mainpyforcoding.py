import pandas as pd
import matplotlib.pyplot as plt

#----Global Variables----#
quit = False

#----Setup dataframe and query it here prior to creating visualization and UI functions----#
Covid_df = pd.read_csv('Data/country_wise_latest.csv')

# Cleaned dataset
Covidclean_df = Covid_df.drop(columns=['New deaths', 'New cases', 'New recovered', 'Deaths / 100 Recovered', 'Confirmed last week', '1 week change', '1 week % increase'])

def showOriginalData():
    print(Covid_df)

def showUpdatedData():
    print(Covidclean_df)

def showCharts():
    Covidclean_df.plot(
        kind='barh',  # Horizontal bar graph
        x='Country/Region',
        y='Deaths',
        color='red',
        alpha=0.6
    )
    plt.xlabel('Number of Deaths')
    plt.ylabel('Country/Region')
    plt.title('COVID-19 Deaths per Country')
    plt.show()

def showCountryPieChart(country, ax=None):
    
    country_data = Covid_df[Covid_df['Country/Region'] == country]

    
    deaths = country_data['Deaths'].values[0]
    recoveries = country_data['Recovered'].values[0]

    # Data for the pie graph
    labels = 'Deaths', 'Recoveries'
    sizes = [deaths, recoveries]
    colors = ['red', 'green']
    explode = (0.1, 0)  # explode the 'Deaths' slice


    if ax is not None:
        ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
        ax.set_title(f'COVID-19 Deaths vs Recoveries in {country}')
    else:
        plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
        plt.title(f'COVID-19 Deaths vs Recoveries in {country}')
        plt.show()


def compareCountriesPieChart():
    countries = ['Australia', 'US', 'China', 'United Kingdom', 'India']
    
    print("Please choose the first country to compare:")
    for i, country in enumerate(countries, start=1):
        print(f"{i} - {country}")
    try:
        choice1 = int(input('Enter the number corresponding to your first choice: '))
        country1 = countries[choice1 - 1]
    except (ValueError, IndexError):
        print('Invalid selection. Please enter a number between 1 and 5.')
        return

    print("Please choose the second country to compare:")
    for i, country in enumerate(countries, start=1):
        print(f"{i} - {country}")
    try:
        choice2 = int(input('Enter the number corresponding to your second choice: '))
        country2 = countries[choice2 - 1]
    except (ValueError, IndexError):
        print('Invalid selection. Please enter a number between 1 and 5.')
        return


    fig, axs = plt.subplots(1, 2, figsize=(14, 7))

    # this is here to show graphs side by side
    showCountryPieChart(country1, axs[0])
    showCountryPieChart(country2, axs[1])

    plt.tight_layout()
    plt.show()

# Average deaths per country 
def avg_deaths():
    average_deaths_per_country = Covid_df['Deaths'].mean()
    print(f"The average deaths per country is {average_deaths_per_country:.2f}")

# Average COVID cases per country
def avg_cases():
    average_cases_per_country = Covid_df['Confirmed'].mean()
    print(f"The average confirmed cases per country is {average_cases_per_country:.2f}")

# Average COVID deaths per 100 cases across all countries
def avg_case_deaths():
    average_case_deaths_per_country = Covid_df['Deaths / 100 Cases'].mean()
    print(f"The average deaths per 100 confirmed cases across all countries is {average_case_deaths_per_country:.2f}")

def userOptions():
    global quit

    print("""
          
    Please select an option:
    1 - Show original dataset
    2 - Show cleaned dataset
    3 - Average deaths per country
    4 - Average cases per country
    5 - Average deaths per 100 cases across all countries
    6 - Show deaths per country graph
    7 - Compare deaths vs recoveries between two countries
    8 - Quit Program
        """)
    try: 
        choice = int(input('Enter Selection: '))

        if choice == 1:
            showOriginalData()
        
        elif choice == 2:
            showUpdatedData()

        elif choice == 3:
            avg_deaths()
        
        elif choice == 4:
            avg_cases()
        
        elif choice == 5:
            avg_case_deaths()

        elif choice == 6:
            showCharts()

        elif choice == 7:
            compareCountriesPieChart()

        elif choice == 8:
            quit = True
        else:
            print('Please enter a number between 1 and 8.')

    except ValueError:
        print('Please enter a number between 1 and 8.')


while not quit:
    userOptions()