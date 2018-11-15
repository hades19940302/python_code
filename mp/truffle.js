var PrivateKeyProvider = require("truffle-privatekey-provider");
 
var privateKey = "bcec428d5205abe0f0cc8a734083908d9eb8563e31f943d760786edf42ad67dd";
 
module.exports = {
  networks: {
    rinkeby: {
      provider: new PrivateKeyProvider(privateKey, "http://127.0.0.1:8545"),
      network_id: '*'
    },
    ....
  }
};