function rCombi(str, arr) {
	arr = arr || [""];
	if (!str.length) {return arr;}
	var last = str[0];
	str = str.slice(1, str.length);
	for (var i = 0, len = arr.length; i < len; i++) {
		arr.push(arr[i] + last)
		console.log("arrrr", arr)
	}
	console.log(arr, str, "console log before end")
	return rCombi(str, arr);
}

var string = "ABCD";
console.log(rCombi(string), "this is result");
