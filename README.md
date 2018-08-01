Python script for automated access to world-bank website and retreiving datasets with datapackages.

## Data
World bank is a global partnership that provides loans to countries for capital projects. It tracks global development indicators and allows free and open access to its data. There are indicators from a variety of fields such as agriculture, economy, climate change etc.

## Usage

The scripts are python based and use python 3.5+. The script `get.py` has no dependencies outside of the standard library. It is used to download and extract a specific indicator. Credit goes to [rufuspolock](https://github.com/rufuspollock/world-bank-data). In order to obtain dataset with a specific indicator url run:
`python scripts/get.py indicator_url`

Example:
```
python scripts/get.py https://data.worldbank.org/indicator/GC.DOD.TOTL.GD.ZS
# This will download Central government total debt as percentage of GDP dataset
```

The script `extractFeaturedWorldBankDatasets.py` obtains datasets from the world-bank featured page https://data.worldbank.org/indicator?tab=featured. It uses library BeautifulSoup in order to scrape indicator urls. To install BeautifulSoup run:
`pip install bs4`

To obtain all featured indicators run:
`python scripts/extractFeaturedWorldBankDatasets.py`
