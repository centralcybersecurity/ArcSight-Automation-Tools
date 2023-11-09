from arcsight_sdk import ArcSightLogger

LOW_SEVERITY_THRESHOLD = 3
HIGH_SEVERITY_THRESHOLD = 8

logger = ArcSightLogger()

for case in logger.get_cases():

  if case.severity < LOW_SEVERITY_THRESHOLD:
    case.close("Low severity")

  elif case.severity > HIGH_SEVERITY_THRESHOLD:  
    case.reopen("High severity")
    case.assign("Security Team")

  else:
    case.update("Triaged")

logger.flush_cases()