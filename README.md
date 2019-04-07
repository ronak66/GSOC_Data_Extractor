# GSOC_Data_Extractor

It is a simple tool created to make life easier for people applying for GSOC.

## Features

```
1. Compares and gives a list of gsoc organization that are common between different years
2. Provides a list of gsoc organization that uses the given technology
3. Provides list of oraganizations that uses the given technology and occur almost every year (first and second feature combined)  
```

## Installation

1. [FuzzyWuzzy Python library (Run)](https://pypi.org/project/fuzzywuzzy/):
    ```
    * $pip install fuzzywuzzy
    * $pip install python-Levenshtein
    ```
2. [BeautifulSoup library (Run)](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup):
    ```
    * $sudo apt-get install python3-bs4
    ```

## How to use
1. Run `$python gsoc_yearly_data_generator.py`
    * Input the gsoc year you want to search for
    * Wait till the count down drops to zero

2. Run `python query.py`
    * If you want to get list of organizations that uses a specific technology, your input should in the form:  
    `gt <gsoc year you want to search>`  
    Example: `gt 2016`

    * If you want all the organizations that are common between different years, your input should in the form:  
    `co <gsoc year1>,<gsoc year2>,...`  
    Example: `co 2016,2017,2018`

**Note : Don't manually delete any GSOC_<'year'>_Data.ods file, and even if you do, remove the line containing that year from ExtractedData.txt**
