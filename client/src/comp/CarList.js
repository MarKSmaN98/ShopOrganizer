import { useState, useEffect } from "react";

function CarList() {

    const [carList, setCarList] = useState([])

    useEffect(() => {
        fetch('/cars').then( r => {
            return r.json()
        }).then( body => {
            setCarList(body)
        })
    }, [])

    if (!carList) {
        return (<div id="loading">...Loading...</div>)
    }

    console.log(carList)

    let renderCars = carList.map( car => {
        return (
            <div className="CarCard" key={`CarCard${car.id}`}>
                <h3>Customer: {car.customer}</h3>
                <h4>Car: {`${car.year} ${car.make} ${car.model}`} </h4>
            </div>
        )
    })

    return (
        <div className="CarList">
            {renderCars}
        </div>
    )
}

export default CarList;