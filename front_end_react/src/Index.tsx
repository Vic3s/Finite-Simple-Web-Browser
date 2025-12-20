import { SearchBar } from "./components/SearchBar"
import { LogoSearch } from "./components/LogoSearch"
import { MoreSeacthOptions } from "./components/MoreSearchOptions";

export const Index = () => {

    return (<>
    
        <div className="main-container">
            <div className="main-content d-flex flex-column align-items-center justify-content-center gap-5" 
            style={{"minHeight": "70vh"}}>
                <LogoSearch/>
                <SearchBar/>
                <MoreSeacthOptions/>
            </div>
        </div>
    
    </>);
}


