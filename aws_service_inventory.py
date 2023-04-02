"""
A python script that creates a list of AWS services and deletes two services.
By Joan Owusu
"""
#!/usr/bin/env python3.7

# 1) Set the AwsServices variable to be an empty list.
AwsServices = []
 
 # 2) Populate the list using "append."
AwsServices.append('EC2')
AwsServices.append('S3')
AwsServices.append('CloudFormation')
AwsServices.append('Lambda')
AwsServices.append('DynamoDB')
AwsServices.append('GuardDuty')
AwsServices.append('Neptune')

# 3) Print the Aws Services list and the length of the list.
print() # Empty line.
print("AWS Services list.")
print(len(AwsServices), "Aws Services: ", AwsServices)

print()

# 4) Remove "EC2" and "Lamda" from the Aws Services list by name.
print("New AWS Services list with 'EC2' and 'Lambda' removed.")
AwsServices.remove('EC2')
AwsServices.remove('Lambda')

# 5) Print the new Aws Services list and the new length of the list.
print(len(AwsServices), "Aws Services: ", AwsServices)
print()
