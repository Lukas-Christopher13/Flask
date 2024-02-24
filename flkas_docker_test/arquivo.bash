# Criar o arquivo .gitignore
echo -e ".venv/\n__pycache__/" > .gitignore
echo "Arquivo .gitignore criado com sucesso."

pip freeze > requirements.txt
echo "Arquivo requirements.txt criado com sucesso."

git init 

git add .

git commit -m "Commit inicial - Arquivo .gitignore e requirements.txt"