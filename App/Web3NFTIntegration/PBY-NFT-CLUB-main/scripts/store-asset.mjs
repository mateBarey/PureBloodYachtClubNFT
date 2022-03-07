import { NFTStorage, File } from "nft.storage"
import fs from 'fs'
import dotenv from 'dotenv'
dotenv.config()

const API_KEY = process.env.NFT_STORAGE_API_KEY

async function storeAsset() {
   const client = new NFTStorage({ token:"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweDZhNzA1OWU4M2U2YWUxQkY2MzIyNDIyZDM0QTE0QzNjOTM2ODlkY0IiLCJpc3MiOiJuZnQtc3RvcmFnZSIsImlhdCI6MTY0NjQ3MTM1ODcxMCwibmFtZSI6IlBvbHlnb24gKyBORlQuU3RvcmFnZSJ9.pOB7j5kDF48iYGbyovC7Nf-nm-TomXT2jG3cmzuyVwM"})
   const metadata = await client.store({
       name: 'nft.png',
       description: 'My ExampleNFT is an awesome artwork!',
       image: new File(
           [await fs.promises.readFile('assets/nft.png')],
           'nft.png',
           { type: 'image/png' }
       ),
   })
   console.log("Metadata stored on Filecoin and IPFS with URL:", metadata.url)
}

storeAsset()
   .then(() => process.exit(0))
   .catch((error) => {
       console.error(error);
       process.exit(1);
   });