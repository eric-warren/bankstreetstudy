import matplotlib.pyplot as plt


def bar(df):

    # Column related to Q3
    q3_column = 'Q3'

    # Extract the responses from Q3 column
    q3_values = df[q3_column].dropna()  # Remove any NaN values

    # Count the frequency of each unique value
    q3_total_counts = q3_values.value_counts()

    # Plotting the results
    plt.figure(figsize=(12, 8))  # Increase figure size for more space
    ax = q3_total_counts.plot(kind='bar', color='blue')

    # Customizing the plot
    plt.title('Total Counts of Each Response in Q3')
    plt.xlabel('Response Options')
    plt.ylabel('Frequency')
    plt.xticks(rotation=20, ha='right')  # Rotate the x-axis labels for better readability

    # Increase bottom margin to give more space to the labels
    plt.subplots_adjust(bottom=0.2)

    # Adding numbers on top of the bars
    for idx, value in enumerate(q3_total_counts):
        ax.text(idx, value + 0.1, str(value), ha='center', va='bottom', fontsize=10, color='black')

    # Show the plot
    plt.show()

def pie(df):
    # Column related to Q3
    q3_column = 'Q3'

    # Extract the responses from Q3 column
    q3_values = df[q3_column].dropna()  # Remove any NaN values

    # Count the frequency of each unique value
    q3_total_counts = q3_values.value_counts()

    # Plotting the results as a pie chart
    plt.figure(figsize=(8, 8))  # Set the figure size for better visibility
    colors = ['#66b3ff', '#99ff99', '#ffcc99', '#ffb3e6', '#ff6666']  # Custom colors for the pie chart
    ax = q3_total_counts.plot(kind='pie', autopct='%1.1f%%', colors=colors, legend=False)

    # Customizing the plot
    plt.title('Distribution of Responses for Q3')
    plt.ylabel('')  # Remove the y-label for a cleaner look

    # Show the plot
    plt.show()