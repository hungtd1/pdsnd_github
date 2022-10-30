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

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_of_week

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
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_of_week

    print('\n1.Calculating The Most Frequent Times of Travel...\n')
    # display the most common month
    popular_Month = df['month'].mode()[0]
    print("   1.1. The most common month: ",popular_Month)

   
    # display the most common day of week
    popular_Day = df['day_of_week'].mode()[0]
    print("   1.2. The most common Day of week: ", popular_Day)

    # display the most common start hour
    popular_Hour = df['hour'].mode()[0]
    print("   1.3. Tmost common hour of day: ", popular_Hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\n2. Calculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_StartStation = df['Start Station'].mode()[0]
    print("   2.1. The most common Start Station: ",popular_StartStation)


    # display most commonly used end station
    popular_EndStation = df['End Station'].mode()[0]
    print("   2.2. The most common End Station: ",popular_EndStation)


    # display most frequent combination of start station and end station trip
    df['StartEndStation'] = df['Start Station'] + ' - ' + df['End Station']
    popular_StartEndStation = df['StartEndStation'].mode()[0]
    print("   2.3. The most common start - end station : ",popular_StartEndStation)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """2. Displays statistics on the total and average trip duration."""

    print('\n3.Calculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    totaltime = df['Trip Duration'].sum()
    print("   3.1.total travel time : ",totaltime)

    # display mean travel time

    meantime = df['Trip Duration'].mean()
    print("   3.2.mean travel time : ",meantime)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""   

    print('\n4.Calculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    countUserType = df.groupby(['User Type'])['User Type'].count()
    print("   4.1.counts of user types : ",countUserType)
    # Display counts of gender
    countGender = df.groupby(['Gender'])['Gender'].count()
    print("   4.2.counts of Gender : ",countGender)

    # Display earliest, most recent, and most common year of birth
    earliest = min(df['Birth Year'])
    print("   4.3.earliest year of birth : ", earliest)
    recent = max(df['Birth Year'])
    print("   4.4.recent year of birth : ", recent)
    mostcommonyear = df['Birth Year'].mode()[0]
    print("   4.5.most common year : ", mostcommonyear)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    invalidInput = False
    while True:
        #HungTD1 comments
        '''
        city, month, day = get_filters()
        if city=='' or month =='' or day =='':
            invalidInput = True
        if not invalidInput:
            df = load_data(city, month, day)
        '''  
        city="chicago"  
        df = pd.read_csv(CITY_DATA[city])
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
