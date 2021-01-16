module.exports = {
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader"
                }
            },
            {

                test: /\.css$/,

                use: [

                    'style-loader',

                    'css-loader'

                ]

            },

            {

                test: /\.(png|svg|jpg|gif)$/,

                use: [

                    'file-loader'

                ]

            },

            {

                test: /\.(woff|woff2|eot|ttf|otf)$/,

                use: [

                    'file-loader'

                ]

            }
            
        ]
    }
};
