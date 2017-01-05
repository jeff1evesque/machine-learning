/**
 * load-storage.jsx: retrieves values from the sessionStorage:
 *
 *     https://developer.mozilla.org/en-US/docs/Web/API/Window/sessionStorage
 *
 */

// redux store: entire state tree for the application
const loadState = (key) => {
    try {
        const serializedState = sessionStorage.getItem(key);
        if (serializedState === null) {
            return undefined;
        }

        return JSON.parse(serializedState);
    } catch (error) {
        return undefined;
    }
};

// indicate which class can be exported, and instantiated via 'require'
export default loadState
