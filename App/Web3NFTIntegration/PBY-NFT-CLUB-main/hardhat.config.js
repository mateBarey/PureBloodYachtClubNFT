/**
* @type import('hardhat/config').HardhatUserConfig
*/
require("@nomiclabs/hardhat-ethers");
require('dotenv').config();
const { PRIVATE_KEY } = process.env;
module.exports = {
  defaultNetwork: "polygon_mumbai",
  networks: {
    hardhat: {
    },
     polygon_mumbai: {
      url: "https://rpc-mumbai.maticvigil.com",
      accounts: ["55af77961b3a161d1451e42e8246f5ddd400eea51831e043074bb54bffb3b76c"]
    }
  },
  solidity: {
    version: "0.8.12",
    settings: {
      optimizer: {
        enabled: true,
        runs: 200
      }
    }
  },
}