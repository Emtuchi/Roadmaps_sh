const fs = require("fs");

function writeFile(path, data) {
  fs.writeFileSync(path, JSON.stringify(data, null, 2));
}

function readFile(path) {
  if (!fs.existsSync(path)) {
    fs.writeFileSync(path, JSON.stringify([]));
  }

  return JSON.parse(fs.readFileSync(path, "utf-8"));
}

module.exports = { readFile, writeFile };