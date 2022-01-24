# Colorado Congressional Election Audit
Audit to determine integrity of congressional election. Audit tabulated vote totals for all candidates receiving votes in three Colorado counties.

## Audit Results
In this congressional election, **369,711** votes were cast across three Colorado counties centered around the Denver metropolitan region.

The vast majority of votes, over 82%, came from Denver County, followed by Jefferson and Arapahoe Counties respectively.

|County|Votes|Percentage|
|---|---|---|
|**Denver**|306,055|82.8%|
|**Jefferson**|38,855|10.5%|
|**Arapahoe**|24,801|6.7%|

---
Three candidates received votes in this Congressional election
* **Charles Casper Stockham**
* **Diane DeGette**
* **Raymon Anthony Doane**

|Candidate|Votes|Percentage|
|---|---|---|
|**DeGette**|272,892|73.8%|
|**Stockham**|85,213|23.0%|
|**Doane**|11,606|3.1%|

Based on this election audit, the declared winner **Diane DeGette** is correct and well outside the range for a general recount.

## Post Audit Sumamry
With very little modification, this audit code could be used for any elections in the state.

While this election only featured votes from three counties, the number of counties is determined internally so there's no updates needed to expand the reach.

A few minor changes to the file location could be added to negate the need for a local file - instead pulling the data directly from a server or internet.

An additional loop through the candidate vote totals could also be added to provide additional sorting for the runner up candidates.

Futher breakdown of individual candidate results to the county level is also possible.
