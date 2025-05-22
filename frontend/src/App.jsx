import { BrowserRouter, Route, Routes } from "react-router-dom";
import { Home } from "./components/Pages/Home";
import { User } from "./components/Pages/User";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/:userId" element={<User isRandom={false} />} />
        <Route path="/random" element={<User isRandom={true} />} />
        <Route path="/:userId" element={<User isRandom={false} />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
