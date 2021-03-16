import React, { useState } from "react";
import ReactDOM from "react-dom";
import ReactTooltip from "react-tooltip";

import MapChart from "./MapChart";

function App() {
  const [content, setContent] = useState("");
  const [selected, setSelected] = useState("Click a country");
  return (
    <div>
      <div className="base">
        <h1>Framework</h1>
        {selected !== "Click a country" ? (
          <button onClick={() => setSelected("Click a country")}>Clear selection</button>
        ) : (
          <h4>{selected}</h4>
        )}
      </div>
      <div className="map">
        <MapChart selected={selected} setSelected={setSelected} setTooltipContent={setContent} />
        <ReactTooltip>{content}</ReactTooltip>
      </div>
    </div>
  );
}

export default App;