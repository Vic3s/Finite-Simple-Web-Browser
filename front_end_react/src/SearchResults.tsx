import { useState, useEffect } from "react"
import { useLocation } from "react-router-dom"
import type { SearchResultType,  } from "./Interfaces"
import { SearchResultItem } from "./components/SearchResultItem"
import { SearchBar } from "./components/SearchBar"
import "./styling/search-result.css"
import finite_logo from "../public/FInite_logo.png" 

export const SearchResult = () => {

    const[stateObject, setStateObject] = useState<Array<SearchResultType>>([])
    const locaion = useLocation()

    useEffect(() => {
        if(locaion.state){
            setStateObject(locaion.state)
        }
    }, [ locaion.state ])

    return (
        <>
            <div className="search-result-container d-flex">
                <div 
                className="logo-finite-container d-flex flex-column align-items-center" 
                style={{"width": "300px", "height": "95vh", "margin": "auto"}}>
                    <img src={finite_logo} alt="Finite logo" style={{"width": "80%"}}/>
                </div>
                <div className="main-content-result d-flex flex-column gap-3">
                    <SearchBar/>
                    <div className="results-list-container">
                        <div className="results">
                            {stateObject.map((resultObject: SearchResultType) => {
                                return (
                                    <>
                                        {resultObject.url && <SearchResultItem key={resultObject.url}  {...resultObject}/>}
                                    </>
                                )
                            })}
                        </div>
                    </div>
                
                </div>
                <div style={{"width": "300px", "height": "95vh", "margin": "auto"}}>
                </div>
            </div>
        </>
    )
}