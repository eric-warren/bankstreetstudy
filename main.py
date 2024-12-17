import pandas as pd
from q2 import bar_sorted
from post import get_valid, get
# Load the survey data
df = pd.read_csv('survey_responses.csv')

v = get(get_valid(df), ['K1S'])

bar_sorted(v,'Ranking of Choices for Q2 (Only K1S)')
