#----Modules----#
import pandas as pd
import matplotlib.pyplot as plt

#----Global Variables----#
quit = False

#----Setup dataframe and query it here prior to creating visualisation and UI functions----#
original_df = pd.read_csv(country_wise_latest.csv')

big_mac_df = pd.read_csv('ct-test-3\country_wise_latest.csv',)
                            header=None,
                            names=['Country', 'Confirmed cases', 'Deaths', 'Recovered','Deaths / 100 cases', 'Recovered / 100 Cases']