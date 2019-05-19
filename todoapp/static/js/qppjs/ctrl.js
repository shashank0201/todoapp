var todo_app = angular.module('mytodoApp', ["ngRoute"], function ($interpolateProvider, $httpProvider) {
            $httpProvider.defaults.xsrfCookieName = 'csrftoken';
            $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
	
            $interpolateProvider.startSymbol('[[');
	        $interpolateProvider.endSymbol(']]');     
});

todo_app.controller('mytodoCtrl', function($scope, $http, $timeout) {
    $scope.show_panel = true;
    $scope.todo_record_list = [];
    $scope.status_list = ["Inprogress", "Completed", "Pending"];
    $http.get("/get_todo_list").then(function (response) {
    		console.log("___called the servies dollor http servies  in the success _____");
            $scope.todo_record_list = response.data.data;
            $scope.edit_pk = false;
        });
        $scope.delete_record = function(deleteId){
            $http.post("/", {"deleteId":deleteId,"method":"delete"}).then(function (response) {
                $scope.todo_record_list = response.data.data;
                $scope.edit_pk = false;
                console.log("This function handles success");
                alert(response.data.status);
                    $scope.title  = "";
                    $scope.descriptions =  "";
                    $scope.completion_date = "";
                    $scope.status = "";
                    $scope.edit_pk = false;
                }, function (response) {
                
                    console.log("this function handles error");
                
                });


        }
        $scope.edit_record = function(edit_id, title, descriptions, completion_date,status){
            $scope.title  = title;
            $scope.descriptions =  descriptions;
            $scope.completion_date = completion_date;
            $scope.status = status.toString();
            $scope.edit_pk = edit_id;
            $('#save_update').text('update');

        }

        $scope.save = function(){
            $scope.show_panel = false;
            $scope.show_table = true;

            if ($scope.title && $scope.descriptions && $scope.status && ($scope.edit_pk).toString() )
            {
                $http.post("/", {"title":$scope.title, 
                            "descriptions":  $scope.descriptions ,
                            "completion_date": $('#datepicker').val(),
                            "status":$scope.status,
                            "edit_id":($scope.edit_pk).toString(),
                            "method":"save_rec"}).then(function (response) {
                $scope.todo_record_list = response.data.data;
                $scope.edit_pk = false;
                console.log("This function handles success");
                
                $scope.title  = "";
                $scope.descriptions =  "";
                $scope.completion_date = "";
                $scope.status = "";
                $scope.edit_pk = false;
                $('#save_update').text('SAVE');
                alert(response.data.status);


                }, function (response) {
                
                    console.log("this function handles error");
                
                });
            }
            else{
                alert("Enter all fields ");
                $scope.show_panel = true;
                $scope.show_table = false;
            }
            

        }

        $scope.clear = function(){
            $scope.title  = "";
            $scope.descriptions =  "";
            $scope.completion_date = "";
            $scope.status = "";
            $scope.edit_pk = false;
            $('#save_update').text('SAVE');
        }



});
