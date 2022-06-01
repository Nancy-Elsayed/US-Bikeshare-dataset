import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    
    while True:
        city= input('kindly type a city from below to view its data \nChicago \nNew York \nWashington \n').lower()

        if city not in CITY_DATA.keys():
        
            print('try again with a name in the list ')
            city= input('\nkindly type a city from below to view its data \nChicago \nNew York \nWashington \n').lower()
                           
        else:
            print (city)
            break
               
          # TO DO: get user input for month (all, january, february, ... , june)
           
    while True:
        months=['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'all']
        month=input('to filter the month,choose: \njan \nfeb \nmar \napr \nmay \njun \nall \n').lower()
        if month not in months:
        
            print('try again with a month in the list')
            month=input('to filter the month,choose: \njan \nfeb \nmar \napr \nmay \njun \nall \n').lower()
            
        else:
            print(month)
            break
              
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days=['Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'All']
        day=input('Do you want a specific day? choose: \nSat \nSun \nMon\nTue \nWed \nThu \nFri \nAll \n').lower()
        if month not in months:
        
            print('try again with a day in the list')
            day=input('Do you want a specific day? choose: \nSat \nSun \nMon\nTue \nWed \nThu \nFri \nAll \n').lower()
            
        else:
            print(day)
            break
    print ('You choose:', city, month, day)        
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
    
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

# convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

# extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
# filter by month if applicable
    if month != 'all':
# use the index of the months list to get the corresponding int
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
        month = months.index(month) + 1
        
# filter by month to create the new dataframe
        df = df[df['month'] == month]
        
# filter by day of week if applicable
    if day != 'all':
# filter by day of week to create the new dataframe
        df = df[df['day_of_week'].str.startswith(day.title())]
        
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    #check
    #if df['month']  in [1,2,3,4,5,6]:
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month)
    print('-'*40)
    #else:
     #   print('No most common month! You are showing data for a specific month!')
    # TO DO: display the most common day of week
    #if df['day_of_week']  in ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Day:', popular_day)
    print('-'*40)
    #else:
       # print('No most common day! You are showing data for a specific day!') 
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)
    print('-'*40)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station)
    print('-'*40)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station)
    print('-'*40)

    # TO DO: display most frequent combination of start station and end station trip
    Trip_column = df['Start Station'] + df['End Station']
    df['Trip_column']=Trip_column
    popular_trip = df['Trip_column'].mode()[0]
    print('Most Popular Trip:', popular_trip)
    print('-'*40)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
       
    total_times = df['Trip Duration'].sum()
    print('Total travel time:', total_times)
    print('-'*40)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # TO DO: display mean travel time
    mean_times = df['Trip Duration'].mean()
    print('Mean Trip time:',mean_times)
    print('-'*40)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)    

    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_count = df['User Type'].value_counts()
    print('Users Breakdown:', user_count)
    print('-'*40)
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        common_gender=df['Gender'].mode()
        print("most common gender", common_gender )
        print('-'*40)
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        common_year=df['Birth Year'].mode()
        print("most common year of birth", common_year)
        earliest=df['Birth Year'].max()
        print ('Oldest user born in:',earliest)
        mostrecent= df['Birth Year'].min()
        print ('Youngest user born in:', mostrecent)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

   
def display_raw_data(city):
   
    df = pd.read_csv(CITY_DATA[city])

    print('\nRaw data is available to check... \n')
    start_loc = 0
    while True:
        display_opt = input('To View the availbale raw data in chuncks of 5 rows type: Yes, if No, filtering will start again \n').lower()
        if display_opt not in ['yes', 'no']:
            print('That\'s invalid choice, please type yes or no')

        elif display_opt == 'yes':
            print(df.iloc[start_loc:start_loc+5])
            start_loc+=5

        elif display_opt == 'no':
            print('\nExiting...')
            break
                           
        

def main():
    while True:
        city, month, day = get_filters()
                    
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data (city)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
