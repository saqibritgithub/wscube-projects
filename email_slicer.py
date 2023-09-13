email=input("Please enter your email :").strip()
user_name=email[:email.index("@")]
domain_name=email[email.index("@")+1:]
look=(f"your user name is'{user_name}'and your domain name is'{domain_name}'")
print(look)