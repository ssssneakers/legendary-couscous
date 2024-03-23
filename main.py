from transformers import AutoTokenizer


def count_tokens(text):
    tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")
    return len(tokenizer.encode(text))


assistant_content = (
    "Continue your answer, based on the previous answers that I will now provide you,you need to continue the answer "
    "strictly on the topic that is given in the previous answers.")


def system(sub, lev):
    system_content = (
        f"You are a teacher in the subject: {sub}, you need to explain the questions that the user will ask as "
        f"informatively as possible, the user has a certain level of knowledge: {lev}")
    return system_content


max_tokens_in_task = 300
