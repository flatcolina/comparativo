
import requests
import openpyxl

def main():
    checkin = input("Digite a data de check-in (YYYY-MM-DD): ").strip()
    checkout = input("Digite a data de check-out (YYYY-MM-DD): ").strip()
    adultos = input("Número de adultos: ").strip()
    criancas = input("Número de crianças: ").strip()

    with open("ids.txt") as f:
        ids = [line.strip() for line in f if line.strip()]

    # Criar workbook
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Resultados"
    sheet.append(["ID Propriedade", "Nome Propriedade", "Valor"])

    for pid in ids:
        url = (
            f"https://comparativo-production.up.railway.app/executar"
            f"?checkin={checkin}&checkout={checkout}&hospedes={adultos}&criancas={criancas}&id={pid}"
        )
        print(f"➡️  Verificando propriedade {pid}")
        try:
            response = requests.get(url)
            data = response.json()

            nome = data.get("nome", "N/A")
            valor = data.get("valor", "N/A")
            print(f"✅ {nome} - {valor}")
            sheet.append([pid, nome, valor])
        except Exception as e:
            print(f"❌ Erro ao consultar {pid}: {e}")

    # Salvar XLSX
    workbook.save("resultado_busca.xlsx")
    print("Arquivo 'resultado_busca.xlsx' gerado com sucesso!")

if __name__ == "__main__":
    main()
