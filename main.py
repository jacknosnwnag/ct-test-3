#----Modules----#
import pandas as pd
import matplotlib.pyplot as plt

#----Global Variables----#
quit = False

#----Setup dataframe and query it here prior to creating visualisation and UI functions----#
Covid_df = pd.read_csv('data\country_wise_latest.csv')
header=None,
names=['Country', 'Confirmed cases', 'Deaths', 'Recovered','Deaths / 100 cases', 'Recovered / 100 Cases']
Covidclean_df = Covid_df.drop(columns=['New deaths', 'New cases','New recovered','Deaths / 100 Recovered', 'Confirmed last week','1 week change','1 week % increase' ])
     
print(Covidclean_df)

def showOriginalData():
    print(Covid_df)

def showUpdatedData():
    print(Covidclean_df)

def showCharts():
    Covidclean_df.plot(
                    kind='bar',
                    x='Country',
                    y='AUD',
                    color='blue',
                    alpha=0.3,
                    title='Cost of a Big Mac in AUD')
    plt.show()