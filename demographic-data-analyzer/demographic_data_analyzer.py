import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    datafile = pd.read_csv('adult.data.csv')
    datafile.columns = ['Age', 'workclass', 'fnlwgt', 'AcademicDegree', 'education-num',
                        'marital-status', 'occupation', 'relationship', 'race', 'gender',
                        'capital-gain', 'capital-loss', 'HoursPerWeek', 'country', 'Salary']

    datafile = datafile.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = datafile['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(datafile[datafile['gender']=='Male']['Age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?

    Bachelors_count = datafile[datafile['AcademicDegree'] == 'Bachelors'].shape[0]
    Academics_count = datafile["AcademicDegree"].count()
    percentage_bachelors = round((Bachelors_count / Academics_count) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    a_educationOver50 = datafile[
        (datafile['AcademicDegree'].isin(["Bachelors", "Masters", "Doctorate"])) & (datafile['Salary'] == '>50K')]
    higher_education = datafile[(datafile['AcademicDegree'].isin(["Bachelors", "Masters", "Doctorate"]))]
    a_education_count = higher_education.shape[0]
    a_educationOver50_count = a_educationOver50.shape[0]

    no_educationOver50 = datafile[
        (~datafile['AcademicDegree'].isin(["Bachelors", "Masters", "Doctorate"])) & (datafile['Salary'] == '>50K')]
    lower_education = datafile[(~datafile['AcademicDegree'].isin(["Bachelors", "Masters", "Doctorate"]))]
    no_education_count = lower_education.shape[0]
    no_educationOver50_count = no_educationOver50.shape[0]

    # percentage with salary >50K
    higher_education_rich = round((a_educationOver50_count / a_education_count) * 100, 1)
    lower_education_rich = round((no_educationOver50_count / no_education_count) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = round(datafile['HoursPerWeek'].min(), 1)

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    minwork_highMoney = datafile[(datafile['HoursPerWeek'] == min_work_hours) & (datafile['Salary'] == '>50K')].shape[0]
    num_min_workers = datafile[(datafile['HoursPerWeek'] == min_work_hours)].shape[0]

    rich_percentage = round((minwork_highMoney / num_min_workers) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    dvalidcountries = datafile[datafile['country'] != '?']
    dvc_count = dvalidcountries['country'].value_counts()
    highpaids = dvalidcountries[dvalidcountries['Salary'] == '>50K']
    highpaids_count = highpaids.groupby('country').size().sort_values(ascending=False)
    highpaids_percantage = ((highpaids_count / dvc_count) * 100).sort_values(ascending=False)
    highest_earning_country = highpaids_percantage.idxmax()
    highest_earning_country_percentage = round(highpaids_percantage.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    popular_occupations = datafile[(datafile['country'] == 'India') & (datafile['Salary'] == '>50K')].groupby(
        ['occupation']).size().sort_values(ascending=False)
    top_IN_occupation = popular_occupations.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
            highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
