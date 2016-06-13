function rCombi(str, arr) {
	arr = arr || [""];

	if (!str.length) {return arr;}

	var substr = str[0];

	str = str.slice(1, str.length);

	for (var i = 0, len = arr.length; i < len; i++) {
		arr.push(arr[i] + substr)
		console.log("arrrr", arr)
	}

	console.log(arr, str, "console log before end")

	return rCombi(str, arr);
}

var string = "ABCD";
// console.log(rCombi(string), "this is result");

function rPermutations(str, substr, arr){
	arr = arr || [];
	substr = substr || "";
	if (!str.length){arr.push(substr); return arr;}
	// console.log(str, "str", arr)
	for (var i = 0, len = str.length ; i < len; i++){
		// console.log(i, str)
		var before = str.slice(0, i);
		var after = str.slice(i + 1, str.length);
		rPermutations(before+after, substr+str[i], arr);
	}
	return arr;
}
// console.log(rPermutations(string));

function rInOrderSubstrings(str, arr, substr) {
	arr = arr || [];
	substr = substr || "";

	if (str === "") {
		arr.push(substr);
		console.log(str, arr, substr, -1)
	} else {
		console.log(str, arr, substr, 0);
		rInOrderSubstrings(str.slice(1), arr, substr + str.slice(0,1));
		console.log(str, arr, substr, 1);
		rInOrderSubstrings(str.slice(1), arr, substr);
		console.log(str, arr, substr, 2);
	}
	return arr;
}
rInOrderSubstrings("abc");









