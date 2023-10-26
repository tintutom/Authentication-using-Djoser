// import React, { useState } from 'react';
// import { Link, useNavigate } from 'react-router-dom';
// import { connect } from 'react-redux';
// import { signup } from '../actions/auth';


// const DoctorSignup = ({ signup, isAuthenticated }) => {
//     const [accountCreated, setAccountCreated] = useState(false);
//     const navigate = useNavigate();
//     const [formData, setFormData] = useState({
//         first_name: '',
//         last_name: '',
//         email: '',
//         password: '',
//         re_password: '',
//         is_staff: true, // Set isDoctor to true to indicate staff (doctor)
//     });

//     const { first_name, last_name, email, password, re_password, is_staff } = formData;

//     const onChange = e => setFormData({ ...formData, [e.target.name]: e.target.value });
//     console.log("Onchange",formData)
//     const onSubmit = e => {
//         e.preventDefault();

//         if (password === re_password) {
//             // Pass the "isDoctor" field to the signup action
//             signup(first_name, last_name, email, password, re_password, is_staff);
//             setAccountCreated(true);
//         }
//     };

//     if (isAuthenticated) {
//         return navigate('/');
//     }
//     if (accountCreated) {
//         return navigate('/login');
//     }

//     return (
//         <div className='container mt-5'>
//             <h1>Sign Up</h1>
//             <p>Create your Account</p>
//             <form onSubmit={e => onSubmit(e)}>
//                 <div className='form-group'>
//                     <input
//                         className='form-control'
//                         type='text'
//                         placeholder='First Name*'
//                         name='first_name'
//                         value={first_name}
//                         onChange={e => onChange(e)}
//                         required
//                     />
//                 </div>
//                 <div className='form-group'>
//                     <input
//                         className='form-control'
//                         type='text'
//                         placeholder='Last Name*'
//                         name='last_name'
//                         value={last_name}
//                         onChange={e => onChange(e)}
//                         required
//                     />
//                 </div>
//                 <div className='form-group'>
//                     <input
//                         className='form-control'
//                         type='email'
//                         placeholder='Email*'
//                         name='email'
//                         value={email}
//                         onChange={e => onChange(e)}
//                         required
//                     />
//                 </div>
//                 <div className='form-group'>
//                     <input
//                         className='form-control'
//                         type='password'
//                         placeholder='Password*'
//                         name='password'
//                         value={password}
//                         onChange={e => onChange(e)}
//                         minLength='6'
//                         required
//                     />
//                 </div>
//                 <div className='form-group'>
//                     <input
//                         className='form-control'
//                         type='password'
//                         placeholder='Confirm Password*'
//                         name='re_password'
//                         value={re_password}
//                         onChange={e => onChange(e)}
//                         minLength='6'
//                         required
//                     />
//                 </div>
//                 <button className='btn btn-primary' type='submit'>Register</button>
//             </form>
            
//             <p className='mt-3'>
//                 Already have an account? <Link to='/login'>Sign In</Link>
//             </p>
//         </div>
//     );
// };

// const mapStateToProps = state => ({
//     isAuthenticated: state.auth.isAuthenticated
// });

// export default connect(mapStateToProps, { signup })(DoctorSignup);
