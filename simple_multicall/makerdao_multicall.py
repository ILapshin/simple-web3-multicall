MAKERDAO_MULTICALL_ABI = '[{"constant":true,"inputs":[],"name":"getCurrentBlockTimestamp","outputs":[{"name":"timestamp","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"components":[{"name":"target","type":"address"},{"name":"callData","type":"bytes"}],"name":"calls","type":"tuple[]"}],"name":"aggregate","outputs":[{"name":"blockNumber","type":"uint256"},{"name":"returnData","type":"bytes[]"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getLastBlockHash","outputs":[{"name":"blockHash","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"addr","type":"address"}],"name":"getEthBalance","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getCurrentBlockDifficulty","outputs":[{"name":"difficulty","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getCurrentBlockGasLimit","outputs":[{"name":"gaslimit","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getCurrentBlockCoinbase","outputs":[{"name":"coinbase","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"blockNumber","type":"uint256"}],"name":"getBlockHash","outputs":[{"name":"blockHash","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"}]'

MAKERDAO_MULTICALL_ADDRESS = {
    'mainnet': '0xeefba1e63905ef1d7acba5a8513c70307c1ce441',
    'kovan': '0x2cc8688c5f75e365aaeeb4ea8d6a480405a48d2a',
    'rinkeby': '0x42ad527de7d4e9d9d011ac45b31d8551f8fe9821',
    'goerli': '0x77dca2c955b15e9de4dbbcf1246b4b85b651e50e',
    'ropsten': '0x53c43764255c17bd724f74c4ef150724ac50a3ed',
    'xdai': '0xb5b692a88bdfc81ca69dcb1d924f59f0413a602a',
    'polygon': '0x11ce4B23bD875D7F5C6a31084f55fDe1e9A87507',
    'mumbai': '0x08411ADd0b5AA8ee47563b146743C13b3556c9Cc',
    'bsc-mainnet': '0x41263cba59eb80dc200f3e2544eda4ed6a90e76c',
    'bsc-testnet': '0xae11C5B5f29A6a25e955F0CB8ddCc416f522AF5C'
}