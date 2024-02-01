import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#importing files
dailyActivity_merged=pd.read_csv(r"F:\dataanalytics project\Fitabase Data 4.12.16-5.12.16\dailyActivity_merged.csv")
dailyCalories_merged=pd.read_csv(r"F:\dataanalytics project\Fitabase Data 4.12.16-5.12.16\dailyCalories_merged.csv")
dailyIntensities_merged=pd.read_csv(r"F:\dataanalytics project\Fitabase Data 4.12.16-5.12.16\dailyIntensities_merged.csv")
dailySteps_merged=pd.read_csv(r"F:\dataanalytics project\Fitabase Data 4.12.16-5.12.16\dailySteps_merged.csv")
heartrate_seconds_merged=pd.read_csv(r"F:\dataanalytics project\Fitabase Data 4.12.16-5.12.16\heartrate_seconds_merged.csv")
hourlyCalories_merged=pd.read_csv(r"F:\dataanalytics project\Fitabase Data 4.12.16-5.12.16\hourlyCalories_merged.csv")
hourlyIntensities_merged=pd.read_csv(r"F:\dataanalytics project\Fitabase Data 4.12.16-5.12.16\hourlyIntensities_merged.csv")
hourlySteps_merged=pd.read_csv(r"F:\dataanalytics project\Fitabase Data 4.12.16-5.12.16\hourlySteps_merged.csv")
minuteCaloriesNarrow_merged=pd.read_csv(r"F:\dataanalytics project\Fitabase Data 4.12.16-5.12.16\minuteCaloriesNarrow_merged.csv")
minuteCaloriesWide_merged=pd.read_csv(r"F:\dataanalytics project\Fitabase Data 4.12.16-5.12.16\minuteCaloriesWide_merged.csv")
minuteIntensitiesNarrow_merged=pd.read_csv(r"F:\dataanalytics project\Fitabase Data 4.12.16-5.12.16\minuteIntensitiesNarrow_merged.csv")
minuteIntensitiesWide_merged=pd.read_csv(r"F:\dataanalytics project\Fitabase Data 4.12.16-5.12.16\minuteIntensitiesWide_merged.csv")
minuteMETsNarrow_merged=pd.read_csv(r"F:\dataanalytics project\Fitabase Data 4.12.16-5.12.16\minuteMETsNarrow_merged.csv")
minuteSleep_merged=pd.read_csv(r"F:\dataanalytics project\Fitabase Data 4.12.16-5.12.16\minuteSleep_merged.csv")
minuteStepsNarrow_merged=pd.read_csv(r"F:\dataanalytics project\Fitabase Data 4.12.16-5.12.16\minuteStepsNarrow_merged.csv")
minuteStepsWide_merged=pd.read_csv(r"F:\dataanalytics project\Fitabase Data 4.12.16-5.12.16\minuteStepsWide_merged.csv")
sleepDay_merged=pd.read_csv(r"F:\dataanalytics project\Fitabase Data 4.12.16-5.12.16\sleepDay_merged.csv")
weightLogInfo_merged=pd.read_csv(r"F:\dataanalytics project\Fitabase Data 4.12.16-5.12.16\weightLogInfo_merged.csv")



#understanding their structures
# List of DataFrames
dataframes = [dailyActivity_merged, dailyCalories_merged, dailyIntensities_merged,
               dailySteps_merged, heartrate_seconds_merged, hourlyCalories_merged,
               hourlyIntensities_merged, hourlySteps_merged, minuteCaloriesNarrow_merged,
               minuteCaloriesWide_merged, minuteIntensitiesNarrow_merged, minuteIntensitiesWide_merged,
               minuteMETsNarrow_merged, minuteSleep_merged, minuteStepsNarrow_merged,
               minuteStepsWide_merged, sleepDay_merged, weightLogInfo_merged]

# Print the structure of each DataFrame
for df in dataframes:
    print(df.info())
    print('\n' + '='*50 + '\n')  # Separating each DataFrame's info for better readability




#cleaning data
for df in dataframes:
    # Remove duplicates
    df.drop_duplicates(inplace=True)
    
    # Handle null values
    df.dropna(inplace=True)


# List of dataframes to verify against
dataframes_to_verify = [dailyCalories_merged, dailyIntensities_merged, dailySteps_merged,
                        heartrate_seconds_merged, hourlyCalories_merged, hourlyIntensities_merged,
                        hourlySteps_merged, minuteCaloriesNarrow_merged, minuteCaloriesWide_merged,
                        minuteIntensitiesNarrow_merged, minuteIntensitiesWide_merged, minuteMETsNarrow_merged,
                        minuteSleep_merged, minuteStepsNarrow_merged, minuteStepsWide_merged, sleepDay_merged,
                        weightLogInfo_merged]


# Check each dataframe against dailyActivity_merged
for df in dataframes_to_verify:
    common_columns = set(dailyActivity_merged.columns) & set(df.columns)
    matching_ids = dailyActivity_merged['Id'].equals(df['Id'])
    
    if common_columns and matching_ids:
        print(f"Dataframe: {df}")
        print(f"Common Columns: {common_columns}")
        print(f"Matching IDs: {matching_ids}")

        common_columns_values = dailyActivity_merged[common_columns].equals(df[common_columns])
        print(f"Matching Data Values for Common Columns: {common_columns_values}")

        print(f"Sample rows from dailyActivity_merged:")
        print(dailyActivity_merged[common_columns].head())

        print(f"Sample rows from other_dataframe:")
        print(df[common_columns].head())
        print("="*50)





#analysis
#1.summarizing some of the daily usage



        
# Selecting specific columns
selected_columns = ['TotalSteps', 'TotalDistance', 'SedentaryMinutes', 'Calories']

# Creating a subset of the dataframe with selected columns
subset_daily_activity = dailyActivity_merged[selected_columns]

# Using the describe method for summary statistics
summary_statistics = subset_daily_activity.describe()

# Displaying the summary statistics
print(summary_statistics)
print(sleepDay_merged.describe())
print(weightLogInfo_merged.describe())
print(heartrate_seconds_merged.describe())




'''

#2.verifying correlation between steps and calories burned



selected_columns = ['TotalSteps', 'Calories']
subset_dataframe = dailyActivity_merged[selected_columns].dropna()  # Drop rows with missing values
sns.regplot(x='TotalSteps', y='Calories', data=subset_dataframe)

# Adding labels and title
plt.title("Total Steps vs. Calories")
plt.xlabel("Total Steps")
plt.ylabel("Calories")
plt.legend()

# Display the plot
plt.show()






#3.analyzing no of steps per weekday




dailyActivity_merged['ActivityDate'] = pd.to_datetime(dailyActivity_merged['ActivityDate'])

# Extracting day of the week and setting the order
dailyActivity_merged['weekday'] = dailyActivity_merged['ActivityDate'].dt.strftime('%A')
weekday_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
dailyActivity_merged['weekday'] = pd.Categorical(dailyActivity_merged['weekday'], categories=weekday_order, ordered=True)

# Grouping by weekday and calculating mean steps
weekday_steps = dailyActivity_merged.groupby('weekday')['TotalSteps'].mean().reset_index()

# Plotting the data
plt.figure(figsize=(10, 6))
sns.barplot(x='weekday', y='TotalSteps', data=weekday_steps, palette="viridis")
plt.axhline(y=7500, color='red', linestyle='--', label='Threshold (7500 steps)')
plt.title('Daily Steps per Weekday')
plt.xlabel('Weekday')
plt.ylabel('Daily Steps')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.show()



#4.analyzing sleeping hours per weekday




sleepDay_merged['SleepDay'] = pd.to_datetime(sleepDay_merged['SleepDay'])

# Extracting day of the week and setting the order
sleepDay_merged['weekday'] = sleepDay_merged['SleepDay'].dt.strftime('%A')
weekday_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
sleepDay_merged['weekday'] = pd.Categorical(sleepDay_merged['weekday'], categories=weekday_order, ordered=True)

# Grouping by weekday and calculating mean sleep duration
weekday_sleep = sleepDay_merged.groupby('weekday')['TotalMinutesAsleep'].mean().reset_index()

# Plotting the data
plt.figure(figsize=(10, 6))
sns.barplot(x='weekday', y='TotalMinutesAsleep', data=weekday_sleep, palette="pastel")
plt.axhline(y=480, color='red', linestyle='--', label='Threshold (480 minutes)')
plt.title('Minutes Asleep per Weekday')
plt.xlabel('Weekday')
plt.ylabel('Minutes Asleep')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.show()




# 5.analyzing hourly intensities



hourlyIntensities_merged['ActivityHour'] = pd.to_datetime(hourlyIntensities_merged['ActivityHour'], format='%m/%d/%Y %I:%M:%S %p')

# Splitting into date and time
hourlyIntensities_merged['date'] = hourlyIntensities_merged['ActivityHour'].dt.date
hourlyIntensities_merged['time'] = hourlyIntensities_merged['ActivityHour'].dt.time

# Grouping by time and calculating mean total intensity
hourly_intensities = hourlyIntensities_merged.groupby('time').agg(mean_total_int=('TotalIntensity', 'mean')).reset_index()

# Plotting the data
plt.figure(figsize=(12, 6))
sns.barplot(x='time', y='mean_total_int', data=hourly_intensities, color='purple')
plt.title('Average Total Intensity vs. Time')
plt.xlabel('Time')
plt.ylabel('Mean Total Intensity')
plt.xticks(rotation=90)
plt.show()





#6.hourly steps throughout the day 



if not hourlySteps_merged['ActivityHour'].empty:
    # Convert 'ActivityHour' to datetime format
    hourlySteps_merged['ActivityHour'] = pd.to_datetime(hourlySteps_merged['ActivityHour'], format='%m/%d/%Y %I:%M:%S %p')

    # Extracting date and time
    hourlySteps_merged['date'] = hourlySteps_merged['ActivityHour'].dt.strftime('%Y-%m-%d')
    hourlySteps_merged['time'] = hourlySteps_merged['ActivityHour'].dt.strftime('%H:%M:%S')

    # Grouping by time and calculating mean steps
    hourly_steps_grouped = hourlySteps_merged.groupby('time')['StepTotal'].mean().reset_index()

    # Plotting the data
    plt.figure(figsize=(12, 6))
    sns.barplot(x='time', y='StepTotal', data=hourly_steps_grouped, palette='RdYlGn_r')
    plt.title('Hourly Steps Throughout the Day')
    plt.xlabel('Time')
    plt.ylabel('Average Steps')
    plt.xticks(rotation=90)
    plt.show()
else:
    print("Error: 'ActivityHour' column is empty.")


'''



