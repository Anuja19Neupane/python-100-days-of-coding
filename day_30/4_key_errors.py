fb_post=[
    {'likes':21,'comments':2},
    {'likes':24,'comments':4},
    {'comment':56,'share':5}
    
]

total_likes=0

for post in fb_post:
    try:
        total_likes=total_likes+post['likes']
    except KeyError:
        pass

print(total_likes)
