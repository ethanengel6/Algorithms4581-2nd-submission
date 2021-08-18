import pandas as pd

def loadInvestments(Filename,increment):
    realEstateDf = pd.read_csv(Filename, usecols=['RegionName','2019-01', '2020-01'])
    realEstateDf = realEstateDf.drop([realEstateDf.index[0]])
    realEstateDf['Return'] = realEstateDf['2020-01'] - realEstateDf['2019-01']
    realEstateDf=realEstateDf.drop(['2019-01'], axis=1)
    realEstateDf['2020-01']=round(realEstateDf['2020-01']/increment)
    investments = realEstateDf.values.tolist()
    return investments


def optimizeInvestments(investments,cash,increment):
    roundcash=int(cash/increment)
    weights=[]
    returns=[]
    for z in range(len(investments)):
        weights.append(int(investments[z][1]))
        returns.append(investments[z][2])
    n=len(weights)
    table = [[None for row in range(roundcash + 1)] for column in range(n+ 1)]
    for i in range(n + 1):
        for w in range(roundcash + 1):
            if i == 0 or w == 0:
                table[i][w] = 0
            elif weights[i-1] <= w:
                table[i][w] = max(returns[i-1]
                          + table[i-1][w-weights[i-1]],
                              table[i-1][w])
            else:
                table[i][w] = table[i-1][w]

    return table,(table[n][roundcash])

def cities(investments,matrix,cash,increment):
    roundcash2=int(cash/increment)
    cities2=[]
    weights2=[]
    for zz in range(len(investments)):
        cities2.append(investments[zz][0])
        weights2.append(int(investments[zz][1]))
        returns2.append(investments[zz][2])
    m=len(weights2)
    x = m
    y = roundcash2
    while (x > 0 and y > 0):
        if(matrix[x][y] != matrix[x-1][y]):
            print(cities2[x])
            y = y-weights2[x]
            x = x-1
        else:
            x = x-1


cash = 1000000
increment=1000
z=loadInvestments('metro.csv',increment)
q=optimizeInvestments(z,cash,increment)
print("Total returns = $",q[1])
cities(z,q[0],cash,increment)
