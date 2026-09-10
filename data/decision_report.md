# Decision Report

- generated_at: 2026-09-10T14:26:24.921701+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14167**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.55% / filled 20/20。**
- 全期間 MARKET基準: n=14167, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.55% | **+0.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.32% | **+1.26%** |
| LIMIT_ATR | 9/20 | 45.0% | +2.61% | **+1.18%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.62% | **+0.73%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.14% | **+0.57%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.04% | **+0.47%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,047.54** / 初期 $100.00 (+947.54%)
- 確定: 5347件 (Win 1607 / Loss 1727 / Flat 2013) / skip 5381件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SPCXSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.34% 残高後 $1,047.54

## 4. Robust Adaptive DryRun ($100)

- 残高: **$206.86** / 初期 $100.00 (+106.86%)
- 確定: 2761件 (Win 762 / Loss 648 / Flat 1351) / skip 4817件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0985 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SPCXSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.27% 残高後 $206.86

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.64** / 初期 $100.00 (+21.64%)
- 確定: 2672件 (Win 787 / Loss 1021 / Flat 864) / pending 5件 / skip 2962件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000265 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SPCXSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.14% 残高後 $121.64

## 6. Latest Market Context

- 更新: 2026-09-10T14:26:11.761087+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.25% price=77331.1
- Funnel: target 1065 → liquid 172 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VTHO/USDT:USDT | +50.55% | $9,323,450.31 |
| CATE/USDT:USDT | +30.98% | $2,777,859.29 |
| NES/USDT:USDT | +21.79% | $1,600,888.71 |
| ETHFI/USDT:USDT | +9.13% | $5,090,808.29 |
| SOXS/USDT:USDT | +6.28% | $23,726,911.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ETHFI/USDT:USDT | below_1h_threshold | +4.81% | +4.56% |
| EGLD/USDT:USDT | below_1h_threshold | +2.86% | +2.61% |
| ROBINHOOD/USDT:USDT | below_1h_threshold | +2.31% | +2.06% |
| COTI/USDT:USDT | below_1h_threshold | +2.22% | +1.97% |
| RE/USDT:USDT | below_1h_threshold | +1.90% | +1.65% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
