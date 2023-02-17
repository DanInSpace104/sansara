from typing import Any, TypeAlias

from blockchain import Blockchain

# just some mock ups of future classes
NetworkConnection: TypeAlias = Any
NetworkId: TypeAlias = int
NodeAddress: TypeAlias = Any


class Node:
    '''A class that allows to maintain one node (even centralized option)
    that will process blockchain, has network interfaces and runs with certain settings.
    '''

    def __init__(self) -> None:
        self.blockchain: Blockchain
        self.connections: list[NetworkConnection]
        self.settings: dict[str, Any]

    def start_node(self, net_id: NetworkId) -> None:
        '''Start the processes of all required modules of the full network node.
        For example, the networking module, blockchain processing module,
        module of interaction with the user / node administrator.
        '''

    def start_networking(self, trusted_node: NodeAddress) -> None:
        '''Start a network module and interact with other network nodes.'''

    def stop_node(self) -> None:
        '''Terminate the execution of all processes and modules of the current node.
        Write every necessary data to disk.'''

    def update_configuration(
        self, new_conf: dict[str, Any] | None = None, **kwargs: dict[str, Any]
    ) -> None:
        if new_conf is not None:
            self.settings.update(new_conf)
        self.settings.update(kwargs)
