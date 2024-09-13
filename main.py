from senha import chave
import requests
import json

headers = {"Authorization": f"Bearer {chave}", "Content-Type": "application/json"}
link = "https://api.openai.com/v1/chat/completions"
id_modelo = "gpt-3.5-turbo"

body_mensagem = {
    "model": id_modelo,
    "messages": [
        {"role": "user",
         "content": "Desenvolver uma aplicação que emprega a API do ChatGPT para gerar conceitos inovadores de startups com base nos inputs dos usuários."
         }
    ]
}

body_mensagem = json.dumps(body_mensagem)
requisicao = requests.post(link, headers=headers, data=body_mensagem)
print(requisicao)
print(requisicao.text)

