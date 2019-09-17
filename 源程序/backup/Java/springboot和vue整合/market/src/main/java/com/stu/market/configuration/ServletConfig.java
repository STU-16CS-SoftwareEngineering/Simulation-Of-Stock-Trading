package com.stu.market.configuration;

import com.stu.market.interceptor.LoginInterceptor;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.web.server.ConfigurableWebServerFactory;
import org.springframework.boot.web.server.ErrorPage;
import org.springframework.boot.web.server.WebServerFactoryCustomizer;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.HttpStatus;

@Configuration
public class ServletConfig {
    private static final Logger logger = LoggerFactory.getLogger(LoginInterceptor.class);
    @Bean
    public WebServerFactoryCustomizer<ConfigurableWebServerFactory> webServerFactoryCustomizer(){
        return factory -> {
            ErrorPage error404Page = new ErrorPage(HttpStatus.NOT_FOUND, "/index.html");
            ErrorPage error400Page = new ErrorPage(HttpStatus.BAD_REQUEST, "/index.html");
            ErrorPage error405Page = new ErrorPage(HttpStatus.METHOD_NOT_ALLOWED, "/index.html");
            //ErrorPage... errorPages 表示不定参数
            factory.addErrorPages(error400Page,error405Page,error404Page);
        };
    }
}
