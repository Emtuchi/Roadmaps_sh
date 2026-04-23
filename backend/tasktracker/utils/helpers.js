let currentId = 0;

function generateId() {
  currentId += 1;
  return currentId;
}

function now() {
  return new Date().toISOString();
}

module.exports = { generateId, now };