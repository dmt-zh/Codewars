# A man has a rather old car being worth $2000. He saw a secondhand car being worth $8000.
# He wants to keep his old car until he can buy the secondhand one.
# He thinks he can save $1000 each month but the prices of his old car and of the new one decrease 
# of 1.5 percent per month. Furthermore this percent of loss increases of 0.5 percent at the end of every two months.
# Our man finds it difficult to make all these calculations.

def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    import numpy as np
    import itertools
    a = np.arange(percentLossByMonth, 100.5, 0.5)
    b = np.arange(percentLossByMonth + 0.5, 100.5, 0.5)
    c = list(itertools.chain(*zip(a, b)))
    savings = [i * savingperMonth for i in range(1, len(a))]
    loss_old = []
    loss_new = []
    if startPriceOld - startPriceNew >= 0:
        return ([0, startPriceOld - startPriceNew])
    else:
        for i in c:
            startPriceOld = startPriceOld - ((i * startPriceOld)/100)
            loss_old.append(startPriceOld)
            startPriceNew = startPriceNew - ((i * startPriceNew)/100)
            loss_new.append(startPriceNew)
        res = list(map(lambda x, y, z: (x + y) - z, loss_old, savings, loss_new))

    return [res.index([x for x in res if x > 0][0]) + 1, round([x for x in res if x > 0][0])]


print(nbMonths(2000, 8000, 1000, 1.5))






