import pandas as pd
import matplotlib.pyplot as plt

DF = pd.read_csv('data.csv')

### show all duplicates
print(DF.duplicated())

### convert string to date time
DF['Hire Date'] = pd.to_datetime(DF['Hire Date'])

### fill empty data with avg of their respective column
# DF.fillna(avg_age, inplace=True)

### Column-wise modifying
DF['Age'] = DF['Age'].fillna(DF['Age'].mean())

#average of age
def avg_age():
    avg_age = DF['Age'].mean()
    print(f"Average age is: {avg_age}")


## average of salary
def avg_salary():
    avg_sal = DF['Salary'].mean()
    print(f"Average Salary is {avg_sal} ruppees.")

### column names
def column_names():
    columns = DF.columns.tolist()
    print(f"The columns are: ")
    for col in columns:
        print(col)


### shape of data
def shape_of_data():
    print(f"Shape of data: {DF.shape}")


### Sorted order of Salary
def sort_sal():
    salary_des = DF.sort_values(by='Salary', ascending=False)
    print(salary_des[['Name', 'Salary']].reset_index(drop=True))

### Graph of Salary
def graph_salary_name():
    X = DF['Salary']
    Y = DF['Name']
    ax = plt.subplots()
    ax.plot()
    DF.plot(kind='bar', x='Salary', y='Name')
    plt.show()

### Sort by Performance Score
def sort_performance():
    performance_order = DF.sort_values(by='Performance Score', ascending=False)
    print(performance_order[['Name', 'Performance Score']].reset_index(drop=True))



### Sort by Hire Date
def sort_hire_date():
    hire_date = DF.sort_values(by='Hire Date')
    print(hire_date[['Name', 'Hire Date']].reset_index(drop=True))



def data():
    print(DF)


over = True

while(over):
    query = str(input("Enter the query(only one function at a time): ")).lower()

    if "column" in query:
        column_names()

    elif "average" in query and "salary" in query:
        avg_salary()

    elif "average" in query and "age" in query:
        avg_age()

    elif "shape" in query:
        shape_of_data()

    elif "sort" in query and "salary" in query:
        sort_sal()

    elif "sort" in query and "performance" in query:
        sort_performance()

    elif "sort" in query and "hire" in query:
        sort_hire_date()
    
    elif "end" in query:
        over = False
    
    elif "data" in query:
        data()
    
    elif "salary" in query and "name" in query:
        graph_salary_name()
        