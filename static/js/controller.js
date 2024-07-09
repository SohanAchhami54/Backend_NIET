app.controller("bioController", function ($scope, $http) {
  $scope.postMessage = function (data) {
    $http.post("/message/", data).then(
      function (response) {
        console.log("Message sent successfully:", response.data);
        // Show Bootstrap toast message
        $(".toast").toast("show");
        // Clear form fields
        $scope.newData = {};
      },
      function (error) {
        console.log("Error sending message:", error);
      }
    );
  };
});
