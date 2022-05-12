import React from 'react';
import { Link } from 'react-router-dom';

function App() {
  return (
  	<div>
		<Link to="/dashboard">
			<button> Login </button>
		</Link>
	</div>
  );
}

export default App;
