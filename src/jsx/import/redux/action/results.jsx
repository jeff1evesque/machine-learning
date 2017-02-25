/**
 * results.jsx: send current prediction result to the redux store.
 *
 */

function setResults(action) {
    return {
        type: 'DISPLAY-RESULTS',
        data: {
            type: action.type,
            results: {
                keys: action.data.results.keys,
                values: action.data.results.values
            }
        }
    };
}

// indicate which class can be exported, and instantiated via 'require'
export default setResults
