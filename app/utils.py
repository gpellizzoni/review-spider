from datetime import datetime, timezone

def convert_timestamp_to_date(timestamp_str):
    timestamp_ms = int(timestamp_str)
    timestamp_sec = timestamp_ms / 1000.0
    dt_object = datetime.fromtimestamp(timestamp_sec, tz=timezone.utc)
    formatted_date = dt_object.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'

    return formatted_date