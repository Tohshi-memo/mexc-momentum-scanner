# Decision Report

- generated_at: 2026-07-14T23:56:09.322067+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8706**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.14% / filled 20/20。**
- 全期間 MARKET基準: n=8706, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.14% | **+1.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.14% | **+1.14%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/7 | 100.0% | +1.45% | **+1.45%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.95% | **+0.44%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.62% | **+0.28%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.30% | **+0.21%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$103.22** / 初期 $100.00 (+3.22%)
- 確定トレード: 96件 (TP 33 / SL 61 / EXP 2)
- 最新: LAB/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.22
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$329.76** / 初期 $100.00 (+229.76%)
- 確定: 2863件 (Win 894 / Loss 931 / Flat 1038) / skip 2404件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VANRY/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $329.76

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.12** / 初期 $100.00 (+5.12%)
- 確定: 694件 (Win 161 / Loss 163 / Flat 370) / skip 1423件
- 成長率目線: 平均log +0.000072 / 幾何平均 +0.007% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DODO/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $105.12

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.75** / 初期 $100.00 (-1.25%)
- 確定: 60件 (Win 19 / Loss 39 / Flat 2) / pending 0件 / skip 116件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000116 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AEHRSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $98.75

## 6. Latest Market Context

- 更新: 2026-07-14T23:56:03.113812+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.25% price=65001.3
- Funnel: target 862 → liquid 163 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AEHRSTOCK/USDT:USDT | +31.19% | $2,889,146.62 |
| DODO/USDT:USDT | +21.90% | $3,770,617.63 |
| VELVET/USDT:USDT | +11.57% | $32,377,345.26 |
| US/USDT:USDT | +6.45% | $1,780,511.42 |
| POETSTOCK/USDT:USDT | +6.45% | $7,351,173.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DODO/USDT:USDT | below_relative_strength | +5.13% | +4.88% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +2.13% | +1.87% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.88% | +1.63% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +1.63% | +1.38% |
| ZEC/USDT:USDT | below_1h_threshold | +1.51% | +1.25% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
