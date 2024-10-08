import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import { StarRating } from "./components/StarRating";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    {/*<App />*/}
    <StarRating
      maxRating={5}
      messages={["Terrible", "Bad", "Okay", "Good", "Amazing"]}
    />
    <StarRating maxRating={10} />
  </React.StrictMode>,
);
