const CONTRACT_ADDRESS = "0x7A2D0334B551810d1Cf9B6d3Ca25664Fd5c01A2F"
const META_DATA_URL = "ipfs://bafyreic3kbtrec7odlmvfngroizqtikuk6amxko25vdk5j6k62f5j67lca/metadata.json"

async function mintNFT(contractAddress, metaDataURL) {
   const PBYnft = await ethers.getContractFactory("PBYnft")
   const [owner] = await ethers.getSigners()
   await PBYnft.attach(contractAddress).mintNFT(owner.address, metaDataURL)
   console.log("NFT minted to: ", owner.address)
}

mintNFT(CONTRACT_ADDRESS, META_DATA_URL)
   .then(() => process.exit(0))
   .catch((error) => {
       console.error(error);
       process.exit(1);
   });