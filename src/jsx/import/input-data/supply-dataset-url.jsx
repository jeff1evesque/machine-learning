/**
 * supply-dataset-url.jss: url upload fieldset.
 *
 * @SupplyDatasetUrl, must be capitalized in order for reactjs to render it as
 *     a component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import checkValidUrl from './../validator/valid-url.js';

class SupplyDatasetUrl extends React.Component {
  // initial 'state properties'
  getInitialState() {
    return {
      additional_elements: [],
    };
  }
  // update 'state properties': index for additional input elements
  handleAddMore() {
    const elements = this.state.additional_elements;
    elements.push(true);
    this.setState({ additional_elements: elements });
    this.props.onChange({ submitted_proper_predictor: false });
  }
  handleRemove() {
    const elements = this.state.additional_elements;
    let datasetBoolean = true;

    if (elements.length > 0) {
      elements.pop();
      this.setState({ additional_elements: elements });

      // define boolean to indicate all urls properly defined
      for (let index = 0; index < elements.length; index++) {
        const value = this.state[`value_dataset_${index.toString()}`];
        if (inputVal === undefined) {
          datasetBoolean = false;
        }
      }

      // allow parent component to know all files properly defined
      if (datasetBoolean) {
        this.props.onChange({ submitted_proper_dataset: true });
      } else {
        this.props.onChange({ submitted_proper_dataset: false });
      }

      // possibly clear submit button
      this.validUrlEntered();
    }
  }
  // update 'state properties': allow parent component(s) to access properties
  validUrlEntered() {
    // get array of input elements, by classname
    const dataset = document.getElementsByClassName('dataset-url');

    /*
            Iterate the node list containing the supplied dataset(s). If the
            input value is a valid file, store 'true', within the array.
    */
    const boolArray = Array.prototype.map.call(dataset, (element) => {
      if (element.value && checkValidUrl(element.value)) {
        return true;
      }
      return false;
    });

    // check if every element is 'true'
    const datasetFlag = boolArray.every(element => element === true);

    if (datasetFlag) {
      this.props.onChange({ submitted_proper_dataset: true });
    } else {
      this.props.onChange({ submitted_proper_dataset: false });
    }
  }
  // triggered when 'state properties' change
  render() {
    const inputs = this.state.additional_elements;

    return (
      <fieldset className="fieldset-supply-dataset">
        <legend>Supply Dataset</legend>
        <input
          type="url"
          name="dataset[]"
          placeholder="Dataset URL"
          className="dataset-url"
          onChange={this.validUrlEntered}
          defaultValue=""
        />

        <input
          type="button"
          value="Add more"
          onClick={this.handleAddMore}
        />

        <input
          type="button"
          value="Remove"
          onClick={this.handleRemove}
        />

        {/* array components require unique 'key' value */}
        {inputs && inputs.map((value, index) => (<input
          type="url"
          name="dataset[]"
          placeholder="Dataset URL"
          className="dataset-url"
          key={index}
          onChange={this.validUrlEntered}
          defaultValue=""
        />))}
      </fieldset>
    );
  }
}

// indicate which class can be exported, and instantiated via 'require'
export default SupplyDatasetUrl;
