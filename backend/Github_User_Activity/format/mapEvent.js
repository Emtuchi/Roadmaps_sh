const { getEventMessage } = require ("./getEventMessage.js");

function mapEvent(event) {
  const message = getEventMessage(event);

  if (!message) return null;

  return `${message} in ${event.repo.name}`;
}

module.exports = { mapEvent };