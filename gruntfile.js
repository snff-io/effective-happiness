module.exports = function(grunt) {
    grunt.initConfig({
        watch: {
            files: ["app/ts/**/*.ts"],
            tasks: ["ts"]
        },
        ts: {
            default: {
                src: ["app/ts/**/*.ts"],
                outDir: "app/js",
                options: {
                    rootDir: "app/ts"
                }
            }
        }
    });

    grunt.loadNpmTasks("grunt-ts");
    grunt.loadNpmTasks("grunt-contrib-watch");

    grunt.registerTask("default", ["watch"]);
};