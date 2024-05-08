import React, { useEffect, useState, memo } from "react";
import {
  ZoomableGroup,
  ComposableMap,
  Geographies,
  Geography,
} from "react-simple-maps";
import { scaleQuantile } from "d3-scale";
import { csv } from "d3-fetch";
import { max } from "d3-array";
import dataset from "./dataset.csv";

const geoFile = "./static/features.json";

const MapChart = ({ setTooltipContent, series, year }) => {
  const [data, setData] = useState([]);

  useEffect(() => {
    // https://www.bls.gov/lau/
    csv(dataset).then((dataset) => {
      setData(dataset);
    });
  }, []);
  return (
    <>
      <ComposableMap
        data-tip=""
        projectionConfig={{
          rotate: [-40, 0, 0],
          scale: 180,
        }}
        style={{
          maxHeight: "600",
          paddingLeft: "25%",
          paddingRight: "25%",
        }}
      >
        <ZoomableGroup>
          <Geographies geography={geoFile}>
            {({ geographies }) =>
              geographies.map((geo) => {
                const cur = data.find(
                  (s) =>
                    s.Country_Name === geo.properties.name &&
                    s.Series_Name === series
                );
                const colorScale = scaleQuantile()
                  .domain(
                    data
                      .filter((d) => d.Series_Name === series)
                      .map((d) => d[year])
                  )
                  .range([
                    "#ffedea",
                    "#ffcec5",
                    "#ffad9f",
                    "#ff8a75",
                    "#ff5533",
                    "#e2492d",
                    "#be3d26",
                    "#9a311f",
                    "#782618",
                  ]);
                return (
                  <Geography
                    key={geo.rsmKey}
                    geography={geo}
                    onMouseEnter={() => {
                      if (cur) {
                        setTooltipContent(
                          geo.properties.name + ": " + cur[year]
                        );
                        if (!cur[year]) {
                          setTooltipContent(geo.properties.name + ": No data");
                        }
                      } else {
                        setTooltipContent(geo.properties.name + ": No data");
                      }
                    }}
                    onMouseLeave={() => {
                      setTooltipContent("");
                    }}
                    stroke="#aaa"
                    strokeWidth="0.5"
                    fill={cur && cur[year] ? colorScale(cur[year]) : "#EEE"}
                    style={{
                      default: {
                        outline: "none",
                      },
                      hover: {
                        fill: "#c9e4ca",
                        outline: "none",
                      },
                      pressed: {
                        fill: "#E42",
                        outline: "none",
                      },
                    }}
                  />
                );
              })
            }
          </Geographies>
        </ZoomableGroup>
      </ComposableMap>
    </>
  );
};

export default MapChart;
