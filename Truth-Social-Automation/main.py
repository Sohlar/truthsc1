from TruthPy import User
import time
from win10toast import ToastNotifier

async def main(email,password,id,waitTime,message):

    user = User()
    await user.login(email,password)

    # post = await user.post("Hello World!, This is a test post from TruthPy")
    feedPosts = []

    feed = await user.feed.get_feed()
    for post in feed:
        # print(post.account["id"])
        feedPosts.append(post.id)
    time.sleep(5)

    while True:
        try:
            feed = await user.feed.get_feed()

            for post in feed:
                if post.id in feedPosts:
                    print('do nothing')
                else:
                    #check if post is of the same user
                    if post.account["id"] == id:
                        print('my post. Dont comment')
                    else:
                        feedPosts.insert(0, post.id)
                        print('nice')
                        await post.reply(user,message)  
            
            print("-----")

            time.sleep(waitTime)

        except Exception as e:
            print(e)
            toast.show_toast(
                "Truth Social Automation",
                f"Account email {email} got disabled. Please try to run again or change credentials",
                duration = 20,
            )
            f = open("disabled_accounts.txt","a")
            f.write(f'{email} {password} {id}\n')
            return


if __name__ == "__main__":
    import asyncio
    import json

    toast = ToastNotifier()

    with open('credentials.json') as f:
        data = json.load(f)
 
    asyncio.run(main(data["email"],data["password"],data["id"],data["waitTime"],data["message"]))
