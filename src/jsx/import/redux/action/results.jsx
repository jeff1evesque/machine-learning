/**
 * results.jsx: send current prediction result to the redux store.
 *
 */

function setResults(action) {
    return {
        type: 'DISPLAY-RESULT',
        data: {
            type: action.type,
            results: {
                keys: action.results.keys.split(/\s*,\s*/),
                values: action.results.values.split(/\s*,\s*/)
            }
        }
    };
}

// indicate which class can be exported, and instantiated via 'require'
export default setResults
