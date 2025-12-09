OpenDataELTProject — iTunes API (John Lennon Data Pipeline)

This project demonstrates a simple ELT workflow using the public iTunes Search API.
It extracts Beatles-related track data, saves the raw dataset, applies several transformations, and exports a clean processed CSV for later analysis or dashboarding.

⸻

Data Source

Public API (no key required):

https://itunes.apple.com/search?term=beatles&limit=50


⸻

Project Structure

OpenDataELTProject/
├── data/
│   ├── raw/
│   │   └── raw.csv
│   └── processed/
│       └── output.csv
├── src/
│   └── main.py
├── requirements.txt
└── README.md


⸻

ELT Workflow

Extract
	•	Sends a request to the iTunes API
	•	Converts the JSON response into a pandas DataFrame
	•	Saves the unmodified data to data/raw/raw.csv

Load (Raw)
	•	The raw CSV is stored immediately after extraction
	•	No cleaning or filtering applied at this stage

Transform
	•	Converts releaseDate to datetime
	•	Filters rows where artistName contains John Lennon
	•	Sorts by release date
	•	Removes empty columns and cleans missing values

Load (Processed)
	•	Saves the cleaned dataset to:
data/processed/output.csv

⸻

How to Run
	1.	Install dependencies:

pip install -r requirements.txt


	2.	Run the ELT script:

python -m src.main


	3.	The processed file will appear at:

data/processed/output.csv



⸻

Output

The final CSV contains only John Lennon tracks retrieved from the broader Beatles search query, sorted by release date and cleaned of empty columns.
