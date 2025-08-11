# Validates email address by checking username and domain separetely;

email = input("What's your email? ").strip();

username, domain = email.split("@");

if username and "." in domain: #{
    print("Valid");
#}
else: #{
    print("Invalid")
#}