var app = angular.module("bioApp", []);
app.config([
  "$httpProvider",
  function ($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = "csrftoken";
    $httpProvider.defaults.xsrfHeaderName = "X-CSRFToken";
  },
]);
