import pandas as pd
import matplotlib.pyplot as plt

def line_graph_prs_per_day(csv_file):
    df = pd.read_csv(csv_file)
    df['Created_At'] = pd.to_datetime(df['Created_At'])
    df.groupby(df['Created_At'].dt.date).size().plot(kind='line')
    plt.title('Total Number of Pull Requests Per Day')
    plt.xlabel('Day')
    plt.ylabel('Number of Pull Requests')
    plt.savefig('line_graph_prs_per_day.png')
    plt.show()

def line_graph_open_closed_prs_per_day(csv_file):
    df = pd.read_csv(csv_file)
    df['Created_At'] = pd.to_datetime(df['Created_At'])
    pivot = df.pivot_table(index=df['Created_At'].dt.date, columns='State', aggfunc='size')
    pivot.plot(kind='line')
    plt.title('Open vs Closed Pull Requests Per Day')
    plt.xlabel('Day')
    plt.ylabel('Number of Pull Requests')
    plt.savefig('line_graph_open_closed_prs_per_day.png')
    plt.show()

def bar_plot_users_per_repository(csv_file):
    df = pd.read_csv(csv_file)
    if 'Repositories' not in df.columns:
        print("Column 'Repositories' not found in the data.")
        return
    
    # Assuming 'Username' is a column in your CSV
    user_counts = df['Username'].value_counts()
    user_counts.plot(kind='bar')
    plt.title('Number of Repositories per User')
    plt.xlabel('User')
    plt.ylabel('Number of Repositories')
    plt.show()

