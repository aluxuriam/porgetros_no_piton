from supabase import create_client

SUPABASE_URL = "https://brtnpqaouwvorgafoeou.supabase.co"

SUPABASE_KEY = "sb_publishable_2Kmn9iU3VOePFGLi6QvcPA_QDa1D7ab"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

print("Cliente Supabase criado com sucesso!")

from getpass import getpass

try:
    email =  input("Digite seu email: ")
    password = getpass("Digite Sua senha: ")
    resposta = supabase.auth.sign_in_with_password({"email": email, "password": password})
    print("Login realizado com sucesso!")
except KeyboardInterrupt:
    print("\nOperação cancelada pelo usuário.")
except Exception as erro:
    print(f"Erro ao fazer login: {erro}")