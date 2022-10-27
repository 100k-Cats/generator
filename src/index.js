import fs from 'fs';
import { exec } from 'child_process';
import util from 'util';

const execPromise = util.promisify(exec);
let range = [0, 2];
const list = ['Background', 'Digits', 'Rear', 'Body', 'Clothing', '.eth', 'Eyewear', 'Hat', 'Crown', 'Mouth', 'Foreground']

for (var subdomain = range[0]; subdomain < range[1] + 1; subdomain++) {
  let subdomain_ = String(subdomain).padStart(5, '0');
  let command = `bash ./src/generator.sh ${subdomain_}`;
  try {
    const {stdout, stderr} = await execPromise(command);
    console.log(`CID/PNG ${subdomain_} (${subdomain_}.png): ` + `${stdout.split('+')[0]}`);
    let attr = stdout.split('+')[1].replace(/(\r\n|\n|\r)/gm, "").split('=');
    var attributes = [];
    for (var i=0; i < attr.length; i++) {
      if (attr[i] != '-') {
        attributes.push(
          {
            "trait_type": `${list[i]}`,
            "value": `${attr[i]}`
          }
        )
      }
    }
    const content = {
      "name": `${subdomain_}.100kCat.eth`,
      "description": `100k Cats for 100k ENS Club`,
      "external_url": `https://100kCat.eth.limo`,
      "image": `ipfs://${stdout.split('+')[0]}`,
      "attributes": attributes
    };
    fs.writeFile(`./dist/json/${subdomain_}.json`, JSON.stringify(content, null, 4), err => {
      if (err) {
        console.error(err);
      }
    });
  } catch (error) {
    console.log(error);
  }
}

// add contractURI
const contractURI = {
  "name": "100k ENS Cats",
  "description": "100k Cats for 100k ENS Club",
  "image": `ipfs://<avatar>`,
  "external_link": "https://100kCat.eth.limo",
  "seller_fee_basis_points": 750,
  "fee_recipient": "0xblablabla..."
};
fs.writeFile(`./dist/json/contractURI.json`, JSON.stringify(contractURI, null, 4), err => {
  if (err) {
    console.error(err);
  }
});

/*
// Pin PNG to IPFS
console.log('Pinning PNG to IPFS ...');
let commandPng = `ipfs add -n -r ./dist/png`;
const {stdoutPng, stderrPng} = await execPromise(commandPng);
let repoPng = stdoutPng.split('\n')[stdoutPng.split('\n').length - 2].split(' ')[1]
console.log('PNG Repo CID: ' + repoPng);

// Pin JSON to IPFS
console.log('Pinning JSON to IPFS ...');
let commandJson = `ipfs add -n -r ./dist/json`;
const {stdoutJson, stderrJson} = await execPromise(commandJson);
let repoJson = stdoutJson.split('\n')[stdoutJson.split('\n').length - 2].split(' ')[1]
console.log('JSON Repo CID: ' + repoJson);
*/
