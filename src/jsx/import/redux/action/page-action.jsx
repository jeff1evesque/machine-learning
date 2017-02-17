/**
 * page-action.jsx: send current support vector 'submit button' boolean,
 *                  indicating whether it should be displayed to the redux
 *                  store.
 *
 */

function setSvButton(settings) {
    return {
        type: 'SUBMIT-SV-ANALYSIS',
        submit_button: {
            analysis: settings.submit_button.analysis
        }
    };
}

// indicate which class can be exported, and instantiated via 'require'
export default setSvButton
