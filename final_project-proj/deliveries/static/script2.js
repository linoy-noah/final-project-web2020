$(document).ready(function () {
  $.getJSON("../static/typeIcons.json", function (data) {
      console.log(data);
      $.each(data, function (key, val) {
          console.log(key + " .type");
          console.log("=" + val)
          $(key + " .type").css('background', 'url("' + val + '") no-repeat');
          $(key + " .type").css('background-size', 'contain');
      });
  });
});