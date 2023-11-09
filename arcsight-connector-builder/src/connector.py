from arcsight_sdk.connector import ConnectorBuilder

# Parser logic to normalize events
def parse_event(event):
    return {
        "name": event["title"],
        "severity": "5", 
        "source": "sample-source"
    }

builder = ConnectorBuilder.for_parser(parse_event)
builder.build("Sample Connector")