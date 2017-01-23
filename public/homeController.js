var app = new angular.module('financeapp', []);

app.controller('homeController', function($scope, $http) {
	var flag = 0;
	var iheight = -1;
	$scope.posts = [];
	$scope.botPosts = [];
	$scope.chattext = undefined;

	$scope.submitPost = function() {
		if (iheight == -1) {
			iheight = angular.element(document.querySelector('#scrollable'))[0].offsetHeight;
		}
		if (!$scope.ctext || $scope.ctext === '') { return; }
		$scope.posts.push({
			text: $scope.ctext,
			id: $scope.posts.length + 1
		});

		$http.post('/', {'out': $scope.ctext})
		.then(function(res){
			//console.log(JSON.stringify(res));
		});

		$http.get('/post').then(function(res) {
			//console.log(JSON.stringify(res));
		});

		$http.get('/subm').then(function(res) {
			$scope.botPosts.push({id: $scope.botPosts.length + 1, data: "Sorry I can't help you right now."});
			console.log(JSON.stringify(res, null, 2));
		});

		$scope.ctext = '';
		$scope.$watch('posts', function() {
			if (angular.element( document.querySelector('#chatbox'))[0].offsetHeight > angular.element( document.querySelector('#scrollable'))[0].offsetHeight - iheight && flag == 0) {
				angular.element( document.querySelector('#chatbox'))[0].style.overflow = 'hidden';
			} else {
				flag = -1;
				angular.element( document.querySelector('#scrollable'))[0].style.top = '0px';
				angular.element( document.querySelector('#chatbox'))[0].style.overflowY = 'scroll';
				angular.element( document.querySelector('#scrollable'))[0].offsetHeight = angular.element( document.querySelector('#chatbox'))[0].scrollHeight;
				angular.element( document.querySelector('#chatbox'))[0].scrollTop = angular.element( document.querySelector('#chatbox'))[0].scrollHeight;
			}
		});

	};
});
