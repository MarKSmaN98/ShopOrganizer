import { useState, useEffect } from "react";
import CarList from "./CarList";
import TechList from "./TechList";

function Home() {

    return (
        <div className="MainContainer">
            <h1 id='homeBanner'>HOME!@</h1>
            <TechList />
            <CarList />
        </div>
    )
}

export default Home;