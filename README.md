# Chicago Assault/Battery and Weather (2025)

The final analysis dataset is `data/processed/daily_crimes_weather.csv`. It has one row per day in 2025, with separate assault and battery counts, daily average temperature, and precipitation.

## Data folders

- `data/original/` contains source files. The crime records, `weather_Chicago.csv`, and `new_precipitation.csv` are inputs to the current cleaning workflow. `weather.csv` is an earlier weather dataset and is not used by the current notebooks.
- `data/processed/` contains derived datasets:
  - `crimes_cleaned.csv` — 2025 crime records with date and primary type.
  - `Chicago_midway_weather_cleaned.csv` — daily Midway weather.
  - `daily_crimes_weather.csv` — final daily analysis dataset.

## Recreate the datasets

1. Run `notebooks/weather_cleaning.ipynb` with the working directory set to `notebooks/`. It reads source files from `data/original/` and writes cleaned weather to `data/processed/`.
2. Run `group-project.ipynb` with the working directory set to the project root. It regenerates the cleaned 2025 crime data and the final joined dataset.

The notebooks and source data are included so the processed output can be reproduced. The older `data/original/weather.csv` can be omitted from a GitHub push if you do not need to retain that unused source.
