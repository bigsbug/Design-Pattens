from notification_interface import StrategyInterface


class MessageInSite(StrategyInterface):
    def notify(self, reqeust, message, toAll) -> bool:
        print(
            "Notification [{message}] to [{request.user}] via Messages in site sended."
        )


class Email(StrategyInterface):
    def notify(self, reqeust, message, toAll) -> bool:
        print("Notification [{message}] to [{request.user}] via Email sended.")


class Websocket(StrategyInterface):
    def notify(self, reqeust, message, toAll) -> bool:
        print("Notification [{message}] to [{request.user}] via Web Socket sended.")


class SMS(StrategyInterface):
    def notify(self, reqeust, message, toAll) -> bool:
        print("Notification [{message}] to [{request.user}] via SMS sended.")
