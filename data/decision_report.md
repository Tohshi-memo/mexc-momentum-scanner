# Decision Report

- generated_at: 2026-09-11T19:51:24.303630+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14251**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14251, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.09% | **+0.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| MARKET | 20/20 | 100.0% | +0.09% | **+0.09%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.00% | **+0.00%** |
| LIMIT_2PCT | 15/20 | 75.0% | -0.90% | **-0.68%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.59% | **+2.59%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.83% | **+1.65%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.27% | **+1.27%** |
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.70% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,119.36** / 初期 $100.00 (+1019.36%)
- 確定: 5408件 (Win 1632 / Loss 1749 / Flat 2027) / skip 5404件
- 成長率目線: 平均log +0.000447 / 幾何平均 +0.045% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RIVER/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,119.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$210.13** / 初期 $100.00 (+110.13%)
- 確定: 2823件 (Win 777 / Loss 655 / Flat 1391) / skip 4839件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0430 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RIVER/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $210.13

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.77** / 初期 $100.00 (+24.77%)
- 確定: 2743件 (Win 814 / Loss 1050 / Flat 879) / pending 4件 / skip 2976件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000342 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RIVER/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $124.77

## 6. Latest Market Context

- 更新: 2026-09-11T19:51:13.932728+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.37% price=77306.2
- Funnel: target 1067 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STORJ/USDT:USDT | +39.62% | $10,158,796.97 |
| LAB/USDT:USDT | +17.23% | $7,847,871.04 |
| BEAT/USDT:USDT | +12.62% | $9,684,338.88 |
| RIVER/USDT:USDT | +10.34% | $3,878,340.62 |
| WLFI/USDT:USDT | +3.29% | $13,398,923.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIVER/USDT:USDT | below_relative_strength | +5.03% | +4.66% |
| 4/USDT:USDT | below_1h_threshold | +4.01% | +3.64% |
| STONK/USDT:USDT | below_1h_threshold | +3.35% | +2.98% |
| LSK/USDT:USDT | below_1h_threshold | +3.27% | +2.90% |
| MINA/USDT:USDT | below_1h_threshold | +2.92% | +2.55% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
