import matplotlib.pyplot as plt


def plot_campaign_comparison(summary):

    summary[
        ["# of Website Clicks", "# of Purchase"]
    ].plot(
        kind="bar",
        figsize=(8, 5)
    )

    plt.title("Clicks vs Purchases by Campaign")
    plt.xlabel("Campaign")
    plt.ylabel("Count")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()


def plot_ctr_comparison(summary):

    summary["CTR (%)"].plot(
        kind="bar",
        figsize=(7, 5)
    )

    plt.title("CTR Comparison")
    plt.xlabel("Campaign")
    plt.ylabel("CTR (%)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()


def plot_cpa_comparison(summary):

    summary["CPA (USD)"].plot(
        kind="bar",
        figsize=(7, 5)
    )

    plt.title("CPA Comparison")
    plt.xlabel("Campaign")
    plt.ylabel("CPA (USD)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()