import { Bar } from './bar.js';

(function(){
	console.log( 'hello world!' )
	d3.json( '/load_data' ) // async
		.then( data => main( data ) ) // run the application
		.catch( err => console.error( err ) ) // print errors if there are any
})();

// Global Variables
function main( data ) {
	// Input to main
	d3.select( "#users" )
		.append( "span" )
		.text( data.users.length )

	let	bars = new Bar( data, 'vis1' );
}