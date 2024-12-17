import matplotlib.pyplot as plt

def bar(df):
    # Columns related to Q1 (e.g., Q1_Answer_1, Q1_Answer_2, etc.)
    q1_columns = ['Q1_Answer_1', 'Q1_Answer_2', 'Q1_Answer_3', 'Q1_Answer_4', 'Q1_Answer_5']

    # Combine all Q1 columns into a single series
    all_q1_values = df[q1_columns].stack()

    # Drop any NaN values (only count actual responses)
    all_q1_values = all_q1_values.dropna()

    # Clean by removing periods at the end of responses
    all_q1_values = all_q1_values.str.rstrip('.')  # Removes trailing periods

    # Count the frequency of each unique value
    q1_total_counts = all_q1_values.value_counts()

    # Plotting the results
    plt.figure(figsize=(12, 8))  # Increase figure size for more space
    ax = q1_total_counts.plot(kind='bar', color='blue')

    # Customizing the plot
    plt.title('Total Counts of Each Response in Q1')
    plt.xlabel('Response Options')
    plt.ylabel('Frequency')
    plt.xticks(rotation=10, ha='right')  # Rotate the x-axis labels for better readability

    # Increase bottom margin to give more space to the labels
    plt.subplots_adjust(bottom=0.2)

    # Adding numbers on top of the bars with a different color (e.g., red)
    for idx, value in enumerate(q1_total_counts):
        ax.text(idx, value + 0.1, str(value), ha='center', va='bottom', fontsize=10, color='black')

    # Show the plot
    plt.show()
