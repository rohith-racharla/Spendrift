from __future__ import annotations

from typing import Any


class CostDataStore:
    """Store normalized cost data in Amazon S3."""

    def __init__(
        self,
        bucket_name: str,
        client: Any | None = None,
    ) -> None:
        if client is None:
            import boto3

            client = boto3.client("s3")

        self.bucket_name = bucket_name
        self.client = client

    def put_json(
        self,
        key: str,
        content: str,
    ) -> None:
        """Write JSON content to S3."""

        self.client.put_object(
            Bucket=self.bucket_name,
            Key=key,
            Body=content.encode("utf-8"),
            ContentType="application/json",
        )