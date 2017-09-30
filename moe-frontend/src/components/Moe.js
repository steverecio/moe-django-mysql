import React, { Component } from 'react';
import './Moe.css';

const RMS_PHOTOS = [
    "https://stallman.org/photos/rms-working/mid/mid_p1000844.jpg",
    "https://stallman.org/photos/rms-working/mid/mid_img_0554.jpg",
    "https://stallman.org/photos/rms-working/mid/mid_img_1755.jpg",
    "https://stallman.org/photos/rms-working/mid/mid_img_3235.jpg",
    "https://stallman.org/photos/rms-working/mid/mid_img_3658.jpg",
    "https://stallman.org/photos/rms-working/mid/mid_img_4188.jpg",
    "https://stallman.org/photos/rms-working/mid/mid_working-with-the-devil.jpg",
    "https://stallman.org/photos/rms-working/mid/mid_p1000541.jpg",
];

function choose(choices) {
    let index = Math.floor(Math.random() * choices.length);
    return choices[index];
}


class Moe extends Component {

  constructor(props) {
    super(props);
    this.state = {src: choose(RMS_PHOTOS)};
    this.updateMoe = this.updateMoe.bind(this);
  }

  updateMoe() {
    this.setState({
      src: choose(RMS_PHOTOS)
    });
  }

  render() {
    return (
       <img className="Moe" src={this.state.src} onClick={this.updateMoe} />
    );
  }
}

export default Moe;
