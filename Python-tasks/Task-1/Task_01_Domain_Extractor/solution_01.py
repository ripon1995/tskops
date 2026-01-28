urls = [
    "https://api.github.com/v3",
    "https://scholar.google.com/",
    "https://www.jstor.org/",
    "https://www.sciencedirect.com/check/",
    "https://www.researchgate.net/test.test/",
    "https://www.researchgate.net/v1/v2",
]

domains = []
for url in urls:
    path = url.split("//")[-1].split("/")[0]
    parts = path.split(".")[1:]
    domain = ".".join(parts)
    domains.append(domain)


print(*domains, sep="\n")
