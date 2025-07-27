def send_activation_email(email: str, token: str):
    print(f"[DEBUG] Email sending on {email}: http://localhost:8000/api/v1/auth/activate?token={token}")
