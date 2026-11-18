# Chicago Assault/Battery and Weather Analysis

This project studies whether daily weather conditions are associated with reported assault and battery incidents in Chicago.

## Current project status

Completed:

- Cleaned the Chicago crime records and retained 2025 assault and battery incidents.
- Cleaned daily weather observations from NOAA's Chicago Midway Airport station.
- Calculated daily average temperature from the maximum and minimum temperatures.
- Joined daily crime counts with temperature and precipitation by date.
- Completed introductory exploratory analysis, including descriptive statistics, Pearson correlations, rainy/dry comparisons, monthly averages, weekday averages, and data-quality checks.
- Created three exploratory figures.

The current analysis is limited to 2025. The crime data currently include all selected assault and battery records; the code does **not** apply an `ARREST = True` filter. The project should not claim that an arrest filter was used unless that filter is added and the processed results are regenerated.

## Main data files

The final analysis dataset is `data/processed/daily_crimes_weather.csv`. It contains one row per day in 2025 with:

- `Date`
- `Assault Count`
- `Battery Count`
- `Temperature`
- `Precipitation`

Source data are in `data/original/`. Processed data are in `data/processed/`:

- `crimes_cleaned.csv` — 2025 crime records with date and primary type.
- `Chicago_midway_weather_cleaned.csv` — cleaned daily Midway weather observations.
- `daily_crimes_weather.csv` — joined daily crime and weather data.

## Reproduce the cleaned datasets

Run these from the project root:

1. Run `notebooks/weather_cleaning.ipynb` to create the cleaned weather file.
2. Run `group-project.ipynb` to create the cleaned crime file and joined daily dataset.

## Run the exploratory analysis

After creating the processed datasets, run:

```bash
python notebooks/exploratory_analysis.py
```

The script creates summary tables in `results/` and four charts in `figures/` covering data quality, descriptive statistics, correlations, rainy/dry comparisons, monthly averages, and weekday averages.

## Preliminary findings

The current exploratory results show:

- 365 daily observations in 2025.
- 10,925 cleaned assault and battery records.
- A temperature correlation of approximately `0.354` with combined daily incidents.
- A precipitation correlation of approximately `-0.013` with combined daily incidents.
- Average combined incidents of approximately `30.12` on rainy days and `29.86` on dry days.

These are preliminary associations, not evidence that temperature causes crime. The single weather station may not represent conditions across all Chicago neighborhoods, and reported incidents may not represent all actual crime. Further work may include adding calendar controls, evaluating a regression model, and comparing the results with related studies.
