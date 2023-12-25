import pandas as pd
import matplotlib.pyplot as plt

def boxplot_commits(csv_file):
    df = pd.read_csv(csv_file)
    df.boxplot(column='Commits', by='State')
    plt.title('Commits in Open vs Closed Pull Requests')
    plt.suptitle('')  # Removes the default title
    plt.xlabel('PR State')
    plt.ylabel('Number of Commits')
    plt.savefig('boxplot_commits.png')
    plt.show()
    
def boxplot_additions_deletions(csv_file):
    df = pd.read_csv(csv_file)
    df[['Additions', 'Deletions']].plot(kind='box')
    plt.title('Additions and Deletions in Pull Requests')
    plt.ylabel('Count')
    plt.savefig('boxplot_additions_deletions.png')
    plt.show()

def boxplot_changed_files_author(csv_file):
    df = pd.read_csv(csv_file)
    if 'Author_Association' not in df.columns:
        print("Column 'Author_Association' not found in the data.")
        return
    df.boxplot(column='Changed_Files', by='Author_Association')
    plt.title('Changed Files by Author Association')
    plt.suptitle('')
    plt.xlabel('Author Association')
    plt.ylabel('Number of Changed Files')
    plt.savefig('boxplot_changed_files_author.png')
    plt.show()


def scatterplot_additions_deletions(csv_file):
    df = pd.read_csv(csv_file)
    df.plot(kind='scatter', x='Additions', y='Deletions')
    plt.title('Relationship Between Additions and Deletions')
    plt.xlabel('Additions')
    plt.ylabel('Deletions')
    plt.savefig('scatterplot_additions_deletions.png')
    plt.show()

def calculate_correlations():
    try:
        # Load data
        df = pd.read_csv('repositories.csv')

        # Select only the numerical columns
        numerical_data = df.select_dtypes(include=['int64', 'float64'])

        # Calculate correlation matrix
        correlation_matrix = numerical_data.corr()

        # Display the correlation matrix
        print("Correlation matrix:")
        print(correlation_matrix)

    except FileNotFoundError:
        print("The repositories.csv file does not exist. Please collect data first.")
    except Exception as e:
        print(f"An error occurred: {e}")

