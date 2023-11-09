# ArcSight Report Generator

Generates various security reports from ArcSight.

## How It Works

This script allows us to automatically generate security reports from ArcSight on a scheduled basis. Some examples of the reports we can produce:

Watchlist event report - Shows all security events related to high profile assets we have on a watchlist, like critical servers or customer data. Useful for monitoring activity around our sensitive assets.

Top alerts report - Ranks the most frequent security alerts from ArcSight. Helps highlight patterns in the top threats we face.

User anomaly report - Detects unusual login or access patterns for users that could indicate compromised credentials.

Rather than having analysts pull these reports manually, the script does it automatically and delivers them as PDFs to relevant stakeholders.

## Key benefits:

Frees up security team to focus on higher value tasks than report building.

Ensures reports are generated consistently on time rather than relying on individual users.

Can customize reports to focus on security insights that matter most to our business.

Easy to add new report types to the script as needed.

The automated delivery of custom reports on relevant metrics can help make security data more actionable and accessible for leadership. It can surface trends and risks that otherwise might be missed in manual reporting.

## Usage

1. Update report types in `src/report_generator.py`
2. Run `python src/report_generator.py`
3. Reports will be automatically generated as PDFs