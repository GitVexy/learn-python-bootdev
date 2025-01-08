def filter_messages(messages):
    filtered_list = []
    bad_word_count = []
    for message in messages:
        counter = 0
        filtered_message = []
        
        for word in message.split():
            if word == "dang":
                counter += 1
            else:
                filtered_message.append(word)

        filtered_list.append(" ".join(filtered_message))
        bad_word_count.append(counter)
    return filtered_list, bad_word_count