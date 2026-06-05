import requests
import json
import time

BASE = "https://api.github.com"

# Please review this PR as you would in a real code review.
# Leave comments on anything you would flag.

def get_repos(u, h={}):
    r = []
    p = 1
    while True:
        url = BASE + "/users/" + u + "/repos?per_page=100&page=" + str(p)
        resp = requests.get(url, headers=h)
        data = resp.json()
        if len(data) == 0:
            break
        r += data
        p += 1
    return r


def fetch_stats(username, token=None):
    h = {}
    if token:
        h["Authorization"] = "token " + token
    try:
        repos = get_repos(username, h)
        stars = 0
        forks = 0
        for repo in repos:
            stars += repo["stargazers_count"]
            forks += repo["forks_count"]
        print("Stars: %s, Forks: %s" % (stars, forks))
        return {"stars": stars, "forks": forks}
    except:
        print("something went wrong")
        return None


def main():
    users = ["torvalds", "gvanrossum", "kennethreitz"]
    results = {}
    for u in users:
        results[u] = fetch_stats(u)
        time.sleep(1)
    with open("stats.json", "w") as f:
        json.dump(results, f)


if __name__ == "__main__":
    main()
