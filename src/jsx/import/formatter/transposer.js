/**
 * transpose.js: converts an object of arrays, to it's transpose equivalent,
 *                within an array of arrays.
 *
 *     The following input:
 *
 *         const obj = {
 *             'decision_function': [
 *                 1.0610881348559356,
 *                 2.438911865144064
 *             ],
 *             'classes': [
 *                 'dep-variable-1',
 *                 'dep-variable-2',
 *                 'dep-variable-3'
 *             ],
 *             'probability': [
 *                 0.011340985822887105,
 *                 0.04184262393469196,
 *                 0.9468163902424211
 *             ]
 *         }
 *
 *     Will yield the following, when transposed:
 *
 *         const obj = [
 *             [
 *                 1.0610881348559356,
 *                 'dep-variable-1',
 *                 0.011340985822887105
 *             ],
 *             [
 *                 2.438911865144064,
 *                 'dep-variable-2',
 *                 0.04184262393469196
 *             ],
 *             [
 *                 undefined,
 *                 'dep-variable-3',
 *                 0.9468163902424211
 *             ]
 *         ]
 */

function convert(obj) {
    // local variables
    const keys = Object.keys(obj);
    const max = Math.max(...keys.map(k => obj[k].length));

    // return value
    return Array.from({ length: max }).map((_, i) => {
        return keys.map(k => obj[k][i])
    });
}

export default function transpose(value) {
    return convert(value);
}
