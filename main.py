
import requests
import openpyxl
import sys

def main():
    if len(sys.argv) != 5:
        print("Uso correto:")
        print("python main.py <checkin> <checkout> <adultos> <criancas>")
        sys.exit(1)

    checkin = sys.argv[1]
    checkout = sys.argv[2]
    adultos = sys.argv[3]
    criancas = sys.argv[4]

    with open("ids.txt") as f:
        ids = [line.strip() for line in f if line.strip()]

    # Criar planilha
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Resultados"
    sheet.append(["ID Propriedade", "Nome Propriedade", "Valor", "Link Airbnb", "Link API"])

    for pid in ids:
        airbnb_url = (
            f"https://www.airbnb.com.br/rooms/{pid}"
            f"?check_in={checkin}&check_out={checkout}"
            f"&adults={adultos}&children={criancas}&infants=0&pets=0&source_impression_id=cli_app"
        )

        api_url = (
            f"https://comparativo-production.up.railway.app/executar"
            f"?checkin={checkin}&checkout={checkout}&hospedes={adultos}&criancas={criancas}&id={pid}"
        )

        print("=" * 60)
        print(f"➡️  Verificando propriedade: {pid}")
        print(f"🔗 Link Airbnb: {airbnb_url}")
        print(f"📡 Chamando API: {api_url}")

        try:
            response = requests.get(api_url)
            data = response.json()

            nome = data.get("nome", "N/A")
            valor = data.get("valor", "N/A")
            print(f"✅ Nome: {nome}")
            print(f"💲 Valor: {valor}")

            sheet.append([pid, nome, valor, airbnb_url, api_url])
        except Exception as e:
            print(f"❌ Erro ao consultar {pid}: {e}")

    # Salvar planilha
    workbook.save("resultado_busca.xlsx")
    print("\n📄 Arquivo 'resultado_busca.xlsx' gerado com sucesso!")

if __name__ == "__main__":
    main()
