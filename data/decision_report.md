# Decision Report

- generated_at: 2026-07-03T11:47:59.487310+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8157**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.04% / filled 20/20。**
- 全期間 MARKET基準: n=8157, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.04% | **+1.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.04% | **+1.04%** |
| ASK | 20/20 | 100.0% | +1.04% | **+1.04%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.20% | **+0.17%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.35% | **+0.35%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | -0.03% | **-0.01%** |
| ASK_LONG | 20/20 | 100.0% | -0.05% | **-0.05%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | -0.55% | **-0.25%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.66% | **-0.30%** |

## 2. $100 Live Portfolio

- 残高: **$102.11** / 初期 $100.00 (+2.11%)
- 確定トレード: 54件 (TP 19 / SL 34 / EXP 1)
- 最新: SKHYNIXSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.11
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$288.02** / 初期 $100.00 (+188.02%)
- 確定: 2478件 (Win 762 / Loss 826 / Flat 890) / skip 2240件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ARPA/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $288.02

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.39** / 初期 $100.00 (+6.39%)
- 確定: 603件 (Win 145 / Loss 143 / Flat 315) / skip 965件
- 成長率目線: 平均log +0.000103 / 幾何平均 +0.010% per trade / maxDD +3.57%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score -0.0084 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ARPA/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $106.39

## 5. Latest Market Context

- 更新: 2026-07-03T11:47:50.402531+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=61942.5
- Funnel: target 834 → liquid 165 → pre 50 → checked 50 → surge 5 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.5 >= 65=1, 4h RSI 70.7 >= 65=1, 4h RSI 66.1 >= 65=1, 4h RSI 67.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARPA/USDT:USDT | +60.64% | $3,788,822.54 |
| NEX/USDT:USDT | +48.94% | $2,630,558.41 |
| RIF/USDT:USDT | +40.58% | $8,473,525.51 |
| ZKP/USDT:USDT | +27.80% | $4,630,226.00 |
| BLESS/USDT:USDT | +27.17% | $6,190,469.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MAGMA/USDT:USDT | below_1h_threshold | +4.36% | +4.27% |
| RIVER/USDT:USDT | below_1h_threshold | +3.04% | +2.95% |
| XPL/USDT:USDT | below_1h_threshold | +2.16% | +2.07% |
| PEPE/USDT:USDT | below_1h_threshold | +2.06% | +1.97% |
| BLESS/USDT:USDT | below_1h_threshold | +1.76% | +1.67% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
