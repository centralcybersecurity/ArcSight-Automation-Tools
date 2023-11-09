# ArcSight SmartConnector Builder

This builds custom SmartConnectors for ArcSight ESM.

# ArcSight SmartConnector SDK for Python to build custom connectors:

Rapid development: You can build and modify connectors quickly using Python without needing to compile or deploy Java code.

Flexible parsing: Python makes it easy to parse diverse data sources and normalize to ArcSight events using regular expressions, JSON processing, etc.

Leverages existing libraries: Can utilize Python data processing libraries like pandas for transformation and normalization.

Easier troubleshooting: Can add logging, breakpoints, etc to debug connector logic during development.

Portability: The connector can be run anywhere Python runs including containers. No need to install Connector Appliance.

Streamlined deployment: The connector is packaged as a single executable so deployment is simplified.

Community support: Can leverage Python community and ecosystem for libraries, examples, and support.

Future-proof: Using Python will allow tapping into new ArcSight connector features as the SDK evolves.

## Usage

1. Update `src/connector.py` with parser logic 
2. Run `pip install -r requirements.txt`
3. Run `python src/connector.py`
4. New SmartConnector will be created