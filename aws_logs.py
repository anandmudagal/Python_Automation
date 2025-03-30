# aws_logs.py
import boto3
from datetime import datetime, timedelta

def fetch_cloudwatch_logs(log_group, stream_name):
    client = boto3.client('logs')
    end_time = int(datetime.now().timestamp() * 1000)
    start_time = int((datetime.now() - timedelta(minutes=5)).timestamp() * 1000)

    response = client.get_log_events(
        logGroupName=log_group,
        logStreamName=stream_name,
        startTime=start_time,
        endTime=end_time,
        limit=20
    )
    return [event['message'] for event in response['events']]
