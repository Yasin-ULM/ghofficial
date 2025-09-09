# No-Whore-Mod
# Adds an option not to go whoring yourself out in the slums when Ben ask you to.

mod_plot = {
    "d8_ben_whore_3" : {
        "next" : "d8_ben_whore_4",
        "pc" : "upset",
        "txt" : "Emily:\nThe slums? Great... what am I supposed to do there?"
    },
    "d8_ben_whore_10" : {
        "next" : "d8_ben_whore_10_choice",
        "txt" : "Ben:\nAnd what if granny had a beard? We both know you want to do it.",
        "npc" : "img/npc/ben.png"
    },
    "d8_ben_whore_10_choice" : {
        "choice" : [["True", "No way!", "d8_ben_whore_10_nope"], ["True", "Play along.", "d8_ben_whore_11"]]
    },
    "d8_ben_whore_10_nope" : {
        "next" : "d8_ben_whore_10_nope_1",
        "pc" : "upset",
        "txt" : "Emily:\nYou\'re out of your fucking mind! I pull you out of trouble and this is what I get in return?"
    },
    "d8_ben_whore_10_nope_1" : {
        "next" : "d8_ben_whore_10_nope_2",
        "txt" : "Ben:\nOh c\'mon! I\'m doing you a favor here! I know you can fuck your way through school, but what then? What kind of job do you think you can get, huh? ",
        "npc" : "img/npc/ben.png"
    },
    "d8_ben_whore_10_nope_2" : {
        "next" : "d8_ben_whore_10_nope_3",
        "pc" : "neutral",
        "txt" : "Emily:\nI can be a... well, I could..."
    },
    "d8_ben_whore_10_nope_3" : {
        "next" : "d8_ben_whore_10_nope_4",
        "txt" : "Ben:\nWake up. Wake up and smell the ashes. You\'re never gonna be anyone! Learn to earn money with your body girl, that\'s all you ever gonna do!",
        "npc" : "img/npc/ben.png"
    },
    "d8_ben_whore_10_nope_4" : {
        "next" : "d8_ben_whore_10_nope_5",
        "pc" : "upset",
        "txt" : "Emily:\nBut..."
    },
    "d8_ben_whore_10_nope_5" : {
        "next" : "d8_ben_whore_10_nope_6",
        "txt" : "Ben:\nMoney for sex! What part of \'money for sex\' don\'t you understand? I know you\'re stupid, but you can\'t be that stupid! ",
        "npc" : "img/npc/ben.png"
    },
    "d8_ben_whore_10_nope_6" : {
        "next" : "d8_ben_whore_10_nope_7",
        "pc" : "upset",
        "txt" : "Emily:\nFucking fuck you Ben!"
    },
    "d8_ben_whore_10_nope_7" : {
        "next" : "d8_ben_whore_10_nope_8",
        "txt" : "Ben:\nYeah, I\'m not in the mood anymore. We\'re done here. You\'re waste of time. ",
        "npc" : "img/npc/ben.png"
    },
    "d8_ben_whore_10_nope_8" : {
        "next" : "d8_ben_whore_10_nope_9",
        "pc" : "upset",
        "txt" : "He turns around and starts walking away. You yell \'Asshole!\' to his back and he flips you off over his shoulder without even turning his head.",
        "cmd" : ["exec_once(\'save.rep_ben -= 2\')"]
    },
    "d8_ben_whore_10_nope_9" : {
        "eval_jump_to" : "\'d8_ben_whore_end_11\'"
    }
} 
for k,v in mod_plot.items(): 
    data.plot[k] = v 
