import seaborn as sns

df = sns.load_dataset('tips')
print(df.head())

print(sns.displot(df['tip']))
