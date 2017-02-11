/**
 * page-action.jsx: send current page settings to the redux store.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 */

function setPageState(settings) {
    return {
        page: { layout: settings.layout }
    };
}

// indicate which class can be exported, and instantiated via 'require'
export default setPageState
