# Decision Report

- generated_at: 2026-05-14T11:38:13.751195+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4285**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4285, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=+0.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.13% | **+0.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/12 | 50.0% | +5.18% | **+2.59%** |
| LIMIT_ATR | 16/20 | 80.0% | +1.41% | **+1.13%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +3.24% | **+2.32%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.08% | **+0.83%** |
| MARKET_LONG | 20/20 | 100.0% | +0.62% | **+0.62%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.28% | **+0.33%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.55% | **+0.19%** |

## 2. $100 Live Portfolio

- 残高: **$96.73** / 初期 $100.00 (-3.27%)
- 確定トレード: 42件 (TP 10 / SL 29 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.73
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.18** / 初期 $100.00 (+19.18%)
- 確定: 344件 (Win 94 / Loss 125 / Flat 125) / skip 502件
- 成長率目線: 平均log +0.000510 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GIGA/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $119.18

## 4. Latest Market Context

- 更新: 2026-05-14T11:38:10.148404+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.25% price=79328.0
- Funnel: target 763 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIGENSYN/USDT:USDT | +63.12% | $5,516,841.74 |
| UP/USDT:USDT | +28.09% | $1,788,955.56 |
| TROLLSOL/USDT:USDT | +25.99% | $2,231,543.51 |
| CSCOSTOCK/USDT:USDT | +18.81% | $5,529,293.46 |
| PIEVERSE/USDT:USDT | +17.05% | $2,577,983.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIGENSYN/USDT:USDT | below_1h_threshold | +4.10% | +4.36% |
| UB/USDT:USDT | below_1h_threshold | +1.74% | +2.00% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +0.98% | +1.23% |
| RIVER/USDT:USDT | below_1h_threshold | +0.63% | +0.88% |
| RAVE/USDT:USDT | below_1h_threshold | +0.37% | +0.62% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
