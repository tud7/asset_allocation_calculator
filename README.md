## asset_allocation_calculator
I have multiple investment accounts (within the same broker) and from the dashboard, I can see the list of my stocks across my accounts group by stock symbol, but missing the allocation percentage  
For example: I invested in company XZY in 3 different accounts, and I want to see the (total) percentage of XYZ in all of my accounts  
I contacted the customer service, and they said that feature is not avaiable (sadly).  So I decide to write this simple utility to calculate the allocation percentage and simply print the output to the terminal screen.  

To call:  
```
python allocation_report.py <csv_file>
```
<csv_file>: full path to the csv file with these required columns: (other columns will not be used and will be ignored)
* Symbol
* Current Value
*Check the portfolio_example.csv file for more details*

#### Example output
Symbol | Quantity | Current Value | Percentage
------------ | ------------ | ------------- | ------------- 
DIS | 180 | $ 30,655.83 | 24.70%
BA | 105 | $ 22,669.50 | 18.26%
BAC | 480 | $ 22,137.60 | 17.83%
AAPL | 150 | $ 21,871.51 | 17.62%
SBUX | 120 | $ 13,586.40 | 10.95%
MSFT | 43 | $ 13,207.05 | 10.64%

<br/>

#### Dependencies
* Python 3.8
* pandas 1.3.4


