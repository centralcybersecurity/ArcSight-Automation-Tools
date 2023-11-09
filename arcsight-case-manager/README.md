# ArcSight Case Manager

Automatically handles ArcSight cases based on severity.

This script allows us to automatically triage and handle a large volume of security cases in ArcSight, based on severity.

For example, let's say over the weekend we get 500 cases flagged in ArcSight for potential security issues detected in our network. Our security team would have to go through each case manually to assess severity and determine next steps.

## With the case manager script:

Low severity cases (e.g. informational events) are automatically closed to reduce noise. This could be 200 out of 500 cases.

High severity cases (e.g. critical threats) are escalated and assigned to the security team. This ensures urgent cases get immediate attention. Maybe 20 out of 500 cases.

The remaining moderate severity cases are updated with a "triaged" status so the team knows they have been reviewed.

So in one run, the script has automated the bulk of the mundane case handling work, allowing our security team to focus on the most critical threats first thing Monday morning.

It reduces the case backlog, ensures urgent cases are acted on fast, and gives us metrics on how many cases fell into each category.

The script is customizable as well - we can tweak the severity thresholds or logic as needed to best suit our case handling policies and processes.

## Usage

1. Update case severity thresholds in `src/case_manager.py`
2. Run `python src/case_manager.py`
3. Cases will be automatically created, updated and closed