package uk.co.bbc.md.vtxfoo;

import java.io.IOException;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;

import io.vertx.core.Vertx;
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
        vertx.deployVerticle(FooVerticle.class.getName(), ctx.asyncAssertSuccess());
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
