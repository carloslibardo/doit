import {
  OPEN_LOGIN_MODAL,
  CLOSE_LOGIN_MODAL
} from './types';

export const openLoginModal = () => ({
  type: OPEN_LOGIN_MODAL,
  payload: true
});

export const closeLoginModal = () => ({
  type: CLOSE_LOGIN_MODAL,
  payload: false
})