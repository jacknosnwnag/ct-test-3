#----Modules----#
import pandas as pd
import matplotlib.pyplot as plt

#----Global Variables----#
quit = False

#----Setup dataframe and query it here prior to creating visualisation and UI functions----#
Covid_df = pd.read_csv('data\country_wise_latest.csv')
header=None,
names=['Country', 'Confirmed cases', 'Deaths', 'Recovered','Deaths / 100 cases', 'Recovered / 100 Cases']
Covid_df = Covid_df.drop(columns=['New deaths', 'New cases','New recovered','Deaths / 100 Recovered', 'Confirmed last week','1 week change','1 week % increase' ])
     
print(Covid_df)

#Analysis of Data

#Average deaths per country 
def avg_deaths():
    average_deaths_per_country = Covid_df['Deaths'].mean()
    print(average_deaths_per_country)

#Average COVID cases per country
def avg_cases():
    average_cases_per_country = Covid_df['Confirmed'].mean()
    print(average_cases_per_country)

#Average COVID deaths per 100 cases across all countries
def avg_case_deaths():
    average_case_deaths_per_country = Covid_df['Deaths / 100 Cases'].mean()
    print(average_case_deaths_per_country)



def userOptions():
    global quit

    print("""Greetings user, I see you are here to analyse COVID data!
          
    Please select an option:
    1 - ("Average deaths per country")
    2 - ("Average cases per country")
    3 - ("Average deaths per 100 cases across all)
    4 - Quit Program
        """)
    
    try:
        choice = int(input('Enter Selection: '))

        if choice == 1:
            avg_deaths()
           
        elif choice == 2:
            avg_cases()
          
        elif choice == 3:
            avg_case_deaths()

        elif choice == 4:
            quit = True
        else:
            print('Please enter a number between 1 and 4.')

    except:
        print('Please enter a number between 1 and 4.')

while not quit:
    userOptions()


a
   

