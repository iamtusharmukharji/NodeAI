import { useState } from "react";
import Hero from "../components/Hero";
import FeatureCard from "../components/FeatureCard";
import ChatButton from "../components/ChatButton";
import ChatWindow from "../components/ChatWindow";

function Home() {
  const [isChatOpen, setIsChatOpen] = useState(false);

  return (
    <div className="app">
      <Hero onTryClick={() => setIsChatOpen(true)} />

      <section className="features-section">
        <div className="section-heading">
          <span>NodeAI Capabilities</span>
          <h2>Control hardware using natural language</h2>
          <p>
            NodeAI connects Generative AI with real IoT hardware using FastAPI,
            Gemini, MQTT, and NodeMCU.
          </p>
        </div>

        <div className="features">
          <FeatureCard title="AI Command Engine" text="Converts human prompts into structured IoT actions." />
          <FeatureCard title="5 Relay Control" text="Switch real appliances like lights, fans, and devices." />
          <FeatureCard title="RGB LED Control" text="Set colors, blink lights, and control visual feedback." />
          <FeatureCard title="DHT11 Monitoring" text="Read temperature and humidity from the device." />
          <FeatureCard title="RSSI Monitoring" text="Track NodeMCU Wi-Fi signal strength in real time." />
          <FeatureCard title="MQTT Realtime" text="Low-latency communication between backend and hardware." />
        </div>
      </section>

      <section className="workflow-section">
        <h2>How NodeAI Works</h2>

        <div className="workflow">
          <div>User Prompt</div>
          <span>→</span>
          <div>React App</div>
          <span>→</span>
          <div>FastAPI</div>
          <span>→</span>
          <div>Gemini AI</div>
          <span>→</span>
          <div>MQTT</div>
          <span>→</span>
          <div>NodeMCU</div>
        </div>
      </section>

      <ChatButton onClick={() => setIsChatOpen(true)} />

      <ChatWindow
        isOpen={isChatOpen}
        onClose={() => setIsChatOpen(false)}
      />
    </div>
  );
}

export default Home;