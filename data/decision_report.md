# Decision Report

- generated_at: 2026-07-30T08:56:13.481089+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9873**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +4.80% / filled 20/20。**
- 全期間 MARKET基準: n=9873, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+4.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.80% | **+4.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.80% | **+4.80%** |
| LIMIT_1PCT | 14/20 | 70.0% | +4.52% | **+3.16%** |
| LIMIT_2PCT | 10/20 | 50.0% | +4.73% | **+2.36%** |
| LIMIT_3PCT | 6/20 | 30.0% | +4.15% | **+1.24%** |
| LIMIT_ATR | 8/20 | 40.0% | +3.01% | **+1.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +1.38% | **+1.10%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +0.71% | **+0.21%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.25% | **+0.07%** |
| LIMIT_8PCT_LONG | 12/20 | 60.0% | -0.33% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 170件 (TP 67 / SL 98 / EXP 5)
- 最新: LASERTECSTOCK/USDT:USDT TP_HIT PnL +3.98% 残高後 $121.65
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$494.05** / 初期 $100.00 (+394.05%)
- 確定: 3519件 (Win 1113 / Loss 1147 / Flat 1259) / skip 2915件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $494.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$136.91** / 初期 $100.00 (+36.91%)
- 確定: 1242件 (Win 344 / Loss 283 / Flat 615) / skip 2042件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $136.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$112.22** / 初期 $100.00 (+12.22%)
- 確定: 779件 (Win 256 / Loss 300 / Flat 223) / pending 1件 / skip 562件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.001151 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESP/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $112.22

## 6. Latest Market Context

- 更新: 2026-07-30T08:56:06.452326+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.45% price=64266.8
- Funnel: target 916 → liquid 186 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESP/USDT:USDT | +21.75% | $2,179,187.22 |
| MMT/USDT:USDT | +16.62% | $1,194,899.62 |
| MSFU/USDT:USDT | +14.51% | $2,882,871.95 |
| ADVANTESTSTOCK/USDT:USDT | +11.17% | $1,299,305.05 |
| US/USDT:USDT | +8.74% | $1,898,390.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESP/USDT:USDT | below_1h_threshold | +4.73% | +4.29% |
| SPX/USDT:USDT | below_1h_threshold | +1.73% | +1.28% |
| ZIL/USDT:USDT | below_1h_threshold | +1.71% | +1.26% |
| MMT/USDT:USDT | below_1h_threshold | +1.60% | +1.15% |
| QXOSTOCK/USDT:USDT | below_1h_threshold | +1.12% | +0.67% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
