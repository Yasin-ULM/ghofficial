# Groundhogday Mod v1 for SlutED

data.plot["start_day_18"] =  { "eval_jump_to" : "'start_gh'" }
data.plot["start_gh_4"] = {
        "next" : "start_gh_5",
        "txt" : "...",
        "img" : "img/gh_day/morning559.webp",
        "cmd" : ["save.breakfast = 0", "set_hard_datetime(day=17, hour=5)", "save.morning_shower = 0"]
    }

print('Groundhogday Mod v1 installed!')

