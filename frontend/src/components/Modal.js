import React, { Component } from "react";
import {
  Button,
  Modal,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Form,
  FormGroup,
  Input,
  Label,
} from "reactstrap";

export default class CustomModal extends Component {
  constructor(props) {
    super(props);
    this.state = {
      activeItem: this.props.activeItem,
    };
  }
  
  handleChange = (e) => {
    let { name, value } = e.target;

    if (e.target.type === "checkbox") {
      value = e.target.checked;
    }

    const activeItem = { ...this.state.activeItem, [name]: value };

    this.setState({ activeItem });
  };

  render() {
    const { toggle, onSave } = this.props;

    return (
      <Modal isOpen={true} toggle={toggle}>
        <ModalHeader toggle={toggle}>Bus Stop Point</ModalHeader>
        <ModalBody>
          <Form>
            <FormGroup>
              <Label for="bus-stop-title">Title</Label>
              <Input
                type="text"
                id="bus-stop-title"
                name="title"
                value={this.state.activeItem.title}
                onChange={this.handleChange}
                placeholder="Enter Bus Stop Title"
              />
            </FormGroup>
            <FormGroup>
              <Label for="bus-stop-longitude">Longitude</Label>
              <Input
                type="text"
                id="bus-stop-longitude"
                name="longitude"
                value={this.state.activeItem.description}
                onChange={this.handleChange}
                placeholder="Enter Longitude"
              />
            </FormGroup>
            <FormGroup>
              <Label for="bus-stop-latitude">Latitude</Label>
              <Input
                type="text"
                id="bus-stop-latitude"
                name="latitude"
                value={this.state.activeItem.description}
                onChange={this.handleChange}
                placeholder="Enter Latitude"
              />
            </FormGroup>
          </Form>
        </ModalBody>
        <ModalFooter>
          <Button
            color="success"
            onClick={() => onSave(this.state.activeItem)}
          >
            Save
          </Button>
        </ModalFooter>
      </Modal>
    );
  }
}