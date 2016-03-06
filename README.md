# vtxfoo
A scratch space for trying out vert.x 3

## Building and running locally
-------------------------------
Execute the following at the root of the project:
`./run.sh`

Having the above continuously running enables hot retesting, repackaging and local re-running following code changes.
If you want to see the raw start up time of the app (as long as you've run mvn package once), comment out the `mvn package` in the run.sh script and then re-run it.

## Building and running for CentOS target
-----------------------------------------

### Pre-requisites
------------------
* >= `java-1.8.0-openjdk-devel`
* >= `mbt-1.10.2-1.bbc.el6.noarch`

### Steps
---------
   1. Ensure that jdk 8 is providing the default `java` and `javac` commands
      in the sandbox (and choose the selection for java 1.8.0):

        sudo alternatives --config java
        sudo alternatives --config javac
        
   2. Build the RPM:

        make rpm

   3. Install the RPM:

        sudo yum remove -y vtxfoo
        sudo yum localinstall -y RPMS/vtxfoo*.rpm

   4. Start the service:

        sudo service vtxfoo start

   5. Confirm the service has started by tailing

        tail -F /var/log/vtxfoo/application.log

   6. Call the service status page:

        curl -v localhost:8080/status        

## References
-------------
http://vertx.io/docs/vertx-core/java/
http://vertx.io/docs/vertx-web/java/
https://github.com/vert-x3/vertx-examples/tree/master/web-examples/src/main/java/io/vertx/example/web/jdbc
