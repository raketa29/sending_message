from twilio.rest import Client
from auth.config import Account_SID, auth_TOKEN, phone_number


def sending_sms(text: str, receiver: str):
    try:
        client = Client(Account_SID, auth_TOKEN)
        message = client.messages.create(
            messaging_service_sid='MG6fb4cb8e18e36645958efafbdec3f43f',
            body=text,
            # from_=phone_number,
            to=receiver
            # +48787180128  Добрый день! Вы выиграли 1000 грн. Укажите куда вам перечислить деньги. GO XBET.
        )
    except Exception as ex:
        print("sorry..", ex)


def main():
    receiver = input("input phone number:  ").strip()
    text = input("input text message:  ").strip().title()
    sending_sms(text, receiver)


if __name__ == '__main__':
    main()
