from arcsight_sdk import ArcSightLogger
import pdfkit

watchlist_report = logger.get_watchlist_events_report()
top_alerts_report = logger.get_top_alerts_report()

pdfkit.from_string(watchlist_report, 'watchlist_report.pdf')
pdfkit.from_string(top_alerts_report, 'top_alerts_report.pdf')