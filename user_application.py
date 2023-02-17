from typing import Any, TypeAlias

from wallet import Wallet

NodeConnection: TypeAlias = Any
UserSettings: TypeAlias = dict[str, Any]


class UserApplication:
    '''A class that allows users to run an application
    that will maintain a digital wallet with certain settings and database.'''

    def __init__(self) -> None:
        self.wallet: Wallet
        self.connection: NodeConnection
        self.user_settings: UserSettings

    def start_app(self) -> None:
        '''Starts the processes of all necessary modules of the user application.'''

    def start_networking(self) -> None:
        '''Start the module to interact with a trusted network node.'''

    def update_configuration(self) -> None:
        '''Update the application settings at the initiative of the user.'''

    def stop_app(self) -> None:
        '''Terminate the execution of all processes and modules of the user's application.
        Write every necessary data to disk'''
