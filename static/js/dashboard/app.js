var app = angular.module("dashboardApp", []);
app.config([
  "$httpProvider",
  function ($httpProvider) {
    $httpProvider.defaults.withCredentials = true;
    $httpProvider.defaults.xsrfCookieName = "csrftoken";
    $httpProvider.defaults.xsrfHeaderName = "X-CSRFToken";
  },
]);

app.run(function ($http) {
  // Set CSRF token in all requests
  $http.defaults.headers.common["X-CSRFToken"] = document
    .querySelector('meta[name="csrf-token"]')
    .getAttribute("content");
});

app.directive("fileModel", [
  "$parse",
  function ($parse) {
    return {
      restrict: "A",
      link: function (scope, element, attrs) {
        var model = $parse(attrs.fileModel);
        var modelSetter = model.assign;

        element.bind("change", function () {
          scope.$apply(function () {
            modelSetter(scope, element[0].files[0]);
          });
        });
      },
    };
  },
]);
