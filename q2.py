import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.colors as mcolors
def scoring(data):
    out = {}

    for i, x in data.iterrows():
        for rank, score in zip(['Q2_Rank1', 'Q2_Rank2', 'Q2_Rank3', 'Q2_Rank4', 'Q2_Rank5', 'Q2_Rank6'], [6, 5, 4, 3, 2, 1]):
            rank_value = x.get(rank)
            if pd.notna(rank_value):  # Check if the rank value is not NaN
                if rank_value in out:
                    out[rank_value] += score
                else:
                    out[rank_value] = score

    # Sort in descending order
    sorted_dict_desc = dict(sorted(out.items(), key=lambda item: item[1], reverse=True))

    labels = list(sorted_dict_desc.keys())
    values = list(sorted_dict_desc.values())

    plt.figure(figsize=(12, 8))  # Set the figure size to allow more space for labels
    bars = plt.bar(labels, values, color='skyblue')  # Create a vertical bar chart
    plt.ylabel('Scores')  # Label for the y-axis
    plt.title('Scoring for Various Urban Infrastructure Options')  # Chart title
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    plt.tight_layout()  # Adjust layout to make room for the rotated labels

    # Add numerical values on top of each bar
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval, int(yval), ha='center', va='bottom')
    plt.show()  # Display the plot

def bar(df, title='Ranking of Choices for Q2'):
    # Strip any extra whitespace from the column names
    df.columns = df.columns.str.strip()

    # Prepare the ranking columns for Q2
    ranking_columns = ['Q2_Rank1', 'Q2_Rank2', 'Q2_Rank3', 'Q2_Rank4', 'Q2_Rank5', 'Q2_Rank6']

    # Define the choices with the exact string matching the survey data
    choices = ['Bus-only lanes so buses do not get delayed in traﬃc',
               'Wider sidewalk (where possible)',
               'Cycle lanes', 
               'Space for benches and trees', 
               'Car lanes', 
               'On-street parking and loading zones']

    # Normalize the choices to strip any unwanted spaces (if needed)
    choices = [choice.strip() for choice in choices]

    # Prepare an empty list to collect the data
    ranking_counts_list = []

    # For each ranking column, count occurrences
    for rank_column in ranking_columns:
        for choice in choices:
            rank_count = (df[rank_column] == choice).sum()  # Count how many times the choice is in that rank
            ranking_counts_list.append({'Choice': choice, 'Rank': rank_column, 'Count': rank_count})

    # Convert the list of dictionaries into a DataFrame
    ranking_counts = pd.DataFrame(ranking_counts_list)

    # Pivot the data for easier visualization
    pivot_data = ranking_counts.pivot_table(index='Choice', columns='Rank', values='Count', aggfunc='sum')

    # Ensure the order of the rows (choices) is fixed
    pivot_data = pivot_data.loc[choices]

    # Create a colormap for the gradient (using 'coolwarm' as an example)
    cmap = plt.get_cmap("coolwarm")

    # Normalize the ranks so that the lowest rank (Q2_Rank1) gets the lightest color
    norm = mcolors.Normalize(vmin=1, vmax=6)  # Since we have 6 ranks (Q2_Rank1 to Q2_Rank6)

    # Generate the colors for each rank based on the colormap
    rank_colors = [cmap(norm(i)) for i in range(1, 7)]

    # Plot the data as a bar chart with gradient colors
    ax = pivot_data.plot(kind='bar', stacked=True, figsize=(10, 6), color=rank_colors)

    # Add numerical values on top of each segment
    for i, choice in enumerate(pivot_data.index):
        cumulative_count = 0
        for j, rank in enumerate(ranking_columns):
            count = pivot_data.loc[choice, rank]
            if count > 0:
                ax.text(i, cumulative_count + count / 2, int(count), ha='center', va='center')
            cumulative_count += count
    # Customize the plot
    plt.title(title)
    plt.xlabel('Choices')
    plt.ylabel('Count')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Rank', labels=['Rank 1', 'Rank 2', 'Rank 3', 'Rank 4', 'Rank 5', 'Rank 6'], bbox_to_anchor=(1.05, 1), loc='upper left')

    # Show the plot
    plt.tight_layout()
    plt.show()


def bar_sorted(df, title='Ranking of Choices for Q2 (Sorted by Most First Responses)'):
    # Strip any extra whitespace from the column names
    df.columns = df.columns.str.strip()

    # Prepare the ranking columns for Q2
    ranking_columns = ['Q2_Rank1', 'Q2_Rank2', 'Q2_Rank3', 'Q2_Rank4', 'Q2_Rank5', 'Q2_Rank6']

    # Define the choices with the exact string matching the survey data
    choices = ['Bus-only lanes so buses do not get delayed in traﬃc',
               'Wider sidewalk (where possible)',
               'Cycle lanes', 
               'Space for benches and trees', 
               'Car lanes', 
               'On-street parking and loading zones']

    # Normalize the choices to strip any unwanted spaces (if needed)
    choices = [choice.strip() for choice in choices]

    # Prepare an empty list to collect the data
    ranking_counts_list = []

    # For each ranking column, count occurrences
    for rank_column in ranking_columns:
        for choice in choices:
            rank_count = (df[rank_column] == choice).sum()  # Count how many times the choice is in that rank
            ranking_counts_list.append({'Choice': choice, 'Rank': rank_column, 'Count': rank_count})

    # Convert the list of dictionaries into a DataFrame
    ranking_counts = pd.DataFrame(ranking_counts_list)

    # Pivot the data for easier visualization
    pivot_data = ranking_counts.pivot_table(index='Choice', columns='Rank', values='Count', aggfunc='sum')

    # Sort the choices based on the total count for Rank 1 (most first responses)
    pivot_data['Total'] = pivot_data['Q2_Rank1']  # We assume we're sorting by Rank 1 (first responses)
    pivot_data_sorted = pivot_data.sort_values(by='Total', ascending=False).drop(columns='Total')  # Drop the 'Total' column after sorting

    # Create a colormap for the gradient (using 'coolwarm' as an example)
    cmap = plt.get_cmap("coolwarm")

    # Normalize the ranks so that the lowest rank (Q2_Rank1) gets the lightest color
    norm = mcolors.Normalize(vmin=1, vmax=6)  # Since we have 6 ranks (Q2_Rank1 to Q2_Rank6)

    # Generate the colors for each rank based on the colormap
    rank_colors = [cmap(norm(i)) for i in range(1, 7)]

    # Plot the data as a bar chart with gradient colors
    ax = pivot_data_sorted.plot(kind='bar', stacked=True, figsize=(10, 6), color=rank_colors)

    # Add numerical values on top of each segment
    for i, choice in enumerate(pivot_data_sorted.index):
        cumulative_count = 0
        for j, rank in enumerate(ranking_columns):
            count = pivot_data_sorted.loc[choice, rank]
            if count > 0:
                ax.text(i, cumulative_count + count / 2, int(count), ha='center', va='center')
            cumulative_count += count
    # Customize the plot
    plt.title(title)
    plt.xlabel('Choices')
    plt.ylabel('Count')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Rank', labels=['Rank 1', 'Rank 2', 'Rank 3', 'Rank 4', 'Rank 5', 'Rank 6'], bbox_to_anchor=(1.05, 1), loc='upper left')

    # Show the plot
    plt.tight_layout()
    plt.show()

def per_q1(df):
    # Columns related to Q1
    q1_columns = ['Q1_Answer_1', 'Q1_Answer_2', 'Q1_Answer_3', 'Q1_Answer_4', 'Q1_Answer_5']

    # Create a new column that combines all the Q1 answers into a list
    df['Q1_Combined'] = df[q1_columns].apply(lambda row: [answer for answer in row if pd.notna(answer)], axis=1)

    # Function to normalize answers by stripping trailing periods
    def normalize_answer(answer):
        return answer.rstrip('.')  # Remove trailing periods

    # Get unique values from the combined Q1 answers, normalize them
    unique_values = set(
        normalize_answer(val) for sublist in df['Q1_Combined'] for val in sublist
    )

    # Create a dictionary to store the rows for each unique value
    entries_by_value = {}

    # Loop through each unique value and find the rows that contain it
    for value in unique_values:
        # Normalize the value and get the rows where the normalized value is in the Q1_Combined list
        matching_rows = df[df['Q1_Combined'].apply(
            lambda x: any(normalize_answer(answer) == value for answer in x)
        )]
        # Store the matching rows in the dictionary
        entries_by_value[value] = matching_rows

    for x in entries_by_value:

        bar(entries_by_value[x],f'Ranking of Choices for Q2 (People who chose {x})')

def per_q3(df):
    # Strip any extra whitespace from the column names
    df.columns = df.columns.str.strip()

    # Define unique answers for Q3
    q3_answers = df['Q3'].unique()

    # For each Q3 answer, filter the DataFrame and call the bar function
    for q3_answer in q3_answers:
        filtered_df = df[df['Q3'] == q3_answer]
        
        # Call the bar function with the filtered DataFrame for each Q3 answer
        bar(filtered_df, title=f'Ranking of Choices for Q2 - Answer to Q3: {q3_answer}')
