/**
 * load-storage.jsx: retrieves values from the sessionStorage:
 *
 *     https://developer.mozilla.org/en-US/docs/Web/API/Window/sessionStorage
 *
 */

// attempt to retrieve from sessionStorage
export const loadState = (key) => {
    try {
        var serializedState = sessionStorage.getItem(key);
        if (serializedState === null) {
            return undefined;
        }

        return JSON.parse(serializedState);
    } catch (error) {
        return undefined;
    }
};

// attempt to save (key, value) into sessionStorage
export const saveState = (key, value) => {
    try {
        var serializedState = JSON.stringify(value);
        sessionStorage.setItem(key, serializedState);
    } catch (error) {
        console.log(error);
    }
};
