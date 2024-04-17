import pandas as pd
from tabulate import tabulate

bills = pd.read_csv("src/repositories/data/bills.csv")
bills = pd.DataFrame(bills)
legislator = pd.read_csv("src/repositories/data/legislators.csv")
legislator = pd.DataFrame(legislator)
votes = pd.read_csv("src/repositories/data/votes.csv")
votes = pd.DataFrame(votes)
vote_results = pd.read_csv("src/repositories/data/vote_results.csv")
vote_results = pd.DataFrame(vote_results)

# Votes per legislator
votes_per_legislator = pd.merge(
    vote_results,
    legislator,
    how="left",
    left_on="legislator_id",
    right_on="id",
    suffixes=('', "_y")
)
del votes_per_legislator['id_y']
# Adding bill information
votes_per_legislator_per_bill = pd.merge(
    votes_per_legislator,
    votes,
    how="left",
    left_on="vote_id",
    right_on="id",
    suffixes=('', '_y')
)
del votes_per_legislator_per_bill['id_y']
votes_per_legislator_per_bill = pd.merge(
    votes_per_legislator_per_bill,
    bills,
    how="left",
    left_on="bill_id",
    right_on="id",
    suffixes=('', '_y')
)
del votes_per_legislator_per_bill['id_y']
# Adicionando o primary sponsor
votes_per_legislator_per_bill = pd.merge(
    votes_per_legislator_per_bill,
    legislator,
    how="left",
    left_on="sponsor_id",
    right_on="id",
    suffixes=('', '_y')
)
del votes_per_legislator_per_bill['id_y']
votes_per_legislator_per_bill.rename(columns={"name_y": "Primary sponsor"}, inplace=True)

votes_per_legislator_per_bill = pd.DataFrame(votes_per_legislator_per_bill)

print(tabulate(votes_per_legislator_per_bill))

print(tabulate(votes_per_legislator))
