import { useState } from "react";
import { sendPrompt } from "../api/nodeaiApi";
import ChatMessage from "./ChatMessage";
import CommandChip from "./CommandChip";
import ChatLoader from "./ChatLoader";

function ChatWindow({ isOpen, onClose }) {
  const [messages, setMessages] = useState([
    {
      sender: "bot",
      text: "Hi, I am NodeAI. Give me a device command.",
    },
  ]);

  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSend = async (customPrompt) => {
    const prompt = customPrompt || input;

    if (!prompt.trim()) return;

    setMessages((prev) => [...prev, { sender: "user", text: prompt }]);
    setInput("");
    setLoading(true);

    try {
      const response = await sendPrompt(prompt);

      setMessages((prev) => [
        ...prev,
        {
          sender: "bot",
          text: response.data,
        },
      ]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          sender: "bot",
          text: "API error. Please check FastAPI server.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <div
        className={`chat-overlay ${isOpen ? "show" : ""}`}
        onClick={onClose}
      />

      <aside className={`chat-drawer ${isOpen ? "open" : ""}`}>
        <div className="chat-header">
          <div>
            <h3>NodeAI Assistant</h3>
            <p>AI-powered device control</p>
          </div>

          <button onClick={onClose}>×</button>
        </div>

        <div className="chat-body">
          {messages.map((msg, index) => (
            <ChatMessage key={index} sender={msg.sender} text={msg.text} />
          ))}

          {loading && <ChatLoader />}
        </div>

        <div className="chips">
          <CommandChip text="Turn off the lights" onClick={handleSend} />
          <CommandChip text="Set RGB to blue" onClick={handleSend} />
          <CommandChip text="What is the temperature?" onClick={handleSend} />
          <CommandChip text="Show humidity" onClick={handleSend} />
          <CommandChip text="Check signal strength" onClick={handleSend} />
        </div>

        <div className="chat-input">
          <input
            value={input}
            placeholder="Ask NodeAI to control your device..."
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleSend()}
            disabled={loading}
          />

          <button onClick={() => handleSend()} disabled={loading}>
            Send
          </button>
        </div>
      </aside>
    </>
  );
}

export default ChatWindow;