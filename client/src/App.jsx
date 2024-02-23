import { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [user, setUser] = useState({});
  const [input, setInput] = useState('');

  useEffect(() => {
    // Fetch user data on component mount
    fetch('http://localhost:8000/data')
      .then((res) => res.json())
      .then((data) => {
        console.log("this is data", data);
        setUser(data);
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
      });
  }, []);

  const handleInputChange = (event) => {
    // Update input state on user input
    setInput(event.target.value);
  };

  const handleFormSubmit = () => {
    // Send POST request on form submission
    fetch('http://localhost:8000/input', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ input }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        // Update input state if needed
        // setInput(data);
      })
      .catch((error) => console.error(error));
  };

  return (
    <div>
      {user.name ? (
        <div>{user.name}</div>
      ) : (
        <div>Loading...</div>
      )}
      <input type="text" value={input} onChange={handleInputChange} />
      <button onClick={handleFormSubmit}>Submit</button>
      <p>New user added is: {input}</p>
    </div>
  );
}

export default App;


