const { mapEvent } = require ("./mapEvent.js");

function formatEvents(events) {
  return events
    .map(mapEvent)
    .filter(Boolean)
    .slice(0, 10);
}

module.exports = { formatEvents };