# OCEAN Data NFTs

[![GitHub Codespaces Ready](https://img.shields.io/badge/GitHub%20Codespaces-Ready-green)](https://github.com/features/codespaces)

Quickly create [OCEAN](https://oceanprotocol.com/) Data NFTs by querying blockchain data from different providers ([Dune](https://dune.com/) & [Flipside](https://flipsidecrypto.xyz/)).

### Setup
* Create a GitHub Codespaces workspace.
* Use Python 3.8.
* `pip install -r requirements.txt`
* Create an `.env` file with the following keys:
    * `DUNE_API_KEY`
    * `FLIPSIDE_API_KEY`
    * `WEB3_INFURA_PROJECT_ID` (Note: Must have an Infrura account w/ RPC endpoints.)
    * `PRIVATE_KEY` (For a wallet)
* Run `Create_OCEAN_Data_NFT.ipynb`