# Decision Report

- generated_at: 2026-07-03T12:26:39.262223+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8159**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.64% / filled 20/20。**
- 全期間 MARKET基準: n=8159, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.64%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.64% | **+1.64%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.64% | **+1.64%** |
| ASK | 20/20 | 100.0% | +1.59% | **+1.59%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.52% | **+0.42%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.96% | **+0.29%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.10% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | -0.05% | **-0.05%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | -0.24% | **-0.12%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | -0.55% | **-0.25%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -2.30% | **-0.35%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.71% | **-0.35%** |

## 2. $100 Live Portfolio

- 残高: **$102.11** / 初期 $100.00 (+2.11%)
- 確定トレード: 54件 (TP 19 / SL 34 / EXP 1)
- 最新: SKHYNIXSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.11
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$288.01** / 初期 $100.00 (+188.01%)
- 確定: 2480件 (Win 763 / Loss 827 / Flat 890) / skip 2240件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ARPA/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $288.01

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.01** / 初期 $100.00 (+6.01%)
- 確定: 605件 (Win 145 / Loss 144 / Flat 316) / skip 965件
- 成長率目線: 平均log +0.000097 / 幾何平均 +0.010% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ARPA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $106.01

## 5. Latest Market Context

- 更新: 2026-07-03T12:26:34.163262+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=61939.5
- Funnel: target 834 → liquid 166 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARPA/USDT:USDT | +48.44% | $4,527,292.76 |
| NEX/USDT:USDT | +46.78% | $2,769,713.47 |
| RIF/USDT:USDT | +39.47% | $8,936,543.93 |
| ZKP/USDT:USDT | +28.06% | $5,270,949.33 |
| BLESS/USDT:USDT | +26.64% | $6,594,275.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| US/USDT:USDT | below_1h_threshold | +4.15% | +4.24% |
| XPL/USDT:USDT | below_1h_threshold | +2.37% | +2.45% |
| TIA/USDT:USDT | below_1h_threshold | +1.51% | +1.60% |
| RIVER/USDT:USDT | below_1h_threshold | +1.16% | +1.25% |
| ALLO/USDT:USDT | below_1h_threshold | +1.08% | +1.17% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
