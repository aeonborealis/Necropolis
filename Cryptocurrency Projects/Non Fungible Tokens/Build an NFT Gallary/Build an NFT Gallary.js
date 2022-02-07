import { LoaderFunction, useLoaderData } from "remix";

export const loader: LoaderFunction = async () => {
  const wallet = "DcTmx4VLcf5euAB17nynax7g55xuB3XKBDyz1pudMcjW";
  const body = {
    method: "qn_fetchNFTs",
    params: [wallet, []],
  };
  const options = {
    method: "POST",
    body: JSON.stringify(body),
  };

  const res = await fetch(
    "<YOUR_QUICKNODE_URL_HERE>",
    options
  );
  return res;
};

export default function NFT() {
  const data = useLoaderData();
  return (
    <div className="p-4">
      <h1>gm! {data.result.owner} Here are your NFTs</h1>
      <ul>
        {data.result.assets.map((nft: any) => (
          <li key={nft.tokenAddress}>
            <div className="max-w-sm  m-2 rounded overflow-hidden shadow-lg">
              <img
                className="w-full"
                src={nft.imageUrl}
                alt={nft.description}
              />
              <div className="px-6 py-4">
                <div className="font-bold text-xl mb-2">{nft.name}</div>
                <p className="text-gray-700 text-base">{nft.description}</p>
              </div>
              <div className="px-6 pt-4 pb-2">
                {nft.traits.map((trait: any) => (
                  <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">
                    {trait["trait_type"]}: {trait.value}
                  </span>
                ))}
              </div>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}