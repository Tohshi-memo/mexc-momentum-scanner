# Decision Report

- generated_at: 2026-08-15T16:41:22.592192+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11682**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11682, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.34% | **+0.27%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.36% | **+0.88%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.61% | **+0.52%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.58% | **+0.29%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.36% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.53** / 初期 $100.00 (+21.53%)
- 確定トレード: 183件 (TP 71 / SL 107 / EXP 5)
- 最新: MOVR/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.53
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$641.37** / 初期 $100.00 (+541.37%)
- 確定: 4150件 (Win 1290 / Loss 1355 / Flat 1505) / skip 4093件
- 成長率目線: 平均log +0.000448 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MOVR/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $641.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.25** / 初期 $100.00 (+55.25%)
- 確定: 1745件 (Win 492 / Loss 413 / Flat 840) / skip 3348件
- 成長率目線: 平均log +0.000252 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0806 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MOVR/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $155.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.13** / 初期 $100.00 (+19.13%)
- 確定: 1618件 (Win 493 / Loss 614 / Flat 511) / pending 5件 / skip 1533件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000476 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MOVR/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $119.13

## 6. Latest Market Context

- 更新: 2026-08-15T16:41:14.044873+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=63063.2
- Funnel: target 985 → liquid 142 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AEON1/USDT:USDT | +10.31% | $1,485,897.11 |
| ROBO/USDT:USDT | +3.36% | $8,738,024.83 |
| SKYAI/USDT:USDT | +2.55% | $8,402,247.75 |
| CAP/USDT:USDT | +1.63% | $21,741,668.39 |
| PRL/USDT:USDT | +1.57% | $2,189,478.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ROBO/USDT:USDT | below_1h_threshold | +3.37% | +3.37% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.55% | +2.56% |
| CAP/USDT:USDT | below_1h_threshold | +1.64% | +1.64% |
| PRL/USDT:USDT | below_1h_threshold | +1.57% | +1.58% |
| ETHFI/USDT:USDT | below_1h_threshold | +1.36% | +1.37% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
