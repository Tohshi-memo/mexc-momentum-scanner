# Decision Report

- generated_at: 2026-08-02T16:21:32.127459+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10173**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.49% / filled 20/20。**
- 全期間 MARKET基準: n=10173, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.49% | **+0.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +1.15% | **+0.92%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.74% | **+0.52%** |
| LIMIT_5PCT | 3/20 | 15.0% | +3.30% | **+0.50%** |
| MARKET | 20/20 | 100.0% | +0.49% | **+0.49%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.52% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.04% | **+0.47%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.16% | **+0.43%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.43% | **+0.34%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$566.31** / 初期 $100.00 (+466.31%)
- 確定: 3674件 (Win 1166 / Loss 1205 / Flat 1303) / skip 3060件
- 成長率目線: 平均log +0.000472 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $566.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.31** / 初期 $100.00 (+40.31%)
- 確定: 1281件 (Win 359 / Loss 298 / Flat 624) / skip 2303件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $140.31

## 5. Causal Adaptive DryRun ($100)

- 残高: **$112.22** / 初期 $100.00 (+12.22%)
- 確定: 969件 (Win 307 / Loss 380 / Flat 282) / pending 0件 / skip 672件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000170 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $112.22

## 6. Latest Market Context

- 更新: 2026-08-02T16:21:22.120143+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=63057.6
- Funnel: target 922 → liquid 127 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 1000RATS/USDT:USDT | +4.53% | $36,765,393.29 |
| US/USDT:USDT | +3.66% | $2,478,239.72 |
| BLESS/USDT:USDT | +3.52% | $30,581,696.08 |
| COTI/USDT:USDT | +2.98% | $2,100,207.58 |
| GIGGLE/USDT:USDT | +1.82% | $8,453,248.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 1000RATS/USDT:USDT | below_1h_threshold | +4.54% | +4.57% |
| BLESS/USDT:USDT | below_1h_threshold | +3.81% | +3.85% |
| US/USDT:USDT | below_1h_threshold | +3.67% | +3.70% |
| COTI/USDT:USDT | below_1h_threshold | +2.92% | +2.96% |
| GIGGLE/USDT:USDT | below_1h_threshold | +1.95% | +1.98% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
