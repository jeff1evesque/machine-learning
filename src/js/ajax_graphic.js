/**
 * ajax_loader.js: this file implements an overlay graphic when an ajax call
 *                 is being executed.
 */

/**
 * ajaxLoader: primary function for this file
 */

function ajaxLoader (el) {
  var defaults = {
    bgColor      : '#fff',
    duration     : 800,
    opacity      : 0.45,
    classOveride : false
  }

    this.options    = defaults;
    this.container  = el;

    this.init = function() {
      var container = this.container;

  // Delete any other loaders
      this.remove();

  // Create the overlay
      var overlay = $('<div></div>').css({
        'background-color': this.options.bgColor,
        'opacity':this.options.opacity,
        'width':container.width(),
        'height':container.height()+45, // 45, overlay form submit button
        'position':'absolute',
        'top':'0px',
        'left':'0px',
        'z-index':99999
      }).addClass('ajax_overlay');

  // insert overlay and loader into DOM
    container.append(
      overlay.append(
        $('<div></div>').addClass('ajax_loader')
      ).fadeIn(this.options.duration)
    );
  };

  this.remove = function() {
    var overlay = this.container.children('.ajax_overlay');

    if (overlay.length) {
      overlay.fadeOut(this.options.classOveride, function() {
        overlay.remove();
      });
    }  
  }
 
  this.init();

}
