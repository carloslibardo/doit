import {
  OPEN_LOGIN_MODAL,
  CLOSE_LOGIN_MODAL
} from '../actions/types';

const INITIAL_STATE = {
  loginModalIsOpen: false
};

export default (state = INITIAL_STATE, action) => {
  switch (action.type) {
    case OPEN_LOGIN_MODAL:
      return { loginModalIsOpen: action.payload };
    case CLOSE_LOGIN_MODAL:
      return { loginModalIsOpen: action.payload }

    default:
      return state;
  }
};