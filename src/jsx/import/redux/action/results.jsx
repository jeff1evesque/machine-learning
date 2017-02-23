/**
 * results.jsx: send current prediction result to the redux store.
 *
 */

function setResults(action) {
    return {
        type: 'DISPLAY-RESULT',
        result: {
            type: action.analysis.type,
            results: {
                keys: action.analysis.data.keys.split(/\s*,\s*/),
                values: action.analysis.data.values.split(/\s*,\s*/)
            }
        }
    };
}

// indicate which class can be exported, and instantiated via 'require'
export default setResults
