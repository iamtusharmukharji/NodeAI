function ChatMessage({ sender, text }) {
  const header = sender === "error" ? "Oops!" : null;

  return (
    <div className={`message ${sender}`}>
      {header && (
        <>
          <strong>{header}</strong>
          <br />
        </>
      )}
      {text}
    </div>
  );
}

export default ChatMessage;