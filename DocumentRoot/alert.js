/**
 * This tiny script makes it easy to make use of
 * bootstrap alerts!
 */
var Alert = (function() {
    "use strict";

    var elem,
        hideHandler,
        that = {};

    that.init = function(options) {
        elem = $(options);
    };

    that.show = function(response) {
        clearTimeout(hideHandler);
        elem.addClass('alert-'+response['type']);
        elem.html('<strong>'+response['message']+'</strong>');
        elem.delay(200).fadeIn().delay(4000).fadeOut();
    };

    return that;
}());