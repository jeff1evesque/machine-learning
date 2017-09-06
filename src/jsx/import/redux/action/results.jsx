/**
 * results.jsx: send prediction results to the redux store.
 *
 */

function setResults(action) {
    return {
        type: 'SET-RESULTS',
        results: {
            nid: action.nid,
            data: action.results
        }
    };
}

// indicate which class can be exported, and instantiated via 'require'
export default setResults
