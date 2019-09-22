import multiprocessing as mp
import pandas as pd
from datetime import timedelta
from IPython.display import clear_output
import time
import numpy as np
import progressbar

##
## Function definitions
##
def extractMostRecentRowForKey(key):
    # start = time.time()                     ## For keeping track of iteration duration

    mostRecentRow = empty_row                 ## Default return value
    a = price_trdmnt[key]
    b = price_stkcd[key]
    
    rows_stdck = BS.loc[BS_stkcd == b]                                                                ## Extract BS rows where 'stkcd' == b
    rows_annodt = rows_stdck.loc[rows_stdck['annodt'] < a].sort_values(by='annodt', ascending=True )  ## Extract subrows where annodt < a. Ascending sorting

    # print(rows_annodt)                      ## To verify the sorting, change ascending to False...

    if rows_annodt.size > 0:
        row_to_add = rows_annodt.tail(1)      ## Keep most recent entry, located at the end of the sorted list rows_annodt
        mostRecentRow = row_to_add.values[0]  ## Memorize this entry
        
    # duration = time.time() - start
    # print(key, ':', duration)
    return(mostRecentRow)


##
## Main program
##
# Lecture des donnees
print("Reading data.")
IS = pd.read_pickle('IS.pkl')
BS = pd.read_pickle('BS.pkl')
CF = pd.read_pickle('CF.pkl')
price=pd.read_pickle('PRICE.pkl')

## DataFrame converted from result list
main=pd.DataFrame()

## Extract the columns we need. Much quicker for search/iterating
price_trdmnt = price['trdmnt']
price_stkcd  = price['stkcd']
BS_stkcd     = BS['stkcd']

## Create empty row of the proper size. Will generate a row of NaNs
number_columns = BS.shape[1]
empty_row = [None] * number_columns

# print('# columns: ', number_columns)
# print('empty_row: ', empty_row)

## Creating of pool of workers. Use all available cores/threads
nbrAvailCores = mp.cpu_count()
pool = mp.Pool(processes=nbrAvailCores)

# Get all the job handles, one per price entry. This is very quick
print("Sending %d jobs to %d workers" % (len(price), nbrAvailCores))
resultsHandle = [pool.apply_async(extractMostRecentRowForKey, args=(z,)) for z in range(0, len(price))]

# Just a simple test. This whole job last for about 90 sec. The workers will do their jobs while we sleep for 60s.
# When the sleep is done, we will move to the scrollbar part, the scrollbar will quickly rise to the 2/3 of
# the bar because the results for the first 60 sec are already computed/available.
# Then for the last 30 sec, the results will come in as they became available. The scrollbar will slow down
# to track the progress of the last 1/3 of results. 
print("Main program sleeping for 60s. Workers keep on working. (Just a proof of concept test...)")
time.sleep(60)

# Accumulate and track results as they come in. Results already sorted. Use progressbar
print("Tracking workers progress.")
results = [r.get() for r in progressbar.progressbar(resultsHandle)]
#print(results)

## Convert list into dataFrame
print("Converting results to DataFrame.")
main = pd.DataFrame(results, columns=BS.columns)
print(main)
