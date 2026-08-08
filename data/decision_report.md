# Decision Report

- generated_at: 2026-08-08T03:21:25.817051+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10796**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.38% / filled 20/20。**
- 全期間 MARKET基準: n=10796, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.38% | **+1.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.38% | **+1.38%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.45% | **+0.38%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.39% | **+0.31%** |
| LIMIT_8PCT | 6/20 | 30.0% | +0.57% | **+0.17%** |
| LIMIT_7PCT | 6/20 | 30.0% | +0.27% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +4.23% | **+1.27%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +0.62% | **+0.34%** |
| LIMIT_9PCT_LONG | 8/20 | 40.0% | +0.75% | **+0.30%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.05% | **+0.02%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | -0.20% | **-0.11%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$595.60** / 初期 $100.00 (+495.60%)
- 確定: 3800件 (Win 1203 / Loss 1250 / Flat 1347) / skip 3557件
- 成長率目線: 平均log +0.000470 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $595.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.00** / 初期 $100.00 (+42.00%)
- 確定: 1510件 (Win 424 / Loss 360 / Flat 726) / skip 2697件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0295 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $142.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.02** / 初期 $100.00 (+18.02%)
- 確定: 1182件 (Win 381 / Loss 468 / Flat 333) / pending 0件 / skip 1085件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000075 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AXTISTOCK/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $118.02

## 6. Latest Market Context

- 更新: 2026-08-08T03:21:15.035605+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=64966.5
- Funnel: target 961 → liquid 180 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +168.94% | $4,749,013.65 |
| BLESS/USDT:USDT | +34.26% | $93,310,045.99 |
| MMT/USDT:USDT | +17.46% | $1,281,599.91 |
| EPIC/USDT:USDT | +15.64% | $2,479,635.57 |
| BSB/USDT:USDT | +14.82% | $2,865,098.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RBRKSTOCK/USDT:USDT | below_1h_threshold | +4.20% | +4.09% |
| BSB/USDT:USDT | below_1h_threshold | +1.93% | +1.81% |
| CAP/USDT:USDT | below_1h_threshold | +1.72% | +1.60% |
| ONDO/USDT:USDT | below_1h_threshold | +0.83% | +0.71% |
| WLD/USDT:USDT | below_1h_threshold | +0.55% | +0.43% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
