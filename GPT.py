import requests
import logging
from config import serv
from main import assistant_content

error = ('<b>Состояние: Слишком большое\n'
         'количество символов! </b>\n'
         '<i>Пожалуйста, задайте новый\n'
         'вопрос, это обнулит ваш\n'
         'предыдущий диалог.</i>')


class Question_gpt2:
    def __init__(self):
        self.temperature = 0.7
        self.max_tokens = 100
        self.server = serv

    def promt(self, result1, system_content):
        try:
            resp = requests.post(
                self.server,
                headers={"Content-Type": "application/json"},
                json={
                    "messages": [
                        {"role": "system", "content": f'{system_content}'},
                        {"role": "user", "content": f'{result1.text}'},
                    ],
                    "temperature": self.temperature,
                    "max_tokens": self.max_tokens
                }
            )
            data = resp.json()

            def error_gpt(resp, data):
                if resp.status_code < 200 or resp.status_code >= 300:
                    error = 'Произошла ошибка'
                    logging.error(str(resp.status_code))
                    return error
                if 'error' in data:
                    error1 = 'Произошла ошибка на стороне сервера.'
                    logging.error(str(f'{data["error"]}'))
                    return error1(resp, data)

            answer = data['choices'][0]['message']['content']
            return answer

        except Exception as e:
            error_gpt1 = error
            logging.error(str(e))
            return error_gpt1


class Continue_text_gpt:
    def __init__(self):
        self.temperature = 0.7
        self.max_tokens = 100
        self.server = serv
        self.assistant = assistant_content

    def gpt(self, promt1, system_content):
        try:
            resp = requests.post(
                self.server,
                headers={"Content-Type": "application/json"},
                json={
                    "messages": [
                        {"role": "system", "content": f'{system_content}'},
                        {"role": "assistant", "content": f'{self.assistant} {promt1}'},
                    ],
                    "temperature": self.temperature,
                    "max_tokens": self.max_tokens
                }
            )
            data = resp.json()

            def error_gpt(resp, data):
                if resp.status_code < 200 or resp.status_code >= 300:
                    error = 'Произошла ошибка'
                    logging.error(str(resp.status_code))
                    return error
                if 'error' in data:
                    error1 = 'Произошла ошибка на стороне сервера.'
                    logging.error(str(f'{data["error"]}'))
                    return error1(resp, data)

            continuation = data['choices'][0]['message']['content']
            return continuation

        except Exception as e:
            error1 = error
            logging.error(str(e))
            return error1
