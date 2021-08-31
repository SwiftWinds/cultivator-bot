import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()

constitution = '''
We, allison and blackholeDematerializer/Reactor, on behalf of the people of UCSB CS Students 2024, submit a resolution to improve the democratic processes in this server. We ask for the following terms and no less:

1.That a democracy bot, created by mingus slingus, (a) be added to the server and (b) be assigned sufficient permissions for the following actions:
1a. Creating new text and voice servers.
1b. Creating new roles.
1c. Assigning new roles (including the DJ role).
1d. Creating new emotes.

2. That the democracy bot perform each of the relevant actions either when (a) it reaches a net vote (reactions in favor of - reactions against) consisting of at least 1/3 the total members among the people together with an approving vote from any moderator, or (b) when it reaches a net vote consisting of at least 1/3 of the total members. That everyone is eligible to vote, and that there are no vetoes.

3. That the mods do not interfere with the natural democratic process unless alternate accounts are involved.

4. That a democracy channel be established solely for the purpose of democratic matters.

5. That two additional people be promoted to the role of moderator, elected by a democratic process.
'''

phrases = ['No XD', "do you have a wife's boyfriend?", 'pozzed', 'wanna see some racist memes?', 'too lazy to read XD']


def clean_message(message):
    '''This function strips everything but alpha characters'''
    cleaned_message = ''
    for char in message:
        if char.isalpha():
            cleaned_message += char
    return cleaned_message


def extract_tag(message):
    '''This function extracts the tag from a message'''
    tag = ''
    num_mentions = 0
    start_index = None
    end_index = None
    for char in message:
        if char == '<':
            start_index = message.index(char)
            num_mentions += 1
        if char == '>':
            end_index = message.index(char) + 1

    tag = message[start_index: end_index]
    if num_mentions > 1:
        return -1


    elif num_mentions == 1:
        return tag

    else:
        return None


# create a client
client = discord.Client()


@client.event
async def on_ready():
    # Bot functionality
    channel_id = int(os.getenv("DISCORD_CHANNEL_ID"))
    general_channel = client.get_channel(channel_id)
    await general_channel.send("I've arrived")


@client.event
async def on_message(message):
    input = clean_message(message.content).lower()
    tag = extract_tag(message.content)

    if 'bull' in input and message.author != client.user:
        general_channel = client.get_channel(message.channel.id)
        await general_channel.send('The bull is HIV positive!')

    if input.startswith('based') and message.author != client.user:
        general_channel = client.get_channel(message.channel.id)
        await general_channel.send('based.')

    # Cultivator keyword
    if input.startswith('heycultivator'):
        random_phrase = random.choice(phrases)
        random_percent = random.randrange(0, 100)

        # soyboy branches
        if 'soyboy' in input:
            if tag == None:
                general_channel = client.get_channel(message.channel.id)
                await general_channel.send('LOL you have to give me someone to rate idiot.')

            elif tag == -1:
                general_channel = client.get_channel(message.channel.id)
                await general_channel.send('Bruh moment! I can only rate one person at a time!')

            else:
                general_channel = client.get_channel(message.channel.id)
                message = tag + ' is ' + str(random_percent) + '% soyboy'
                await general_channel.send(message)

        elif 'constitution' in input:
            general_channel = client.get_channel(message.channel.id)
            await general_channel.send(constitution)

        else:
            general_channel = client.get_channel(message.channel.id)
            await general_channel.send(random_phrase)

    if input == "whatsyourbodycount":
        amount = str(random.randrange(0, 100000))
        general_channel = client.get_channel(message.channel.id)
        message = "I'm 18 and I've already slept with " + amount + " women already."
        await general_channel.send(message)

    if len(input) > 150:
        general_channel = client.get_channel(message.channel.id)
        await general_channel.send("too lazy didn't read XD")


# Run client on server
client.run(os.getenv("DISCORD_API_KEY"))
