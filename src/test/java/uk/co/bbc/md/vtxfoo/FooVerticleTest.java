package uk.co.bbc.md.vtxfoo;

import java.io.IOException;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;

import io.vertx.core.DeploymentOptions;
import io.vertx.core.Vertx;
import io.vertx.core.json.JsonObject;
import io.vertx.ext.unit.Async;
import io.vertx.ext.unit.TestContext;
import io.vertx.ext.unit.junit.VertxUnitRunner;

@RunWith(VertxUnitRunner.class)
public class FooVerticleTest {

    private Vertx vertx;
    private Integer port = 8080;

    @Before
    public void setUp(TestContext ctx) throws IOException {
        vertx = Vertx.vertx();

        JsonObject appConf = new JsonObject().put("http.port", port)
                                             .put("jdbc.url", "jdbc:hsqldb:mem:test?shutdown=true")
                                             .put("jdbc.driver_class", "org.hsqldb.jdbcDriver");

        DeploymentOptions opts = new DeploymentOptions().setConfig(appConf);

        vertx.deployVerticle(FooVerticle.class.getName(), opts, ctx.asyncAssertSuccess());
    }

    @After
    public void tearDown(TestContext ctx) {
        vertx.close(ctx.asyncAssertSuccess());
    }

    @Test
    public void testAppDeployment(TestContext context) {
        // get an async handler to inform the test when we are done.
        final Async async = context.async();

        vertx.createHttpClient().getNow(8080, "localhost", "/status", response -> {
            context.assertEquals(200, response.statusCode());
            async.complete();
        });
    }

}
