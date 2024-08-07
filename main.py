import instaloader

def download_instagram_profile_picture(username):
    loader = instaloader.Instaloader()

    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        loader.download_profilepic(profile)
        print(f"Profile picture of '{username}' downloaded successfully!")
    except Exception as e:
        print(f"Failed to retrieve profile picture: {e}")

username = "example.name"
download_instagram_profile_picture(username)