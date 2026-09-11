import pandas as pd


def load_campaign_data(control_path, test_path):
    control = pd.read_csv(control_path, sep=";")
    test = pd.read_csv(test_path, sep=";")

    return control, test


def clean_campaign_data(control, test):
    # Remove incomplete rows from Control
    control_clean = control.dropna().copy()
    test_clean = test.copy()

    # Convert Date column
    control_clean["Date"] = pd.to_datetime(
        control_clean["Date"],
        format="%d.%m.%Y"
    )

    test_clean["Date"] = pd.to_datetime(
        test_clean["Date"],
        format="%d.%m.%Y"
    )

    # Add campaign labels
    control_clean["Campaign Type"] = "Control"
    test_clean["Campaign Type"] = "Test"

    # Combine datasets
    df = pd.concat(
        [control_clean, test_clean],
        ignore_index=True
    )

    return df