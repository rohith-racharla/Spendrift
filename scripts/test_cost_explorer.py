from datetime import date, timedelta
from pprint import pprint

import boto3


def main() -> None:
    client = boto3.client("ce", region_name="us-east-1")

    end_date = date.today()
    start_date = end_date - timedelta(days=7)

    response = client.get_cost_and_usage(
        TimePeriod={
            "Start": start_date.isoformat(),
            "End": end_date.isoformat(),
        },
        Granularity="DAILY",
        Metrics=["UnblendedCost"],
        GroupBy=[
            {
                "Type": "DIMENSION",
                "Key": "SERVICE",
            }
        ],
    )

    pprint(response)


if __name__ == "__main__":
    main()