{{- define "ping.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "hello.name" -}}
{{- default "hello" -}}
{{- end -}}

{{- define "world.name" -}}
{{- default "world" -}}
{{- end -}}