/**
 * page.jsx: send current support vector 'submit button' boolean, indication
 *           whether it should be displayed to the redux store.
 *
 */

function setSvButton(action) {
    return {
        type: 'SUBMIT-SV-ANALYSIS',
        button: {
            submit_analysis: action.button.submit_analysis
        }
    };
}

// indicate which class can be exported, and instantiated via 'require'
export { setSvButton }
