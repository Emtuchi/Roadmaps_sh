function display(messages) {
  if (messages.length === 0) {
    console.log("No recent activity");
    return;
  }

  console.log("\nRecent GitHub Activity:\n");

  messages.forEach((msg) => {
    console.log(`- ${msg}`);
  });
}

module.exports = { display };