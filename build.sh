#!/bin/sh
echo "Executing the fact extractor based on predicates"
cd eipl_predicates/ && sh build.sh && cd ..

echo "\n\nExecuting the fact extractor based on the listener"
cd eipl_listener/ && sh build.sh && cd ..

echo "\n\nExecuting the fact extractor based on the visitor"
cd eipl_visitor/ && sh build.sh && cd ..

