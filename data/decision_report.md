# Decision Report

- generated_at: 2026-08-31T10:31:26.111949+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13163**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +4.38% / filled 20/20。**
- 全期間 MARKET基準: n=13163, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+4.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.38% | **+4.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.38% | **+4.38%** |
| LIMIT_1PCT | 16/20 | 80.0% | +3.61% | **+2.89%** |
| LIMIT_2PCT | 11/20 | 55.0% | +1.71% | **+0.94%** |
| LIMIT_BB3S | 3/14 | 21.4% | +4.00% | **+0.86%** |
| LIMIT_ATR | 6/20 | 30.0% | +2.31% | **+0.69%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 14/20 | 70.0% | +1.24% | **+0.86%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_7PCT_LONG | 14/20 | 70.0% | +0.10% | **+0.07%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -1.14% | **-0.23%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$796.73** / 初期 $100.00 (+696.73%)
- 確定: 4875件 (Win 1485 / Loss 1608 / Flat 1782) / skip 4849件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FONE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $796.73

## 4. Robust Adaptive DryRun ($100)

- 残高: **$173.14** / 初期 $100.00 (+73.14%)
- 確定: 2167件 (Win 601 / Loss 528 / Flat 1038) / skip 4407件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ZORA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $173.14

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.89** / 初期 $100.00 (+15.89%)
- 確定: 2084件 (Win 610 / Loss 812 / Flat 662) / pending 0件 / skip 2549件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000518 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZORA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $115.89

## 6. Latest Market Context

- 更新: 2026-08-31T10:31:18.357914+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=78367.2
- Funnel: target 1028 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKR/USDT:USDT | +43.96% | $47,554,059.19 |
| HEMI/USDT:USDT | +43.60% | $7,504,225.00 |
| BASECAT/USDT:USDT | +40.08% | $1,875,921.17 |
| ZORA/USDT:USDT | +36.12% | $12,810,128.22 |
| FLOCK/USDT:USDT | +25.12% | $1,822,450.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEN/USDT:USDT | below_1h_threshold | +4.54% | +4.69% |
| ZORA/USDT:USDT | below_1h_threshold | +3.33% | +3.48% |
| DASH/USDT:USDT | below_1h_threshold | +2.29% | +2.44% |
| FLOCK/USDT:USDT | below_1h_threshold | +1.24% | +1.39% |
| SOXS/USDT:USDT | below_1h_threshold | +0.96% | +1.11% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
