import logging

import azure.functions as func
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    llm = OpenAI(temperature=0.0, model_name='')
    prompt = PromptTemplate(
        input_variables=['name'],
        template="名前「{name}」に似合うニックネームをつけてください。"
    )
    chain = LLMChain(llm = llm, prompt=prompt)


    try:
        req_body = req.get_json()
    except ValueError:
        pass
    else:
        name = req_body.get('name')

    if name:
        nickname = chain.run(name)

        return func.HttpResponse(nickname)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
