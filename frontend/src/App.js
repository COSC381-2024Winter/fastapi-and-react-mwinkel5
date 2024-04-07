import './App.css';
import { TextField } from '@mui/material'
import { useEffect, useState } from 'react'

function App() {
  const [movieId, setMovieId] = useState("1")

  useEffect(() => {
    console.log(`${movieId}`)
  }, [movieId])

  return (
    <div className="App">
      <header className="App-header">
        <TextField
          id="outline-basic"
          label="Movie ID"
          variant="outlined"
          color="warning" focused
          value={movieId}
          onChange={e=>setMovieId(e.target.value)}
        />
      </header>
    </div>
  );
}

export default App;
