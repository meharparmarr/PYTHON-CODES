def calculate_love_score(name1, name2):
    combined_names = name1.lower() + name2.lower()
    true_count = combined_names.count("t") + combined_names.count("r") + combined_names.count("u") + combined_names.count("e")
    love_count = combined_names.count("l") + combined_names.count("o") + combined_names.count("v") + combined_names.count("e")
    love_score = int(str(true_count) + str(love_count))
    return love_score

def determine_message(love_score):
    if love_score < 10 or love_score > 90:
        return f"The Love Calculator is calculating your score...Your score{love_score}."
    elif 40 <= love_score <= 50:
        return f"The Love Calculator is calculating your score...Your score {love_score}."
    else:
        return f"Your score is {love_score}."

# Example usage
name1 = input()
name2 = input()

score = calculate_love_score(name1, name2)
message = determine_message(score)
print(message)
