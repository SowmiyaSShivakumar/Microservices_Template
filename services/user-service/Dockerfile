FROM openjdk:11-jre-slim
COPY target/user-service-*.jar user-service.jar
ENTRYPOINT ["java","-jar","/user-service.jar"]
