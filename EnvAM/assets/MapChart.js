import React, { useState, memo } from "react";
import {
  ZoomableGroup,
  ComposableMap,
  Geographies,
  Geography
} from "react-simple-maps";

const geoUrl =
  "https://raw.githubusercontent.com/zcreativelabs/react-simple-maps/master/topojson-maps/world-110m.json";

const MapChart = ({ setTooltipContent, selected, setSelected }) => {
  return (
    <>
      <ComposableMap data-tip=""
      projectionConfig={{
        rotate: [-15, 0, 0],
        scale: 180
      }}
      style={{
        maxHeight: "450"
      }}
      >
        <ZoomableGroup>
          <Geographies geography={geoUrl}>
            {({ geographies }) =>
              geographies.map(geo => (
                <Geography
                  key={geo.rsmKey}
                  geography={geo}
                  onMouseEnter={() => {
                    const { NAME, POP_EST } = geo.properties;
                    setTooltipContent(`${NAME}`);
                  }}
                  onMouseLeave={() => {
                    setTooltipContent("");
                  }}
                  onClick={() => {
                    setSelected(geo.properties.NAME)
                  }}
                  stroke='#aaa'
                  strokeWidth='0.5'
                  fill = {geo.properties.NAME === selected ? "#e42" : "#D6D6DA"}
                  style={{
                    default: {
                      outline: 'none'
                    },
                    hover: {
                      fill: "#F53",
                      outline: 'none'
                    },
                    pressed: {
                      fill: "#E42",
                      outline: 'none'
                    }
                  }}
                />
              ))
            }
          </Geographies>
        </ZoomableGroup>
      </ComposableMap>
    </>
  );
};

export default memo(MapChart);
