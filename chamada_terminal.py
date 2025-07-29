
import requests

def main():
    checkin = input("Digite a data de check-in (YYYY-MM-DD): ").strip()
    checkout = input("Digite a data de check-out (YYYY-MM-DD): ").strip()
    adultos = input("Número de adultos: ").strip()
    criancas = input("Número de crianças: ").strip()

    url = f"https://SEU_ENDPOINT_PUBLICO/executar?checkin={checkin}&checkout={checkout}&hospedes={adultos}&criancas={criancas}"

    print(f"Chamando: {url}")
    try:
        response = requests.get(url)
        print("Resposta da API:")
        print(response.text)
    except Exception as e:
        print(f"Erro ao chamar a API: {e}")

if __name__ == "__main__":
    main()
