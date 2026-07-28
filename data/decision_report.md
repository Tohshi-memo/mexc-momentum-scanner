# Decision Report

- generated_at: 2026-07-28T19:31:34.451353+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9721**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9721, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.13% | **-1.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +4.88% | **+1.22%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.66% | **+0.83%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.72% | **+0.25%** |
| LIMIT_BB3S | 12/18 | 66.7% | +0.16% | **+0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.09% | **+1.78%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.88% | **+1.13%** |
| LIMIT_5PCT_LONG | 6/20 | 30.0% | +2.42% | **+0.73%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.61% | **+0.73%** |
| MARKET_LONG | 20/20 | 100.0% | +0.71% | **+0.71%** |

## 2. $100 Live Portfolio

- 残高: **$107.44** / 初期 $100.00 (+7.44%)
- 確定トレード: 150件 (TP 52 / SL 93 / EXP 5)
- 最新: DEXE/USDT:USDT TP_HIT PnL +8.00% 残高後 $107.44
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$499.24** / 初期 $100.00 (+399.24%)
- 確定: 3491件 (Win 1105 / Loss 1132 / Flat 1254) / skip 2791件
- 成長率目線: 平均log +0.000461 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ON/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $499.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1226件 (Win 338 / Loss 275 / Flat 613) / skip 1906件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1214 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SPCXSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.13** / 初期 $100.00 (+10.13%)
- 確定: 739件 (Win 240 / Loss 281 / Flat 218) / pending 5件 / skip 450件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000464 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ON/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $110.13

## 6. Latest Market Context

- 更新: 2026-07-28T19:31:25.325164+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=63831.2
- Funnel: target 904 → liquid 173 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.6 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +34.96% | $1,330,405.30 |
| ON/USDT:USDT | +29.20% | $32,563,789.29 |
| BTW/USDT:USDT | +14.39% | $5,804,218.20 |
| RIF/USDT:USDT | +13.23% | $4,963,824.70 |
| BULLA/USDT:USDT | +9.62% | $2,929,689.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KAITO/USDT:USDT | below_1h_threshold | +4.53% | +4.34% |
| RAVE/USDT:USDT | below_1h_threshold | +3.90% | +3.71% |
| ACH/USDT:USDT | below_1h_threshold | +2.91% | +2.73% |
| RIF/USDT:USDT | below_1h_threshold | +2.27% | +2.08% |
| SNXX/USDT:USDT | below_1h_threshold | +1.55% | +1.36% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
