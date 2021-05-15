from my_instagram_bot import instagram_bot

myusername = input('Please enter the username: ')
mypassword = input('Please enter the password: ')
ig_bot = instagram_bot()
ig_bot.login(myusername,mypassword)
ig_bot.like_hashtag(['蜷尾家','茶壺山','漁光島'])