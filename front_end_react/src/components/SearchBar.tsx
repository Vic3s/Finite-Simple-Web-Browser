import { useState } from "react"
import { useNavigate } from "react-router"
import axios from "axios"
import search_bar_icon from "../../public/magnifying-glass-svgrepo-com.svg"
import "../styling/search_bar.css"

export const SearchBar = () => {

    const[searchString, setSearchString] = useState("");

    const navigate = useNavigate()

    const submitSearch = async (e: React.FormEvent<HTMLFormElement>): Promise<void> => {
        e.preventDefault();

        const result = await axios.post("http://127.0.0.1:3000/search", { "searchString": searchString })
        .then((result) => {
            if (typeof result.data === "object" && result.data !== null && !Array.isArray(result.data)) {
                console.log(result.data)
                navigate("/search-no-information", {state: result.data})
                return 
            }
            navigate("/search-result", { state: result.data })
            return 
        })
        .catch(err => {
            console.log(err)
        })
        
    }

    return (<>
        <form style={{"minWidth": "43vw", "borderRadius": "100px"}} onSubmit={submitSearch} >
            <div className="input-group">
                <input
                type="search"
                className="form-control fs-5"
                placeholder="Every second counts..."
                aria-label="Search"
                style={{"borderTopLeftRadius": "100px", "borderBottomLeftRadius": "100px", "minHeight":"60px", "paddingLeft": "30px"}}
                onChange={e => setSearchString(e.target.value)}
                />
                <button 
                type="submit" 
                style={{"background": "white", "borderTopRightRadius": "100px", "borderBottomRightRadius": "100px",
                     "color": "rgba(106, 106, 106, 1)", "borderColor": "rgb(222, 226, 230)", "borderLeft": "none", "paddingRight": "30px"}} 
                className="btn btn-primary fw-bold fs-5">
                    <img src={search_bar_icon} alt="magnifyer icon" style={{"width": "45px"}}/>
                </button>
            </div>
        </form>
    </>)
}