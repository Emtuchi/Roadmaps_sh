const { capitalize } = require ("../utils/capitalize.js");

function getEventMessage(event) {
  switch (event.type) {
    case "PushEvent":
      return `Pushed ${event.payload.commits?.length || 0} commits`;

    case "IssuesEvent":
      return `${capitalize(event.payload.action)} an issue`;

    case "WatchEvent":
      return "Starred repository";

    case "ForkEvent":
      return "Forked repository";

    case "CreateEvent":
      return `Created ${event.payload.ref_type}`;

    default:
      return null;
  }
}

module.exports = { getEventMessage };