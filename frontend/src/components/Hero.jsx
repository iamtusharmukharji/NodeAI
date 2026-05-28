function Hero({ onTryClick }) {
  return (
    <section className="hero">
      <div className="hero-content">
        <div className="badge">GenAI + IoT Automation</div>

        <h1>
          Control real devices with <span>NodeAI</span>
        </h1>

        <p>
          A smart IoT automation system where natural language commands are
          understood by AI and executed on real NodeMCU hardware using MQTT.
        </p>

        <div className="hero-actions">
          <button onClick={onTryClick}>Try NodeAI</button>
          <a href="#features">View Architecture</a>
        </div>

        <div className="hero-stats">
          <div>
            <strong>5</strong>
            <span>Relays</span>
          </div>
          <div>
            <strong>RGB</strong>
            <span>LED Control</span>
          </div>
          <div>
            <strong>DHT11</strong>
            <span>Sensor</span>
          </div>
        </div>
      </div>

      <div className="hero-panel">
        <div className="panel-card active">
          <span>Command</span>
          <p>Turn off the lights</p>
        </div>

        <div className="panel-card">
          <span>NodeAI Response</span>
          <p>Turning off the lights. Signal quality is -50 RSSI.</p>
        </div>

        <div className="device-grid">
          <div>Relay 1</div>
          <div>Relay 2</div>
          <div>RGB LED</div>
          <div>DHT11</div>
        </div>
      </div>
    </section>
  );
}

export default Hero;