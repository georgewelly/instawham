from bs4 import BeautifulSoup

def extract_usernames_from_html(path):
    with open(path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
        links = soup.find_all("a", href=True)
        usernames = set()
        for a in links:
            href = a['href']
            if href.startswith("https://www.instagram.com/"):
                username = href.split("https://www.instagram.com/")[1].strip("/")
                usernames.add(username.lower())
        return usernames

PATH_TO_FOLLOWERS = "followers_1.html" # might need to be changed
PATH_TO_FOLLOWING ="following.html"
# Load followers and following
followers = extract_usernames_from_html()
following = extract_usernames_from_html("following.html")

# Analysis
not_following_back = following - followers
fans = followers - following
ratio = len(followers) / len(following) if following else 0

# Output
print(f"👥 Followers: {len(followers)}")
print(f"➡️ Following: {len(following)}")
print(f"📊 Follower/Following Ratio: {ratio:.2f}")

print(f"\n❌ Not following you back ({len(not_following_back)}):")
for user in sorted(not_following_back):
    print(f"- https://www.instagram.com/{user}")

print(f"\n⭐ You don’t follow back ({len(fans)}):")
for user in sorted(fans):
    print(f"- https://www.instagram.com/{user}")
