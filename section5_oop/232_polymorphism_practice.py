"""
# Portuguese
- Python nao suporta sobrecarga de metodo. (Overload)
- Python suporta sobreposicao de metodo. (Override)

"""
from abc import ABC, abstractmethod


class Notification(ABC):
    def __init__(self, message) -> None:
        self.message = message

    # -> bool
    # This means that the method sent will return boolean value.
    # It is called TYPE ANNOTATION
    @abstractmethod
    def send(self) -> bool: ...


class EmailNotification(Notification):
    def send(self) -> bool:
        print(f'Sending e-mail: {self.message}')
        return True


class SMSNotification(Notification):
    def send(self) -> bool:
        print(f'Sending SMS: {self.message}')
        return False


def notify(notification: Notification):
    sent_notification = notification.send()
    if sent_notification:
        print('Notification Sent')
    else:
        print('Notification Not Sent')


notify(EmailNotification('Hello World Email'))
notify(SMSNotification('Hello World SMS'))
