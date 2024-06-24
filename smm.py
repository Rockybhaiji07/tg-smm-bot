from telegram import Bot
from telegram.error import TelegramError

# Replace 'YOUR_BOT_TOKEN' with the token provided by BotFather
bot_token = '6958175960:AAFbsEQ19lATd6NUCOhyhyi6ikSkoFvOfGk'

def join_group_or_channel(-1001555092484):
    try:
        bot = Bot(token=6958175960:AAFbsEQ19lATd6NUCOhyhyi6ikSkoFvOfGk)
        bot.join_chat(@ownerRocky)
        print(f"Successfully joined the group/channel with ID: {@OwnerRocky}")
    except TelegramError as e:
        print(f"Failed to join the group/channel: {e}")

if __name__ == "__main__":
    # Replace 'GROUP_OR_CHANNEL_ID' with the ID of the group or channel you want to join
    group_or_channel_id = '-1001555092484'
    join_group_or_channel(-1001555092484)

//tool made my codeprofessor on telegram
