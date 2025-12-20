import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { Index } from './Index'
import { SearchResult } from './SearchResults'
import { createBrowserRouter, RouterProvider } from 'react-router'

const router = createBrowserRouter([{path: "/", element: <Index/>}, {path:"/search-result", element: <SearchResult/>}])
createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <RouterProvider router={router}/>
  </StrictMode>,
)
