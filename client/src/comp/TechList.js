import { useState, useEffect } from "react";

function TechList() {

    const [lOTechs, setlOTechs] = useState([])

    useEffect(() => {
        fetch('/techs').then(
            r => {
                    return r.json()
            }
        ).then( body => {
            setlOTechs(body)
        })
    }, [])

    if (!lOTechs) {
        return (<div id="loading">Loading</div >)
    }

    
    let carCounter = id => {
        id -=1;
        let carCount = 0;
        for (let x = 0 ; x < lOTechs[id].tech_cars.length ; x++) {
            carCount += 1;
        }
        return (<>{carCount}</>)
    }

    let renderTechs = lOTechs.map( tech => {
        return (<div className="techCard" key={`techCard${tech.id}`}>
            <h3>Name: {tech.name}</h3>
            {/* <p>Rate: {tech.rate}</p> */}
            <p>Cars: {carCounter(tech.id)}</p>
        </div>)
    })


    return (
        <div className="TechList">
            TechList
            {renderTechs}
        </div>
    )
}

export default TechList;