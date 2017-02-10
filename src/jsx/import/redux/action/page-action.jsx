/**
 * page-action.jsx: send current page settings to the redux store.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 */

function setPageState(settings) {
  // local variables
    var current_page = settings.current_page;

    return {
        page: { current_page: current_page }
    };
}

// indicate which class can be exported, and instantiated via 'require'
export default setPageState
