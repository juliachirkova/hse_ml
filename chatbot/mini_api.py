#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from openai import OpenAI

PROXY_API_KEY = ""

client = OpenAI(
    api_key=PROXY_API_KEY,
    base_url="https://api.proxyapi.ru/openai/v1",
)


def mini_chat(messages):
    chat_completion = client.chat.completions.create(max_tokens=1024, model="gpt-4o-mini", messages=messages)

    input_tokens, output_tokens = chat_completion.usage.prompt_tokens, chat_completion.usage.completion_tokens
    input_cost, output_cost = 0.0432, 0.1728
    return (
        chat_completion.choices[0].message.content,
        round((input_tokens / 1000 * input_cost + output_tokens / 1000 * output_cost), 2),
    )
