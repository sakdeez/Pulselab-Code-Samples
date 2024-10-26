def NameExtractor(names):
    names = names.strip()
    name_array = names.split(',')
    return [name.strip() for name in name_array]

def NamePrinter(names):
    name_array = NameExtractor(names)
    message_type = input("Which message would you like? 'starter' or 'follow up': ").lower()

    if message_type == "starter":
        for name in name_array:
            print(f"Hey {name}, I was wondering if you work with buyers or sellers?")
    else:
        FollowUp(names)

def FollowUp(names):
    follow_up_messages = {
        1: "This is unbelievable, {name}! I was sitting at my local cafe for my coffee to brew\n"
           "And then on the coffee I see my favorite real estate agent! This must be a sign for us to connect. "
           "Let's schedule a call to chat this week. What day are you available this week?",

        2: "Best Real Estate Agent’s to-do’s:\n\n"
           "1. Get leads\n"
           "2. Close deals\n"
           "3. What day are you free this week for a quick call?",

        3: "Hi {name}! Just a daily reminder, success is one conversation away. Let’s talk and make it happen.",

        4: "Your custom follow-up message here for Follow-up 4",

        5: "Here’s a riddle for you, {name}!\nWhat helps agents close more deals and never sleeps?",

        6: "Hey {name}, are you having a busy day today?",

        7: "I just shared an insane tip with a few agents, would you like it too?",

        8: "I can guarantee this would be you if we can chat further.",

        9: "I have a strategy that I wanna specially reveal to you, {name}. It’s so crazy that the more you know about it, "
           "the more you realize how overpowered it is!",

        10: "Alright {name}, I guess you’re not really interested in growing your business, so I won’t message you anymore. Good luck!"
    }

    name_array = NameExtractor(names)
    while True:
        try:
            f_num = int(input("Which follow-up number would you like? 1-10: "))
            if 1 <= f_num <= 10:
                for name in name_array:
                    print(follow_up_messages[f_num].format(name=name))
                break
            else:
                print("Please enter a valid integer ranging from 1-10.")
        except ValueError:
            print("Please enter a valid integer.")


