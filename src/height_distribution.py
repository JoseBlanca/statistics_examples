import pandas
import numpy
import seaborn
import matplotlib.pyplot as plt

from file_utils import BODY_MEASUREMENTS_CSV, CHARTS_DIR

seaborn.set_theme(style="white")


def gender_to_letter(gender):
    if numpy.isnan(gender):
        return "Other"
    gender = int(gender)
    if gender == 1:
        return "M"
    elif gender == 2:
        return "F"
    else:
        raise ValueError(f"Uknown gender : {gender}")


def get_body_measurements_data(min_age=None):
    measurements = pandas.read_csv(BODY_MEASUREMENTS_CSV)
    measurements["Gender"] = [
        gender_to_letter(gender) for gender in measurements["Gender"]
    ]
    measurements["Height (cm)"] = measurements["TotalHeight"] * 2.54
    measurements["Waist (cm)"] = measurements["Waist "] * 2.54
    if min_age:
        measurements = measurements.loc[measurements["Age"] >= min_age, :]
    return measurements


def plot_height_distribution(min_age=None):
    measurements = get_body_measurements_data(min_age=min_age)

    seaborn.displot(
        measurements,
        x="Height (cm)",
        hue="Gender",
        palette="pastel",
        stat="density",
        common_norm=False,
    )

    plot_path = CHARTS_DIR / "height_by_gender.svg"
    plt.savefig(plot_path, bbox_inches="tight")


def plot_height_waist_relation(min_age=None):
    measurements = get_body_measurements_data(min_age=min_age)

    seaborn.relplot(measurements, x="Height (cm)", y="Waist (cm)", hue="Gender")

    plot_path = CHARTS_DIR / "height_vs_waist.svg"
    plt.savefig(plot_path, bbox_inches="tight")


if __name__ == "__main__":
    plot_height_distribution(min_age=20)
    plot_height_waist_relation(min_age=20)
