import React, { useState } from "react";
import ReactDOM from "react-dom";
import ReactTooltip from "react-tooltip";

import MapChart from "./MapChart";

function App() {
  const [content, setContent] = useState("");
  const [series, setSeries] = useState("CO2 emissions (metric tons per capita)");
  const [year, setYear] = useState("2011")
  return (
    <div className="base">
      <div className="container">
        <h2>Environmental Awareness Model</h2>
        <div className="form">
          <label>Select data:</label>
          <select value={series} onChange={e => setSeries(e.target.value)}>
            <option>CO2 emissions (metric tons per capita)</option>
            <option>CO2 emissions (kt)</option>
            <option>Total greenhouse gas emissions (kt of CO2 equivalent)</option>
            <option>Terrestrial and marine protected areas (% of total territorial area)</option>
            <option>Access to electricity (% of population)</option>
            <option>Energy use (kg of oil equivalent per capita)</option>
            <option>GDP per unit of energy use (PPP $ per kg of oil equivalent)</option>
            <option>Total natural resources rents (% of GDP)</option>

          </select>
        </div>
        <div className="form">
          <label>Select year:</label>
          <input type="number" value={year} onChange={e => setYear(e.target.value)} />
        </div>
      </div>
      <div className="map">
        <MapChart series={series} year={year} setTooltipContent={setContent} />
        <ReactTooltip>{content}</ReactTooltip>
      </div>
    </div>
  );
}

export default App;
