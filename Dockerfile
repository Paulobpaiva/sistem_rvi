# Use uma imagem oficial do Python
FROM python:3.12-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de dependências
COPY requirements.txt .

# Instala as dependências
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia o restante do projeto
COPY . .

# Coleta arquivos estáticos
RUN python manage.py collectstatic --noinput

# Expõe a porta padrão do Django/WSGI
EXPOSE 8000

# Comando para rodar o servidor WSGI (gunicorn)
CMD ["gunicorn", "sistema_estacionamento.wsgi:application", "--bind", "0.0.0.0:8000"] 