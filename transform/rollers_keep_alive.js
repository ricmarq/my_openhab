(function(i) {

//janela/sonoff/SENSOR {"Time":"2018-10-31T14:49:45","SHUTTER-1":100}

		var obj = JSON.parse(i);
		return 100 -  obj["SHUTTER-1"];
	})(input)