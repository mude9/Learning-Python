# ---------------------------
# -- Practical Slice Email --
# ---------------------------

theName = input('What\'s Your Name ?').strip().capitalize()
theEmail = input('What\'s Your Email ?').strip()
                        #start from 0 to @
theUsername = theEmail[:theEmail.index("@")]

                     #start from letter after @ to the end
theWebsite = theEmail[theEmail.index("@") + 1:]

print(f"Hello {theName} Your Email Is {theEmail}")
print(f"Your Username Is {theUsername} \nYour Website Is {theWebsite}")

# email = "Osama@elzero.org"
# print(email[:email.index("@")])