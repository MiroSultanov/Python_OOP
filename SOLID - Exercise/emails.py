# You are provided with code containing class IEmail and class Email. The code does not follow the principle of single 
# responsibility (the Email class has 2 responsibilities). Create a new class - IContent, and a class that inherits it called MyContent to split the responsibilities.

from abc import ABCMeta, abstractmethod, ABC


class IEmail(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class IContent(ABC):

    @property
    @abstractmethod
    def content(self):
        pass

    @content.setter
    @abstractmethod
    def content(self, content):
        pass


class Email(IEmail):

    def __init__(self, protocol, content_type: IContent):
        self.protocol = protocol
        self.content_type = content_type
        self.__sender = None
        self.__receiver = None

    def set_sender(self, sender):
        if self.protocol == 'IM':
            self.__sender = ''.join(["I'm ", sender])
        else:
            self.__sender = sender

    def set_receiver(self, receiver):
        if self.protocol == 'IM':
            self.__receiver = ''.join(["I'm ", receiver])
        else:
            self.__receiver = receiver

    def set_content(self, content):
        self.content_type.content = content

    def __repr__(self):

        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender=self.__sender, receiver=self.__receiver, content=self.content_type.content)


class MyContent(IContent):

    def __init__(self, content_type):
        self.content_type = content_type
        self.__content = None

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content):
        if self.content_type == 'MyML':
            self.__content = '\n'.join(['<myML>', content, '</myML>'])
        else:
            self.__content = content


if __name__ == '__main__':
    email = Email('IM', MyContent('MyML'))
    email.set_sender('qmal')
    email.set_receiver('james')
    email.set_content('Hello, there!')
    print(email)
