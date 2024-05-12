import os
import time
import google.generativeai as genai
import pyfiglet

# Limpar o console
os.system('cls' if os.name == 'nt' else 'clear')

google_api_key = "AIzaSyARF9qQOhk4KZgBYbBdDGTTcku5ulE_-Kk"
genai.configure(api_key=google_api_key)

def print_project_name():
    project_name = pyfiglet.figlet_format("Dorme nene'm ")
    print(project_name)

def select_age_range():
    print("\n\nHora de escolher a faixa etária do seu pequeno!")
    print("1. 😊 2-4 anos")
    print("2. 😁 5-7 anos")
    print("3. 😉 8-10 anos")
    print("4. 😎 11-14 anos")
    while True:
        choice = input("\nDigite o número correspondente à faixa etária: ")
        if choice in ["1", "2", "3", "4"]:
            return choice
        else:
            print("\nOpção inválida. Por favor, escolha novamente.")

def select_story_size():
    print("\n\nHora de escolher o tamanho da história!")
    print("1. 😊 Pequena (8 parágrafos)")
    print("2. 😁 Média (16 parágrafos)")
    print("3. 😉 Grande (20 parágrafos)")
    while True:
        choice = input("\nDigite o número correspondente ao tamanho da história: ")
        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("\nOpção inválida. Por favor, escolha novamente.")

def generate_feedback(age_range):
    feedback_messages = {
        "1": ["Consultando as estrelas...", "Gerando história...", "Desenhando personagens mágicos..."],
        "2": ["Procurando nos arquivos...", "Misturando cores e aventuras...", "História saindo do forno!"],
        "3": ["Conectando com a imaginação...", "Transformando ideias em palavras...", "História épica a caminho!"],
        "4": ["Explorando os confins do universo...", "Construindo mundos fantásticos...", "História pronta para surpreender!"]
    }

    messages = feedback_messages[age_range]
    for message in messages:
        print("\n\n" + message)
        time.sleep(1)

def generate_story(age_range, story_size):
    model_config = {
        "candidate_count": 1,
        "temperature": 0.7
    }

    age_ranges = {
        "1": "2 a 4 anos",
        "2": "5 a 7 anos",
        "3": "8 a 10 anos",
        "4": "11 a 14 anos"
    }

    story_sizes = {
        "1": "pequena, de 8 parágrafos",
        "2": "média, de 16 parágrafos",
        "3": "grande, de 20 parágrafos"
    }

    system_prompt = f"\n\nDorme neném é você.\n\nVocê é uma IA que cria histórias infantis para que os pais possam acessar ao enfrentarem dificuldades em colocar os pequenos para dormir. Use palavras cativantes, contextos criativos, aventuras, cores, dê vida à história que vai criar. Crie sempre uma nova e faça questão de usar expressões que entretenham os pequerruchos. Você deve gerar uma história {story_sizes[story_size]}, e cuidado com o que vai fornecer! Você está lidando com um público de {age_ranges[age_range]}, então faça as adaptações necessárias. Gere um título para a história e o retorne no topo, com espaço de 2 linhas entre ele e a história. Marque-o como 'Título:' e coloque-o em negrito"

    model = genai.GenerativeModel(model_name="gemini-1.0-pro", generation_config=model_config)

    chat = model.start_chat(history=[])
    prompt = system_prompt

    response = chat.send_message(prompt)
    print("\n\nHora da história!\n\n\n")
    print(response.text)


def main():
    print_project_name()
    while True:
        age_range = select_age_range()
        story_size = select_story_size()
        generate_feedback(age_range)
        generate_story(age_range, story_size)

        choice = input("\n\nDeseja gerar outra história? (S/N): ")
        if choice.upper() != "S":
            break

if __name__ == "__main__":
    main()
