import fs from 'fs';
import { exec } from 'child_process';
import util from 'util';

const execPromise = util.promisify(exec);
let range = [1, 16180, 7];
// let range = [...Array(1000).keys()];

for (var index = 0; index < range.length; index++) {
  let subdomain = range[index];
  let subdomain_ = String(subdomain).padStart(5, '0');
  let command = `bash ./src/generator.sh ${subdomain_}`;
  try {
    const {stdout, stderr} = await execPromise(command);
    console.log(`CID/PNG ${subdomain_} (${subdomain_}.png): ` + `${stdout.split('+')[0]}`);
    let attr = stdout.split('+')[1].replace(/(\r\n|\n|\r)/gm, "").split('=');
    let prop = stdout.split('+')[2].replace(/(\r\n|\n|\r)/gm, "").split('=');
    let list = stdout.split('+')[3].replace(/(\r\n|\n|\r)/gm, "").split('=');
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
    for (var i=0; i < prop.length; i++) {
      if (prop[i] != '-') {
        attributes.push(
          {
            "value": `${prop[i]}`
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
  "image": `ipfs://QmRbp24r7E3e39S8AicNri6Euq5gdeHVb9fDsepZbwUCiV`,
  "external_link": "https://100kCat.eth.limo",
  "seller_fee_basis_points": 750,
  "fee_recipient": "0xD62fB2a45ECdCF23f8587acC92119d4705d25Bb5"
};
fs.writeFile(`./dist/contractURI.json`, JSON.stringify(contractURI, null, 4), err => {
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
