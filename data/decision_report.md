# Decision Report

- generated_at: 2026-07-29T02:41:13.869844+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9754**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +4.89% / filled 20/20。**
- 全期間 MARKET基準: n=9754, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+4.89%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.89% | **+4.89%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.89% | **+4.89%** |
| LIMIT_1PCT | 15/20 | 75.0% | +4.92% | **+3.69%** |
| LIMIT_2PCT | 12/20 | 60.0% | +4.49% | **+2.69%** |
| LIMIT_ATR | 11/20 | 55.0% | +3.96% | **+2.18%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +3.63% | **+1.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_8PCT_LONG | 13/20 | 65.0% | +0.00% | **+0.00%** |
| LIMIT_7PCT_LONG | 16/20 | 80.0% | -0.36% | **-0.29%** |
| LIMIT_FIB1618_LONG | 9/20 | 45.0% | -1.83% | **-0.82%** |
| LIMIT_6PCT_LONG | 16/20 | 80.0% | -1.46% | **-1.17%** |

## 2. $100 Live Portfolio

- 残高: **$116.35** / 初期 $100.00 (+16.35%)
- 確定トレード: 158件 (TP 60 / SL 93 / EXP 5)
- 最新: DRAM/USDT:USDT TP_HIT PnL +7.69% 残高後 $116.35
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$494.05** / 初期 $100.00 (+394.05%)
- 確定: 3519件 (Win 1113 / Loss 1147 / Flat 1259) / skip 2796件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $494.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1226件 (Win 338 / Loss 275 / Flat 613) / skip 1939件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0229 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SPCXSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.36** / 初期 $100.00 (+10.36%)
- 確定: 759件 (Win 246 / Loss 290 / Flat 223) / pending 1件 / skip 467件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000372 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $110.36

## 6. Latest Market Context

- 更新: 2026-07-29T02:41:07.100372+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.67% price=64108.5
- Funnel: target 904 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=2, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +25.03% | $1,258,552.17 |
| BTW/USDT:USDT | +16.87% | $6,247,349.17 |
| BEAT/USDT:USDT | +13.22% | $45,804,716.98 |
| KAITO/USDT:USDT | +13.00% | $9,681,576.96 |
| ZIL/USDT:USDT | +8.19% | $8,817,657.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JIMOTHY/USDT:USDT | below_relative_strength | +5.58% | +4.91% |
| SOXS/USDT:USDT | below_relative_strength | +5.39% | +4.72% |
| BTW/USDT:USDT | below_1h_threshold | +3.26% | +2.59% |
| KAITO/USDT:USDT | below_1h_threshold | +3.11% | +2.44% |
| TAG/USDT:USDT | below_1h_threshold | +2.85% | +2.18% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
