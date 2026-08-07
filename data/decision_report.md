# Decision Report

- generated_at: 2026-08-07T05:31:24.094732+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10678**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.52% / filled 20/20。**
- 全期間 MARKET基準: n=10678, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.52% | **+2.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.52% | **+2.52%** |
| LIMIT_1PCT | 16/20 | 80.0% | +2.05% | **+1.64%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.75% | **+1.14%** |
| LIMIT_3PCT | 11/20 | 55.0% | +1.24% | **+0.68%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.12% | **+0.64%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +2.76% | **+2.76%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +0.73% | **+0.40%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +0.43% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$595.60** / 初期 $100.00 (+495.60%)
- 確定: 3797件 (Win 1203 / Loss 1250 / Flat 1344) / skip 3442件
- 成長率目線: 平均log +0.000470 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KMNO/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $595.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$144.37** / 初期 $100.00 (+44.37%)
- 確定: 1454件 (Win 406 / Loss 342 / Flat 706) / skip 2635件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AXTISTOCK/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $144.37

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.67** / 初期 $100.00 (+16.67%)
- 確定: 1159件 (Win 371 / Loss 455 / Flat 333) / pending 0件 / skip 993件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000317 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKAMSTOCK/USDT:USDT `MARKET` EXPIRED account +0.09% 残高後 $116.67

## 6. Latest Market Context

- 更新: 2026-08-07T05:31:14.611047+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=64155.4
- Funnel: target 958 → liquid 194 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STG/USDT:USDT | +41.67% | $8,685,063.90 |
| ON/USDT:USDT | +21.23% | $9,490,256.77 |
| ACE/USDT:USDT | +20.03% | $19,250,259.82 |
| ZHIPUSTOCK/USDT:USDT | +18.27% | $1,890,857.94 |
| TWLOSTOCK/USDT:USDT | +17.65% | $1,414,622.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +3.85% | +3.96% |
| HEI/USDT:USDT | below_1h_threshold | +3.55% | +3.66% |
| COOKIE/USDT:USDT | below_1h_threshold | +2.99% | +3.10% |
| BSB/USDT:USDT | below_1h_threshold | +1.69% | +1.79% |
| ALLO/USDT:USDT | below_1h_threshold | +1.41% | +1.52% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
