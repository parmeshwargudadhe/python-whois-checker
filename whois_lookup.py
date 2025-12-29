import whois

w = whois.whois("google.com")
print(w.domain_name)
print(w.expiration_date)
print(w.status)
