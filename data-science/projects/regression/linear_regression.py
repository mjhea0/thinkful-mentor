import pandas as pd


loansData = pd.read_csv('loansData.csv')

# Print the first 5 rows of each of the column to see what needs to be cleaned
print loansData['Interest.Rate'][0:5]
print loansData['Loan.Length'][0:5]
print loansData['FICO.Range'][0:5]


# Clean up the columns
loansData['Interest.Rate'] = loansData['Interest.Rate'].map(
    lambda x: x.rstrip('%'))
loansData['Loan.Length'] = loansData['Loan.Length'].map(
    lambda x: x.rstrip('months'))

# Print again to see if cleaning took place or not
print loansData['Interest.Rate'][0:5]
print loansData['Loan.Length'][0:5]


'''
convert the data in FICO Range into string and
split the string and take the lowest value.
'''
loansData['FICO.Score'] = loansData['FICO.Range'].astype(str)
print loansData['FICO.Score'][0:5]
loansData['FICO.Score'] = loansData['FICO.Score'].split()
print loansData['FICO.Score'][0:5]
