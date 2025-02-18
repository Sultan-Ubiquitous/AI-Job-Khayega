from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
import os
import re
import json

load_dotenv()

llm = GoogleGenerativeAI(model='gemini-2.0-flash', google_api_key=os.getenv("GOOGLE_API_KEY"))





def userinput():
    prompt = input('describe your component in as much details as possible, ideally give a description for functionalities and other for styling options for the component: \n')
    output = llm.invoke(
        f'''You are an expert Product Manager, UI/UX expert and an expert designer whose job is to take in
          user input and create effective description for other expert coders
          Take this user description {prompt}
          ande give a JSON output with 2 key value pairs, one is functionalities other is styling
          in functionalities use your above mentioned expertise to generate a breif and detailed description for functionalities of the coding component 
          as a Product manager and in styling give a breif and detailed description for styling the component as a designer and UI/UX expert.
          Only give JSON output and nothing else '''
    )
    json_match = re.search(r"{.*}", output, re.DOTALL)
    if json_match:
        json_object = json.loads(json_match.group(0))
        functionalitites = json_object["functionalities"]
        styling = json_object["styling"]
        return functionalitites, styling
    else:
        print("No JSON object found.")
        return None, None


def webinput(prompt):
    
    output = llm.invoke(
        f'''You are an expert Product Manager, UI/UX expert and an expert designer whose job is to take in
          user input and create effective description for other expert coders
          Take this user description {prompt}
          ande give a JSON output with 2 key value pairs, one is functionalities other is styling
          in functionalities use your above mentioned expertise to generate a breif and detailed description for functionalities of the coding component 
          as a Product manager and in styling give a breif and detailed description for styling the component as a designer and UI/UX expert.
          Only give JSON output and nothing else '''
    )
    json_match = re.search(r"{.*}", output, re.DOTALL)
    if json_match:
        json_object = json.loads(json_match.group(0))
        functionalitites = json_object["functionalities"]
        styling = json_object["styling"]
        return functionalitites, styling
    else:
        print("No JSON object found.")
        return None, None
    


def functionalityAgent(description):
    output = llm.invoke(f'''
    You are an expert frontend react and javascript developer who is well versed with latest trends in react, based on this 
    these details
    {description}
     you need to code a react component, code it wihtout any styling but ensure all mentioned functionalities are there and working 
    as mentioned in the given description.
    Only return me .jsx code
    ''')
    return output

def stylingAgent(code, description):
    output = llm.invoke(f'''
   You are an expert tailwind CSS and UI/UX designer. your job is to style this code 
   {code}
   with this given description
   {description}
   analyze the description properly and 
   only return a .jsx component styled with tailwind css
    '''
    )
    return output


def orchestration():
    description = userinput()
    code = functionalityAgent(description[0])
    styledCode = stylingAgent(code, description[1])

    return styledCode

def webOrchestration(prompt):
    description = webinput(prompt)
    code = functionalityAgent(description)
    finalCode = stylingAgent(code, description)
    return finalCode


if __name__ == "__main__":
    print("Aight tight tigth, Working...")
    print(webOrchestration(prompt = 'Make me a landing page for a luxury hotel with luxurious aesthetic and typography, put heavy emphasis on typography by using various composition and fonts'))

