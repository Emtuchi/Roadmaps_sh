const BASE_URL = "https://api.github.com";

async function fetchEvents(username) {
  const url = `${BASE_URL}/users/${username}/events`;

  try {
    const res = await fetch(url);

    if (res.status === 404) {
      console.log("User not found");
      return null;
    }

    if (!res.ok) {
      console.log("API error:", res.status);
      return null;
    }

    return await res.json();
  } catch (err) {
    console.log("Network error:", err.message);
    return null;
  }
}

module.exports = { fetchEvents };