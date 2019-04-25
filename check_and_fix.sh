echo "RUNNING CONFIGURATION COMPLIANCE CHECK"
java -jar conform.jar project.prj
echo "COMPLIANCE CHECK RESULT:"
cat testing
echo "FIXING THE CONFIGURATION"
python3 fix.py
