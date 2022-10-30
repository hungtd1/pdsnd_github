import time
import pandas as pd
import numpy as np
#import datetime as dt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    listOfCities = ['chicago', 'new york city', 'washington']
    listOfMonths = ['all', 'january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november','december']
    listOfDays = ['all', 'monday', 'tuesday', 'wednesday','thusday','friday', 'satuday' ,'sunday']
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('Enter City:')
    city = input()
    if city.lower() not in listOfCities:
        city = ''
        print('Cannot found City data: ' + city)


    # get user input for month (all, january, february, ... , june)
    print('Enter Month:')
    month = input()
    if month.lower() not in listOfMonths:
        month = ''
        print('Cannot found Month: '+month)

    # get user input for day of week (all, monday, tuesday, ... sunday)
    print('Enter Day:')
    day = input()
    if day.lower() not in listOfDays:
        day = ''
        print('Cannot found day: ' + day)

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    
    #print('df.count: ' + str(df.count))
    #print(df)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_of_week
    #hungtd1 temp
    """ 
    df.head()
    df
    df['Start Time'].describe()
    df['month']
    df['month'].describe()
    df['day_of_week'].describe()
    df['day_of_week']
    """
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    
    start_time = time.time()
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_of_week
    df['Duration'] = pd.value_counts(df['Trip Duration'])
    df['CountMonth'] = pd.value_counts(df['month'])
    print (df)
    # display the most common month
    print('\nCalculating The Most Frequent Times of Travel...\n')
    groups = df.groupby(['month']).size().reset_index()
    print("1. The most common month: ")
    #print(group[group.Duration == group.Duration.min()])
    #print(groups[groups["month"].count() == 6])

    # plot the result
    #print (df.head())
    #print (df.columns)
    #print (df.describe())
    #print (df.info())
    #print (df['month'].value_counts())
    #print (df['month'].unique())

    popular_Month = df['month'].mode()[0]
    print('The most common month:', popular_Month)
    MaxCount = df.groupby(['month'])['Trip Duration'].count().max()

    print(groups[groups["month"]['Trip Duration'].count() == MaxCount])
    print(MaxCount)
    print(df.groupby(['month'])['Trip Duration'].count().max())
    #commonMonth = df.groupby(['month'])#,['Trip Duration'])
    #print(commonMonth.get_group(6))
    #['Trip Duration'].count()
    #for name,group in commonMonth:
    #    print (name)
    #    print (group)
    #print(commonMonth)
    #print(commonMonth.loc[commonMonth['month'].idxmax()])
    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    invalidInput = False
    while True:
        #HungTD1 comments
        #city, month, day = get_filters()
        city="chicago"
        month='june'
        day='monday'
        if city=='' or month =='' or day =='':
            invalidInput = True
        if not invalidInput:
            #df = load_data(city, month, day)
            df = pd.read_csv(CITY_DATA[city.lower()])
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
