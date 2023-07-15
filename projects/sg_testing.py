rules = []

rules.append(
    {
        "IpProtocol":"tcp",
        "FromPort":80,
        "ToPort":80,
        "CidrIp": "0.0.0.0/0",
    }
)

rules.append(
    {
        "IpProtocol":"tcp",
        "FromPort":443,
        "ToPort":443,
        "CidrIp": "0.0.0.0/0",
    }
)

sec_group_ingress_rules = []

for rule in rules:
    template = f"""
      - IpProtocol: {rule['IpProtocol']}
        FromPort: {rule['FromPort']}
        ToPort: {rule['ToPort']}
        CidrIp: {rule['CidrIp']}
    """
    sec_group_ingress_rules.append(template)

template_header = f"""
InstanceSecurityGroup:
  Type: AWS::EC2::SecurityGroup
  Properties:
    GroupDescription: License SG for NAMEHERE
    VpcId: !Ref ItsVpc
    SecurityGroupIngress:
"""

# Need to get the stuff after the SG template
template_footer = ""

template = template_header.strip()
for sg in sec_group_ingress_rules:
    template = template + sg.rstrip()

print(template)