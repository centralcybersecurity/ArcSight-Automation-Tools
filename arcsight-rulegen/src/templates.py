from jinja2 import Template

template = Template("""
<Rule name="{{name}}" severity="{{severity}}">
  <Conditions>
    <Condition>
      <ApplyTo>eventA</ApplyTo> 
      <Expression>
        <AND>
          <Matches>
            <Field name="deviceEventClassId">{{class_id}}</Field>
          </Matches>
        </AND>
      </Expression>
    </Condition>
  </Conditions> 
</Rule>
""")