import boto3

# # AWS IAM Roles Search 
def list_iam_roles():
    iam_client = boto3.client("iam")
    paginator = iam_client.get_paginator("list_roles")
    roles = []
  
    for page in paginator.paginate():
        for role in page["Roles"]:
            roles.append(role["RoleName"])
    return roles
  
if __name__ == "__main__":
    roles = list_iam_roles()

    if roles:
        print("IAM Roles in the AWS Account:")
        for role in roles:
            print(role)
    else:
        print("No IAM roles found.")
