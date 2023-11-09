from arcsight_sdk import ArcSightRule
from templates import template

def generate_rule(name, severity, class_id):
  rule_xml = template.render(name=name, severity=severity, class_id=class_id)
  return ArcSightRule.from_xml(rule_xml)

rule = generate_rule("Test Rule", "High", "device::class::id")
rule.export("output/test.xml")