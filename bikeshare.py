import time
import pandas as pd
import numpy as np
# adding calendar to be used in time stats
import calendar as cal

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to write a city, month, and day to analyze.
    Args:
        None.
    Returns:
        str (city): city name to analyze
        str (month): month to filter by, or "all" to apply no month filter
        str (day): name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please Select one of the city between Chicago, New York City or Washington: ").lower()

    while city not in ['chicago', 'new york city', 'washington']:
        print('Not Valid')
        city = input("Please Select one of the city between Chicago, New York City or Washington again: ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please Select a month between January till June or say all: ").lower()
    while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        print('Not Valid')
        month = input("Please Select a month between January till June again: ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please Select a day of the week or say all: ").lower()
    while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
        print('Not Valid')
        day = input("Please Select the day of the week again: ").lower()

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if available.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df: Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month day and hour of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

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
    """Displays statistics on the most frequent times of travel.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None.
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    most_common_month_name = cal.month_name[most_common_month]

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]

    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]

    print('Most common month of travel:', most_common_month_name)
    print('Most common day of travel:', most_common_day)
    print('Most common start hour of travel:', most_common_start_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None.
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    df['start end station'] = df['Start Station'] + ' and ' + df['End Station']
    popular_start_end_station = df['start end station'].mode()[0]

    print('Most commonly used start station:', popular_start_station)
    print('Most commonly used end station :', popular_end_station)
    print('Most frequent combination of start station and end station trip :', popular_start_end_station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None.
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time : ', total_travel_time, 'seconds.')

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean of travel time : ', mean_travel_time, 'seconds.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None.
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_user_types = df['User Type'].value_counts()

    print('Counts of user types:\n', counts_user_types, '\n')

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        counts_gender = df['Gender'].value_counts()
        print('Counts of gender:\n', counts_gender, '\n')
    else:
        print('Information in Gender is not available')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_yob = int(df['Birth Year'].min())
        most_recent_yob = int(df['Birth Year'].max())
        most_common_yob = int(df['Birth Year'].mode())
        print('Earliest year of birth: ', earliest_yob)
        print('Most recent year of birth: ', most_recent_yob)
        print('Most common year of birth: ', most_common_yob)
    else:
        print('Information in Birth Year is not available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#Function to display the data frame itself as per user request
def display_data(df):
    """Displays 5 rows of data from the csv file for the selected city.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None.
    """
    BIN_RESPONSE_LIST = ['yes', 'no']
    rdata = ''
    #counter variable is initialized as a tag to ensure only details from
    #a particular point is displayed
    counter = 0
    while rdata not in BIN_RESPONSE_LIST:
        print("\nDo you wish to view the raw data?")
        print("\nAccepted responses:\nYes or yes\nNo or no")
        rdata = input().lower()
        #the raw data from the df is displayed if user opts for it
        if rdata == "yes":
            print(df.head())
        elif rdata not in BIN_RESPONSE_LIST:
            print("\nPlease check your input.")
            print("Input does not seem to match any of the accepted responses.")
            print("\nRestarting...\n")

    #Extra while loop here to ask user if they want to continue viewing data
    while rdata == 'yes':
        print("Do you wish to view another 5 lines of raw data?")
        counter += 5
        rdata = input().lower()
        #If user opts for it, this displays next 5 rows of data
        if rdata == "yes":
             print(df[counter:counter+5])
        elif rdata != "yes":
             break

    print('-'*80)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
