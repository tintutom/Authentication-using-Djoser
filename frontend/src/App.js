import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Home from './containers/Home'
import Login from './containers/Login'
import ResetPassword from './containers/ResetPassword'
import ResetPasswordConfirm from './containers/ResetPasswordConfirm'
import Signup from './containers/Signup'
import Activate from './containers/Activate'
import { Provider } from 'react-redux'
import Layout from './hocs/Layout' // You should uncomment this line to use the Layout component
import store from './store'
import Google from './containers/Google'
import DoctorSignup from './containers/DoctorSignup'

const App = () => (
    <Provider store={store}>
      <Router>
          <Layout> 
            <Routes>
                <Route exact path='/' element={<Home />} />
                <Route path='/login' element={<Login />} />
                <Route path='/signup' element={<Signup />} />
                <Route path='/google' component={<Google />} />
                <Route path='/reset-password' element={<ResetPassword />} />
                <Route path='/password/reset/confirm/:uid/:token' element={<ResetPasswordConfirm />} />
                <Route path='/activate/:uid/:token' element={<Activate/>} />
                {/* <Route path='/docsignup' element={<DoctorSignup />} /> */}
            </Routes>
          </Layout>
      </Router>
    </Provider>
);
export default App;
