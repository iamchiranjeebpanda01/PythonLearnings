emailID = input("Enter your email ID: ")

emailIDSplitList = emailID.split('@')

userID = emailIDSplitList[0]
domainName = emailIDSplitList[1]

print("Username is: " + userID + " and domain name is: " + domainName)