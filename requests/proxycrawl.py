from requests import Session
import random


def new_proxycrawl_token(gettt_uid, base_gmail_email, password):
    session = Session()

    def get_last_code(uuid):
        try:
            return session.get(f'https://gettt.viti.site/get?t={GETTT_UID}&q=Proxycrawl').json()[0]['text/html'].split('https://proxycrawl.com/users/')[1].split('/')[0]
        except Exception:
            return None

    new_email = f'{base_gmail_email}{random.randint(0, 99999)}@gmail.com'
    sign_up_data = {
        'email': new_email,
        'password': password,
        'password-confirm': password,
        'volume': '< 1000'
    }

    current_last_code = get_last_code(GETTT_UID)

    session.post('https://proxycrawl.com/signup', data=sign_up_data)

    for x in range(0, 100):
        if x == 99:
            return new_proxycrawl_token(gettt_uid, base_gmail_email, password)
        code_now = get_last_code(GETTT_UID)
        if code_now != current_last_code:
            break

    assert session.get(f'https://proxycrawl.com/users/{code_now}/confirm-email').status_code == 200

    session.post('https://proxycrawl.com/login', data={
        'email': new_email,
        'password': password
    })
    api_token = session.get('https://proxycrawl.com/dashboard/account').text.split('token-input')[1].split('value=')[1].split('"')[1]
    return api_token
