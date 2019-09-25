DOCUMENTATION = """
---
module: consul_acl_token

short_description: Manage consul token for consul 1.4 on api v1
description:
    - create, read, update, list, clone and delete consul tokens
    - Related Docs: https://www.consul.io/api/acl/tokens.html
options:
  host:
    description:
      - host of the consul agent defaults to localhost
    required: false
    default: localhost
  port:
    type: int
    description:
      - the port on which the consul agent is running
    required: false
    default: 8500
  scheme:
    description:
      - the protocol scheme on which the consul agent is running
    required: false
    default: http
    version_added: "2.1"
  mgmt_token:
    description:
      - a management token is required to manipulate the acl lists
  state:
    description:
      - whether the ACL pair should be present or absent
    required: false
    choices: ['present', 'absent']
    default: present
  accessor_id:
    description:
      - 
    required: false
    default: None
  secret_id:
    description:
      - 
    required: false
    default: None
  description:
    description:
      - 
    required: false
    default: None
  policies:
    description:
      - 
    required: false
    default: None
  roles:
    description:
      - 
    required: false
    default: None
  service_identities:
    description:
      - 
    required: false
    default: None
  local:
    description:
      - 
    required: false
    default: None
  expiration_time:
    description:
      - 
    required: false
    default: None
  expiration_ttl:
    description:
      - 
    required: false
    default: None
"""

from ansible.module_utils.basic import *
import consul

def main():
    module = AnsibleModule(
        argument_spec={
            "accessor_id": {
                "required": False,
                "type": "str",
                "default": ""
            },
            "secret_id": {
                "required": False,
                "no_log": True,
                "type": "str",
                "default": ""
            },
            "description": {
                "required": False,
                "type": "str"
            },
            "policies": {
                "required": False,
                "default": [],
                "type": "list"
            },
            "roles": {
                "required": False,
                "type": "list",
                "default": []
            },
            "service_identities": {
                "required": False,
                "type": "list",
                "default": []
            },
            "local": {
                "required": False,
                "default": False,
                "type": "bool"
            },
            "expiration_time": {
                "required": False,
                "default": "" ,
                "type": "str"
            },
            "expiration_ttl": {
                "default": "",
                "type": "str"
            },
        },
        supports_check_mode=True
    )
    accessor_id = module.params["accessor_id"]
    secret_id = module.params["secret_id"]
    description = module.params["description"]
    policies = module.params["policies"]
    roles = module.params["roles"]
    service_identities = module.params["service_identities"]
    local = module.params["local"]
    expiration_time = module.params["expiration_time"]
    expiration_ttl = module.params["expiration_ttl"]


    try:
        client = consul.Consul(host=configuration.host, port=configuration.port, scheme=configuration.scheme,
                         verify=configuration.validate_certs, token=token)

        if accessor_id == "":
        client.acl.list()
        client.acl.create()
        changed =
    except Exception, e:
        module.fail_json(msg=str(e))
    module.exit_json(changed=changed)

if __name__ == '__main__':
    main()
