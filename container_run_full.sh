docker run -d -p 8080-8082:8080-8082                   \
-e "ADVERTISED_HOST=localhost"                         \
-e "OBP_API_HOSTNAME=http://127.0.0.1:8080"            \
-e "OBP_BASE_URL_API_EXPLORER=http://localhost:8082"   \
-e "OBP_BASE_URL_SOCIAL_FINANCE=http://localhost:8081" \
-e "OBP_WEBUI_API_EXPLORER_URL=http://localhost:8082"  \
openbankproject/obp-full
