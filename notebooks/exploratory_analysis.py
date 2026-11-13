"""Exploratory analysis for the 2025 Chicago crime and weather dataset.

Run this script from any directory. It reads the processed daily dataset and
writes summary tables and figures to the project's results/ and figures/
directories.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = PROJECT_ROOT / "data" / "processed" / "daily_crimes_weather.csv"
RESULTS_DIR = PROJECT_ROOT / "results"
FIGURES_DIR = PROJECT_ROOT / "figures"


def main() -> None:
    RESULTS_DIR.mkdir(exist_ok=True)
    FIGURES_DIR.mkdir(exist_ok=True)

    data = pd.read_csv(INPUT_FILE, parse_dates=["Date"])
    data["Total Incidents"] = data["Assault Count"] + data["Battery Count"]
    data["Month"] = data["Date"].dt.month
    data["Month Name"] = data["Date"].dt.month_name()
    data["Day of Week"] = data["Date"].dt.day_name()
    data["Rainy"] = data["Precipitation"] > 0

    # Basic data-quality checks.
    quality = pd.DataFrame(
        {
            "check": [
                "row_count",
                "duplicate_dates",
                "missing_values",
                "start_date",
                "end_date",
            ],
            "value": [
                len(data),
                int(data["Date"].duplicated().sum()),
                int(data.isna().sum().sum()),
                data["Date"].min().date(),
                data["Date"].max().date(),
            ],
        }
    )
    quality.to_csv(RESULTS_DIR / "data_quality_checks.csv", index=False)
    print("Data-quality checks")
    print(quality.to_string(index=False))

    # Descriptive statistics for the daily incident counts.
    descriptive = data[
        ["Assault Count", "Battery Count", "Total Incidents", "Temperature", "Precipitation"]
    ].describe().round(2)
    descriptive.to_csv(RESULTS_DIR / "descriptive_statistics.csv")
    print("\nDescriptive statistics")
    print(descriptive)

    # Pearson correlations between weather variables and incident counts.
    correlations = data[
        ["Assault Count", "Battery Count", "Total Incidents", "Temperature", "Precipitation"]
    ].corr()[["Temperature", "Precipitation"]].loc[
        ["Assault Count", "Battery Count", "Total Incidents"]
    ].round(3)
    correlations.to_csv(RESULTS_DIR / "weather_crime_correlations.csv")
    print("\nWeather/crime correlations")
    print(correlations)

    # Compare average counts on rainy and dry days.
    rainy_dry = (
        data.groupby("Rainy")[["Assault Count", "Battery Count", "Total Incidents"]]
        .agg(["count", "mean"])
        .round(2)
    )
    rainy_dry.to_csv(RESULTS_DIR / "rainy_dry_comparison.csv")
    print("\nRainy/dry comparison")
    print(rainy_dry)

    # Grouped comparisons for seasonality and day-of-week patterns.
    monthly = (
        data.groupby(["Month", "Month Name"])[
            ["Assault Count", "Battery Count", "Total Incidents", "Temperature"]
        ]
        .mean()
        .round(2)
        .reset_index()
    )
    monthly.to_csv(RESULTS_DIR / "monthly_averages.csv", index=False)

    weekday_order = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    weekday = (
        data.groupby("Day of Week")[["Assault Count", "Battery Count", "Total Incidents"]]
        .mean()
        .reindex(weekday_order)
        .round(2)
        .reset_index()
    )
    weekday.to_csv(RESULTS_DIR / "weekday_averages.csv", index=False)
    print("\nMonthly averages")
    print(monthly.to_string(index=False))
    print("\nWeekday averages")
    print(weekday.to_string(index=False))

    # Figure 1: temperature and total daily incidents.
    plt.figure(figsize=(8, 5))
    plt.scatter(data["Temperature"], data["Total Incidents"], alpha=0.65)
    plt.xlabel("Average daily temperature")
    plt.ylabel("Assault + battery incidents")
    plt.title("Daily temperature and reported incidents in Chicago, 2025")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "temperature_vs_incidents.png", dpi=200)
    plt.close()

    # Figure 2: monthly average total incidents.
    plt.figure(figsize=(8, 5))
    plt.plot(monthly["Month Name"], monthly["Total Incidents"], marker="o")
    plt.xlabel("Month")
    plt.ylabel("Average daily incidents")
    plt.title("Average daily incidents by month")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "monthly_incident_averages.png", dpi=200)
    plt.close()

    # Figure 3: weekday average total incidents.
    plt.figure(figsize=(8, 5))
    plt.bar(weekday["Day of Week"], weekday["Total Incidents"])
    plt.xlabel("Day of week")
    plt.ylabel("Average daily incidents")
    plt.title("Average daily incidents by day of week")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "weekday_incident_averages.png", dpi=200)
    plt.close()

    print(f"\nSaved summary tables to {RESULTS_DIR}")
    print(f"Saved figures to {FIGURES_DIR}")


if __name__ == "__main__":
    main()
