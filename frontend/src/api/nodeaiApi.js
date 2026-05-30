const BASE_URL = "http://127.0.0.1:8000"

export async function sendPrompt(prompt) {
  const response = await fetch(
    `${BASE_URL}/device/prompt?prompt=${encodeURIComponent(prompt)}`,
    {
      method: "POST",
    }
  );

  return await response.json();
}