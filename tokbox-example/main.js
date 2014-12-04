var VTokBox = {};

(function(){

	this.initSession = function() {

        // config
        var apiKey = "foo";
        var token = "bar";
        var sessionId = "foobar";

		// init session
		var session = OT.initSession(apiKey, sessionId);

        // connect
		session.connect(token, function(error){
            console.log("sanity check!")
			var options = {width: 500, height:400, name:"Publisher"};
			var publisher = OT.initPublisher('myPublisher', options);
			session.publish(publisher);
		});

		return session;
	};

}).apply(VTokBox);