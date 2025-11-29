                          
.PHONY: precommit install_dev_dependencies
                          

                          
# Install dev dependencies
                          
install_dev_dependencies:
                          
	uv pip sync --extra lint --extra test --extra dev
                          

                          
# Local precommit
                          
precommit:
                          
	bash ./precommit.sh
                          
                                                                                                                                       