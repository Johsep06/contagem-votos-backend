import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv(override=True)

# Configurações do banco de dados
DB_CONFIG = {
    'credential': os.getenv('DB_CREDENTIALS'),
    'sheet': os.getenv('DB_SHEET'),
}

# Define o escopo de acesso à API do Google Sheets
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

# Carrega as credenciais do arquivo JSON
creds = ServiceAccountCredentials.from_json_keyfile_name(DB_CONFIG['credential'], scope)

# Autentica o cliente
client = gspread.authorize(creds)

# Abre a planilha pelo nome
spreadsheet = client.open(DB_CONFIG['sheet'])

# Acessa a primeira aba da planilha
sheet = spreadsheet.sheet1

# Lê todos os valores da planilha
dados = sheet.get_all_records()

# Mostra os dados
for linha in dados:
    print(linha)
