# ArcSight Threat Feed Importer

Imports threat intelligence feeds into ArcSight.

## STIX

STIX (Structured Threat Information Expression) is a standard format for sharing threat intelligence information between organizations. STIX feeds contain structured data about latest threats, malware, threat actors, and other IOCs (indicators of compromise).

Many threat intel companies and open source feeds publish STIX feeds regularly with new threat data.

## Threat feed importer code:

1. Fetches these STIX feeds
2. Looks for "indicator" objects - these contain threat data
3. Checks if the indicator has a "pattern" - this is a technical signature to detect the threat
4. Parses this pattern into a structured format our system understands
5. Uses the ArcSight SDK to import each pattern as a detection rule

So in simple terms, we are automatically getting latest threat data from STIX feeds, extracting the technical threat detection logic, and importing them into ArcSight.

## Benefits:

Faster deployment of new threat detection rules
Saves a lot of manual effort for our security team
Leverages latest threat intel from external feeds
Helps improve our threat detection coverage

This allows ArcSight to stay up-to-date with new threats automatically. The security team now has more time to focus on specialized custom detections vs routine work.

## Usage

1. Update `src/importer.py` with feed URL
2. Run `python src/importer.py`
3. Threat events will be imported into ArcSight