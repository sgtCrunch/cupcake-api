
const BASE_URL = "/api/cupcakes"

function createCupcake(cupcake){

    let $cupcakeRow = $('#cupcakes');
    let $cupcakeDiv = $('<div>').addClass('col-sm-3');

    $cupcakeDiv.append(
        $('<img>')
        .attr('src', cupcake.image)
        .addClass('img-thumbnail')
    );

    $cupcakeDiv.append(
        $('<h6>')
        .text(cupcake.flavor)
    );

    $cupcakeDiv.append(
        $('<h6>')
        .text('Size: ' + cupcake.size)
    );

    $cupcakeDiv.append(
        $('<h6>')
        .text('Rating: ' + cupcake.rating)
    );

    $cupcakeRow.append($cupcakeDiv);

}

async function getCupcakes(){
    const res = await axios({
        url: BASE_URL,
        method: "GET",
    });

    

    for(let cupcake of res.data.cupcakes){
        createCupcake(cupcake);
    }

}


$(async function(){
    await getCupcakes();
    $('#form-cupcake').on('submit', async function(e){
        e.preventDefault();
        new_cupcake = {
            'flavor' : $('#flavor').val(),
            'size' : $('#size').val(),
            'rating' : $('#rating').val(),
            'image' : $('#image').val(),
        };
        const res = await axios({
            url: BASE_URL,
            method: "POST",
            data : new_cupcake
        });
        createCupcake(res.data.cupcakes);
        $('#flavor').val("");
        $('#size').val("");
        $('#rating').val("");
        $('#image').val("");
    });
});