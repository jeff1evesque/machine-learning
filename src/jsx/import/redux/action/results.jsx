/**
 * results.jsx: send current prediction result to the redux store.
 *
 */

function setResults(action) {
    return {
        type: 'SET-RESULTS',
        results: {
            type: action.type,
            data: action.data
        }
    };
}

// indicate which class can be exported, and instantiated via 'require'
export default setResults
