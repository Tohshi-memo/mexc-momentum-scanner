# Decision Report

- generated_at: 2026-08-02T13:11:21.171832+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10161**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.48% / filled 20/20。**
- 全期間 MARKET基準: n=10161, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.48% | **+2.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.48% | **+2.48%** |
| LIMIT_1PCT | 18/20 | 90.0% | +2.20% | **+1.98%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +4.06% | **+1.42%** |
| LIMIT_2PCT | 12/20 | 60.0% | +2.02% | **+1.21%** |
| LIMIT_3PCT | 10/20 | 50.0% | +1.42% | **+0.71%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +3.38% | **+0.84%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.29% | **+0.20%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.08% | **+0.02%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | -0.13% | **-0.04%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | -0.40% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$566.31** / 初期 $100.00 (+466.31%)
- 確定: 3674件 (Win 1166 / Loss 1205 / Flat 1303) / skip 3048件
- 成長率目線: 平均log +0.000472 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $566.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.31** / 初期 $100.00 (+40.31%)
- 確定: 1281件 (Win 359 / Loss 298 / Flat 624) / skip 2291件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0089 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $140.31

## 5. Causal Adaptive DryRun ($100)

- 残高: **$112.32** / 初期 $100.00 (+12.32%)
- 確定: 966件 (Win 306 / Loss 378 / Flat 282) / pending 3件 / skip 663件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000127 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CAP/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $112.32

## 6. Latest Market Context

- 更新: 2026-08-02T13:11:15.220738+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=63086.5
- Funnel: target 922 → liquid 132 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +55.11% | $19,735,255.85 |
| HOME/USDT:USDT | +29.31% | $4,534,360.32 |
| UAI/USDT:USDT | +25.49% | $26,918,343.15 |
| HYPER/USDT:USDT | +19.68% | $1,746,970.19 |
| MANTRA/USDT:USDT | +15.66% | $1,094,395.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MANTRA/USDT:USDT | below_1h_threshold | +1.75% | +1.77% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.64% | +1.66% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.46% | +1.47% |
| HYPER/USDT:USDT | below_1h_threshold | +1.28% | +1.30% |
| UNI/USDT:USDT | below_1h_threshold | +0.89% | +0.90% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
