/**
 * breakpoints.js: define consistent custom breakpoints.
 */

// constants
const small_maxWidth = 766;
const medium_minWidth = 767;
const medium_maxWidth = 1170;
const large_minWidth = 1171;

// constant breakpoints
const breakpoints = [
    { name: 'small', maxWidth: small_maxWidth },
    { name: 'medium', minWidth: medium_minWidth, maxWidth: medium_maxWidth },
    { name: 'large', minWidth: large_minWidth },
];

// update component on every size change
const breakpoints_exact = [
    { name: 'small', maxWidth: small_maxWidth, exact: true },
    {
        name: 'medium',
        minWidth: medium_minWidth,
        maxWidth: medium_maxWidth,
        exact: true
    },
    { name: 'large', minWidth: large_minWidth, exact: true },
];

export { breakpoints, breakpoints_exact }
