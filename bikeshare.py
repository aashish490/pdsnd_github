import time
import pandas as pd
import numpy as np

# available cities
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_keys = CITY_DATA.keys()
    valid_city = False
    print(city_keys)
    while valid_city == False:
        try:
            city = input("Enter the city you wish to see the data for, we have data for 'chicago', 'new york city'and 'washington' city:")
        except:
            print("Incorrect input. Please try again.")
        finally:
            if(city in city_keys):
                valid_city = True
            else:
                print("We could not find the exact name in the mentioned city names. Please try again.")

    print('\nYou entered:', city)

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june']
#     month = months.index(month) + 1
    valid_month = False
    while valid_month == False:
        try:
            month = input("Please enter the month(e.g. january) or 'all' if you wish to see results for whole data:")
            if(month == 'all'):
                valid_month = True
            elif(months.index(month) + 1 > 0):
                month= months.index(month) + 1
                valid_month = True
            else:
                print("That didnt work. Please try entering the month again.\nWe have data for 'january', 'february', 'march', 'april', 'may', 'june'\n")
        except:
            print("\nError occurred. We have data for 'january', 'february', 'march', 'april', 'may', 'june'\n")
        finally:
            print("You entered: {}".format(month))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['M', 'Tu', 'W', 'Th', 'F', 'Sa', 'Su']
    valid_day = False
    while valid_day == False:
        try:
            day = input("Please enter the day(e.g. 'M', 'Tu', 'W', 'Th', 'F', 'Sa', 'Su') or 'all' if you wish to see results for whole data:")
            if(day == 'all'):
                valid_day = True
            elif(days.index(day) + 1 > 0):
                valid_day = True
                day= days.index(day) + 1
            else:
                print("\nThat didnt work. Please try entering the day again.\nPlease enter one from 'M', 'Tu', 'W', 'Th', 'F', 'Sa', 'Su'\n")
        except:
            print("\nError occurred. Please enter one from 'M', 'Tu', 'W', 'Th', 'F', 'Sa', 'Su'\n")
        finally:
            print('\nYou entered day:', day)

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
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    if(month != 'all'):
        df = df[df['month'] == month]
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    print(df)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    print('Month: {}'.format(df['month'].mode()[0]))


    # TO DO: display the most common day of week
    print('Day of week: {}'.format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print('Hour: {}'.format(df['Start Time'].dt.hour.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
#     print(df['Start Station'].value_counts())
    print('Start Station: {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
#     print(df['End Station'].value_counts())
    print('End Station: {}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['Station Combo'] = df['Start Station'] + ' + ' + df['End Station']
#     print(df['Station Combo'].value_counts())
    print('Most Popular Start and End Station Combo: {}'.format(df['Station Combo'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Time Taken'] = pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])
    print('Total travel time : {}'.format(df['Time Taken'].sum()))

    # TO DO: display mean travel time
    print('Mean travel time : {}'.format(df['Time Taken'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('User type counts : {}\n'.format(df['User Type'].value_counts()))


    # TO DO: Display counts of gender
    print('Gender Counts : {}/n'.format(df['Gender'].value_counts()))

    # TO DO: Display earliest, most recent, and most common year of birth
    print('Earliest Birth: {}'.format(df['Birth Year'].min()))
    print('Most Recent Birth: {}'.format(df['Birth Year'].max()))
    print('Most Common Birth year: {}'.format(df['Birth Year'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
