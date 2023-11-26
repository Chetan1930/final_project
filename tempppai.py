from bardapi import BardCookies
import datetime

cookie_dict = {
    "__Secure-1PSID" : "cgi86mWqIv9--CNwk_j0TH4dd2ZPiOPH4DT9m81GHXbo2Rd2YbpWH5aNipaEjUjjOx1fcA.",
    "__Secure-1PSIDTS" : "sidts-CjEBNiGH7vIS89b4_IuEaw4QbG4PfqJ3JXDHnoYiDC-TWotz8tiEyQ0X_SW6ZtnJAnahEAA",
    "__Secure-1PSIDCC" : "ACA-OxMs816gt8lIq9j0ateZvKEuNImwc1G0AZXvyMRj5sBHns9ByH5yn66uSwjn8k80QyOA_A"

}

bard = BardCookies(cookie_dict = cookie_dict)

while True:
    Query = input("Enter Your Query: ")
    Reply = bard.get_answer(Query)['content']
    print(Reply)