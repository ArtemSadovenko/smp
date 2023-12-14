import requests

class JSONPlaceholderAPI:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"

    def get_posts(self):
        endpoint = f"{self.base_url}/posts"
        response = requests.get(endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_post(self, post_id):
        endpoint = f"{self.base_url}/posts/{post_id}"
        response = requests.get(endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            return None

# Creating an instance of the JSONPlaceholderAPI class
json_placeholder = JSONPlaceholderAPI()

# Fetching all posts
posts = json_placeholder.get_posts()

if posts:
    print("All Posts:")
    for post in posts:
        print(f"Post ID: {post['id']}, Title: {post['title']}")

    post_id = int(input("Enter the ID of the post to fetch details: "))
    post_details = json_placeholder.get_post(post_id)
    if post_details:
        print("\nPost Details:")
        print(f"Title: {post_details['title']}")
        print(f"Body: {post_details['body']}")
        print(f"User ID: {post_details['userId']}")
    else:
        print("Failed to fetch post details.")
else:
    print("No posts found.")
