"""NAME
    Multicall

DESCRIPTION
    A multicall for use with pure Web3 lbrary.
    It uses MakerDao Multicall smart contract by default,
    but also can use any custom multicall smart contract 
    that implements "aggregate" function

"""

from web3 import Web3
from web3.eth import Contract

from .makerdao_multicall import (
    MAKERDAO_MULTICALL_ABI, 
    MAKERDAO_MULTICALL_ADDRESS
)


class Multicall:
    """
    NAME
        Multicall
    
    DESCRIPTION
       The main multicall class.
    
    ATTRIBUTES
        w3 : Web3 class instanse

        chain: str
            The name of one of defined chains 
            where MakerDao Multicall smart contract is deployed.
            Can be one of the followings:
            - 'mainnet'
            - 'kovan'
            - 'rinkeby'
            - 'goerli'
            - 'ropsten'
            - 'xdai'
            - 'polygon'
            - 'mumbai'
            - 'bsc-mainnet'
            - 'bsc-testnet'

        custom_address: str
            An address of custom multicall smart contract. 
            If specified, MakerDao Multicall smart contract will be omited.

        custom_abi: str
            An ABI of custom multicall smart contract.
            If omited, MakerDao Multicall smart contract ABI will be used.

    """

    def __init__(
        self,
        w3: Web3,
        chain='mainnet',
        custom_address=None,
        custom_abi=None
    ):
        if custom_address:
            address = Web3.toChecksumAddress(custom_address)
        else:
            try:
                address = Web3.toChecksumAddress(MAKERDAO_MULTICALL_ADDRESS[chain])  
            except(Exception):
                print('Chain name key not in default dictionary')
                return  

        abi=MAKERDAO_MULTICALL_ABI        

        if custom_abi:
            abi = custom_abi

        self.multicall = w3.eth.contract(
            address=address,
            abi=abi
        )


    def call(
        self,
        calls: list
    ) -> list:
        """
        Executes multicall for specified list of smart contracts functions.

        Parameters:
            calls: list(tuple)
                list of tuples (target contract address, encoded function name with parameters)
                Can be easy prepared via using Multicall.create_cal' method.

        Returns:
            tuple(block number, list(results)) for default MakerDao multicall. May vary for custom multicalls.
        """
        
        return self.multicall.functions.aggregate(calls).call()


    def create_call(
        self,
        contract: Contract,
        fn_name: str,
        args: list
    ) -> tuple:
        """
        Prepares a tuple for passing to Multicall.call list.

        Parameters:
            contract: Web3.eth.Contract
                A Web3.eth.Contract instance of a contract 
                that is to be called via multicall.

            fn_name: str
                The name of a contract function to be called.

            args: list
                a list of arguments to be passed to a called contract function.

        Returns:
            tuple(target contract address, encoded function name with parameters)

        """

        return (contract.address, contract.encodeABI(fn_name=fn_name, args=args))
        