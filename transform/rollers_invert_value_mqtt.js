(function(i) { switch (i) {
		case "ON":
			return 100;
			break;
		case "OFF":
			return 0;
			break;
		default :
			return 100 - i;
	   
			} })(input)