This is a proof of concept for generating authentication tokens for Neobands.

The repository takes a csv as input. The structur of the csv should look like this:

| Sector  | Faction | Key A  | Key B |
| ------------- | ------------- | ------------- | ------------- |
| 1  | Alleycat Asset Acquisitions  |    |    |
| 2  | Exus  |    |    |
| 3  | Pilot's Perch  |    |    |
| 4  | Maintenance Bay 54  |    |    |
| 5  | ATFL  |    |    |
| 6  | Extremely Temp Agency  |    |    |

Key A is the faction read/write key. The script will generate a unique key and place it in the Key A column for every row that has a Faction name present.
Key B is the universal read key. The script generates a single key and then fills the Key B column for every row that has a Faction name present.

`credentials_updated.csv` shows an example of a csv after the script has executed, based off of `credentials.csv`
