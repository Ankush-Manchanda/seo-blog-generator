from medium import Client

def post_to_medium(title, content):
    client = Client(application_id="YOUR_APP_ID", application_secret="YOUR_SECRET")
    client.exchange_authorization_code("AUTH_CODE", "REDIRECT_URI")
    
    user = client.get_current_user()
    post = client.create_post(
        user_id=user["id"],
        title=title,
        content_format="html",
        content=content,
        publish_status="public"
    )
    return post['url']
