function CommandChip({ text, onClick }) {
  return (
    <button className="command-chip" onClick={() => onClick(text)}>
      {text}
    </button>
  );
}

export default CommandChip;