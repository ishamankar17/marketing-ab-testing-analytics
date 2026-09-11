from scipy.stats import ttest_ind


def welch_ttest(control, test):

    statistic, p_value = ttest_ind(
        control,
        test,
        equal_var=False
    )

    return statistic, p_value


def compare_campaigns(df):

    control = df[df["Campaign Type"] == "Control"]
    test = df[df["Campaign Type"] == "Test"]

    results = {}

    metrics = [
        "CTR (%)",
        "CPA (USD)",
        "Purchase Conversion (%)"
    ]

    for metric in metrics:

        statistic, p_value = welch_ttest(
            control[metric],
            test[metric]
        )

        results[metric] = {
            "Control Mean": control[metric].mean(),
            "Test Mean": test[metric].mean(),
            "p-value": p_value
        }

    return results