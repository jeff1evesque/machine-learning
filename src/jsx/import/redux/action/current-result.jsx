/**
 * current-result.jsx: send current prediction result to the redux store.
 *
 */

function setCurrentResult(action) {
    return {
        type: 'SET-CURRENT-RESULT',
        results: {
            type: action.type,
            data: action.data
        }
    };
}

// indicate which class can be exported, and instantiated via 'require'
export default setCurrentResult
