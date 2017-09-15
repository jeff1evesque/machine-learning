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

function setGotoResultsButton(action) {
    return {
        type: 'GOTO-RESULTS',
        button: {
            goto_results: action.button.goto_results
        }
    };
}

function setLayout(action) {
    const layout = action.layout;
    const css    = action.css

    return {
        type: 'SET-LAYOUT',
        css: action.css,
        layout: action.layout
    };
}

// indicate which class can be exported, and instantiated via 'require'
export { setSvButton, setGotoResultsButton, setLayout }
