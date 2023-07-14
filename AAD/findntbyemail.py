import pandas as pd

df1 = pd.read_csv ("ntaccounts.csv")

def findntbyemail():
    with open('emaillist.txt', 'r') as emails:
        while True:
            username = emails.readline()
            if not username:
                break
            username = username.strip('\n')
            ntname = df1.loc [df1['email'] == username, 'ntname'].item()
            print(ntname)

if __name__ == "__main__":
    findntbyemail()