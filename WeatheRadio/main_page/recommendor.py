import openai

openai.api_key = "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"

messages = [{"role": "system", "content": "You help with music recommendations"},]

def generate_song_recommendations(keywords):
    message = "suggest a songs that match the vibe of the keywords "+ str(keywords) +" just reply with the song suggestion dont reply with anything else(seroiusly). And remember, the songs should be different from the last 10 songs you recommended everytime i ask you again"
    messages.append({"role": "user", "content": message})
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )

    reply = chat.choices[0].message.content
    song = reply
    return song




