import requests
import json
while True:
    subreddit_name = input("Enter a subreddit to scrape: ")

    print("\nSort by:")
    print("1. Hot")
    print("2. top")
    print("3. New")
    sort_choice = input("\nEnter sort type (hot/top/new)")


    if sort_choice not in ["hot", "top", "new"]:
        print("Invalid choice. Defaulting to 'hot'.")
        sort_choice = "hot"

    keyword = input("Filter by keyword (or press Enter to skip)").lower()


    url = f"https://www.reddit.com/r/{subreddit_name}/hot.json?limit=10"
    headers = {"User-Agent": "my_reddit_scraper/1.0"}


    response = requests.get(url, headers=headers)
    data = response.json()

    posts = data["data"]["children"]

    if keyword:
        posts = [post for post in posts if keyword in post["data"]["title"].lower()]

    print(f"\n r/{subreddit_name} - {sort_choice} posts")

    if keyword:
        print(f"Filtered by keyword: '{keyword}'\n")


    print()
    if not posts:
        print("No posts found.")
    else:

        for i, post in enumerate(posts, start=1):
            title = post["data"]["title"]
            score = post["data"]["score"]
            comments = post["data"]["num_comments"]
            link = post["data"]["url"]
        
        print(f"{i}. {title}")
        print(f"Upvotes: {score} | Comments: {comments}")
        print(f" Link: {link}\n")
    cont = input("Do you want to scrape another subreddit? (y/n): ")
    if cont.lower() != 'y':
        break

#try to commit