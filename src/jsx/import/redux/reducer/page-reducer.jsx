/**
 * page-reducer.jsx: describe page attributes.
 *
 * Note: the triple dots is the 'object spread' syntax:
 *
 *       http://redux.js.org/docs/recipes/UsingObjectSpreadOperator.html
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 */

const pageConfig = (state='default', action) => {
    switch(action.type) {
        case 'SUBMIT-SV-ANALYSIS':
            return Object.assign({}, state, {
                status: 'default',
                submit_button: {
                    analysis: action.submit_button.analysis
                }
            });
        default:
            return state;
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default pageConfig
