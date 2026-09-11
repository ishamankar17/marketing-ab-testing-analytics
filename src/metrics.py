def calculate_kpis(df):

    df["CTR (%)"] = (
        df["# of Website Clicks"]
        / df["# of Impressions"]
    ) * 100

    df["CPC (USD)"] = (
        df["Spend [USD]"]
        / df["# of Website Clicks"]
    )

    df["CPA (USD)"] = (
        df["Spend [USD]"]
        / df["# of Purchase"]
    )

    df["Purchase Conversion (%)"] = (
        df["# of Purchase"]
        / df["# of Website Clicks"]
    ) * 100

    df["View to Cart (%)"] = (
        df["# of Add to Cart"]
        / df["# of View Content"]
    ) * 100

    df["Cart to Purchase (%)"] = (
        df["# of Purchase"]
        / df["# of Add to Cart"]
    ) * 100

    return df


def campaign_summary(df):

    metrics = [
        "Spend [USD]",
        "# of Impressions",
        "Reach",
        "# of Website Clicks",
        "# of Searches",
        "# of View Content",
        "# of Add to Cart",
        "# of Purchase"
    ]

    summary = df.groupby("Campaign Type")[metrics].sum()

    summary["CTR (%)"] = (
        summary["# of Website Clicks"]
        / summary["# of Impressions"]
    ) * 100

    summary["CPC (USD)"] = (
        summary["Spend [USD]"]
        / summary["# of Website Clicks"]
    )

    summary["CPA (USD)"] = (
        summary["Spend [USD]"]
        / summary["# of Purchase"]
    )

    summary["Click to Purchase (%)"] = (
        summary["# of Purchase"]
        / summary["# of Website Clicks"]
    ) * 100

    return summary