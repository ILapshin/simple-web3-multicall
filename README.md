# Simple Web3 Multicall

A multicall for use with pure Web3.py library.
It uses MakerDao Multicall smart contract by default,
but also can use any custom multicall smart contract 
that implements "aggregate" function.

Main urge for developmenet such a package was when I was needed to use multicall in my project 
based on Web3.py, but found only libraries which work with Brownie, not on pure Web3.py.


    pip install simple-multicall


## Package Content

- class Multicall - The main multicall class that executes a multicall itself.

- constants file makerdao_multicall - contains a default MakerDao multicall smart contract ABI and a dictionary of addresses of multicall contracts deployed on different chains. 


### class Multicall

The main multicall class. Should be initialized by passing a Web3 instance with specified chain RPC provider.

Has two methods: 

*call* - executes a multicall

*create_call* - prepare a tuple for a list of calls to be passed to a *call* method


**Attributes**
    
*w3* : Web3 class instanse

*chain*: str
The name of one of defined chains 
where MakerDao Multicall smart contract is deployed.
Can be one of the followings

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


*custom_address*: str - An address of custom multicall smart contract. 
If specified, MakerDao Multicall smart contract will be omited.


*custom_abi*: str - An ABI of custom multicall smart contract.
If omited, MakerDao Multicall smart contract ABI will be used.


**Methods**

*call()* - Executes multicall for specified list of smart contracts functions.

Parameters:

calls: list(tuple) - list of tuples (target contract address, encoded function name with parameters)
Can be easy prepared via using Multicall.create_cal' method.

Returns:

tuple(block number, list(results)) for default MakerDao multicall. May vary for custom multicalls.


*create_call()* - Prepares a tuple for passing to Multicall.call list.

Parameters:

contract: web3.eth.Contract - A web3.eth.Contract instance of a contract 
that is to be called via multicall.

fn_name: str - The name of a contract function to be called.

args: list - a list of arguments to be passed to a called contract function.

Returns:

tuple(target contract address, encoded function name with parameters)


## Example

Multicall of three ERC20 tokens of a specified EthDev *address*.

Importing Web3

    >>> from web3 import Web3

Defining constants: ERC20 token ABI token mainnet addresses.

    # ERC20 ABI string is cropped for readability
    >>> ERC20_ABI = '[{"constant":true,"inputs":[],"name":"name", ...

    >>> USDT_ADDRESS = Web3.toChecksumAddress('0xdAC17F958D2ee523a2206206994597C13D831ec7')
    >>> USDC_ADDRESS = Web3.toChecksumAddress('0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48')
    >>> BNB_ADDRESS = Web3.toChecksumAddress('0xB8c77482e45F1F44dE1745F52C74426C631bDD52')

Initializing web3 instance.

    >>> ETH_PROVIDER_URL = 'https://rpc.ankr.com/eth'
    >>> w3 = Web3(Web3.HTTPProvider(ETH_PROVIDER_URL))    
    
Creating token Web3 contracts.

    >>> USDT = w3.eth.contract(address=USDT_ADDRESS, abi=ERC20_ABI)
    >>> USDC = w3.eth.contract(address=USDC_ADDRESS, abi=ERC20_ABI)
    >>> BNB = w3.eth.contract(address=BNB_ADDRESS, abi=ERC20_ABI)
  
Target user address.

    >>> address = '0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe'

Initializing Multicall for mainnet.

    >>> from simple_multicall import Multicall
    >>> 
    >>> multicall = Multicall(w3, 'mainnet')

Creating a list of calls via 'Multicall.create_call()' method.

    >>> calls = [
    ...     multicall.create_call(USDT, 'balanceOf', [address]),
    ...     multicall.create_call(USDC, 'balanceOf', [address]),
    ...     multicall.create_call(BNB, 'balanceOf', [address])
    ... ]

Executing multicall.

    >>> result= multicall.call(calls)

    >>> result
    [15442332, [b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\    
    x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00?D#\xde' b'\x00\x00\x00\x00\x00\
    x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
    x00\x00\x00;\x9a\xf1\x10', b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0
    0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02HA>\xf1\xd3\xf2\x00\x00']]

Interpreting results.

    >>> print('Block number: ', result[0])
    Block number:  15442332

    >>> print('USDT: ', int(result[1][0].hex(), 16) / 10 ** 6)
    USDT:  1061.430238

    >>> print('USDC: ', int(result[1][1].hex(), 16) / 10 ** 6)
    USDC:  1000.01

    >>> print('BNB: ', int(result[1][2].hex(), 16) / 10 ** 18)
    BNB:  42.1
