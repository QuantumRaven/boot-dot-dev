#!/usr/bin/env python3


def filter_messages(messages):
    filtered_messages = []
    words_removed = []
    for message in messages:
        words = message.split()
        non_bad = []
        counter = 0
        for word in words:
            if word == "dang":
                counter += 1
            else:
                non_bad.append(word)
        join_words = " ".join(non_bad)
        filtered_messages.append(join_words)
        words_removed.append(counter)

    return filtered_messages, words_removed
