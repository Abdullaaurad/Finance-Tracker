
const usernamevalidator = (username: string): boolean => {
  // Example validation: 3-10 characters, only alphanumeric
  return /^[a-zA-Z0-9_\-@]{3,20}$/.test(username);
}

const emailvalidator = (email: string): boolean => {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

const passwordvalidator = (password: string): boolean => {
    return /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/.test(password);
}

export { usernamevalidator, emailvalidator, passwordvalidator };