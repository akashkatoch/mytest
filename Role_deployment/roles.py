import logging
import urllib3
import requests
import json

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def add_user_in_tenant(header):
    urllib3.disable_warnings()
    f = open('role.txt')
    data = json.load(f)
    try:
        for tenants in data["tenant"]:
            for new_account in data["account"]:
                for new_member in data["members"]:
                    logging.info(f'Gathering information to add {new_member} in account {new_account} under tenant {tenants}')
                    request_url = f'https://avm.mckinsey.com/role/aws.k8savm.io/{tenants}/{new_account}.{data["role"]}/group/access/member/add/{new_member}'
                    response = requests.post(request_url, headers=header, verify=False)


                    logging.info(f'user {new_member} added in {tenants}/{new_account}')
    except Exception as e:
        logging.info(f'Error received: {e}')


if __name__ == '__main__':
    token = "token"
    header = {
        'accept': 'application/json',
        'authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }

    add_user_in_tenant(header)


