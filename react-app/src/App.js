import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import NavBar from './components/navbar/NavBar';
import Shopping_Cart from './components/shopping_cart';
import Main from './components/main';
import MenuPage from './components/menu';
import ProtectedRoute from './components/auth/ProtectedRoute';
import UsersList from './components/UsersList';
import User from './components/User';
import { authenticate } from './store/session';
import IndividualProductPage from './components/individual_product_page';

function App() {
  const [cartStatus, setCartStatus] = useState('hidden')
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

  useEffect(() => {
    (async() => {
      await dispatch(authenticate());
      if(!localStorage.currentCart) localStorage.setItem('currentCart', JSON.stringify({}))
      setLoaded(true);
    })();
  }, [dispatch, setCartStatus]);


  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <NavBar cartStatus={cartStatus} setCartStatus={setCartStatus}/>
      <Switch>
        <ProtectedRoute path='/users' exact={true} >
          <UsersList/>
        </ProtectedRoute>
        <ProtectedRoute path='/users/:userId' exact={true} >
          <User />
        </ProtectedRoute>
        <Route path='/' exact={true} >
          <Main/>
        </Route>
        <Route path='/menu' exact={true} >
          <MenuPage/>
        </Route>
        <Route path='/individualproduct/:productId' exact={true} >
          <IndividualProductPage setCartStatus={setCartStatus}/>
        </Route>
      </Switch>
      <Shopping_Cart setCartStatus={setCartStatus} cartStatus={cartStatus}/>
    </BrowserRouter>
  );
}

export default App;
