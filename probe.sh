# Temporary workaround until a comprehensive test suit is added

BASE_URL="http://localhost:8000"
ENDPOINTS=("/health" "/healthz" "/docs" "/api/v2/users")

echo "Starting health checks for $BASE_URL..."
echo "------------------------------------------"

for endpoint in "${ENDPOINTS[@]}"; do
    TARGET="$BASE_URL$endpoint"

    # Perform the curl request
    # -s: Silent mode
    # -o /dev/null: Discard the response body
    # -w "%{http_code}": Print only the HTTP status code
    STATUS=$(curl -s -o /dev/null -w "%{http_code}" "$TARGET")

    echo "Endpoint: $TARGET | Status: $STATUS"
done

echo "------------------------------------------"
echo "Checks complete."
