# Decision Report

- generated_at: 2026-08-29T05:36:17.798931+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12901**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.74% / filled 20/20。**
- 全期間 MARKET基準: n=12901, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.74%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.74% | **+2.74%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.74% | **+2.74%** |
| LIMIT_1PCT | 16/20 | 80.0% | +2.39% | **+1.91%** |
| LIMIT_2PCT | 12/20 | 60.0% | +1.72% | **+1.03%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.78% | **+0.84%** |
| LIMIT_BB3S | 5/17 | 29.4% | +2.54% | **+0.75%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.56% | **+0.56%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +0.65% | **+0.39%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.49% | **+0.22%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.34% | **+0.15%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -0.35% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 193件 (TP 73 / SL 115 / EXP 5)
- 最新: AKE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$708.89** / 初期 $100.00 (+608.89%)
- 確定: 4677件 (Win 1414 / Loss 1534 / Flat 1729) / skip 4785件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MOVR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $708.89

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.51** / 初期 $100.00 (+56.51%)
- 確定: 2003件 (Win 544 / Loss 483 / Flat 976) / skip 4309件
- 成長率目線: 平均log +0.000224 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $156.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.96** / 初期 $100.00 (+15.96%)
- 確定: 1997件 (Win 585 / Loss 766 / Flat 646) / pending 4件 / skip 2371件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000453 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MAGMA/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $115.96

## 6. Latest Market Context

- 更新: 2026-08-29T05:36:08.716516+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=77609.0
- Funnel: target 1023 → liquid 146 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TOAD/USDT:USDT | +57.11% | $1,089,318.89 |
| BEAT/USDT:USDT | +14.52% | $9,249,315.85 |
| MAGMA/USDT:USDT | +12.65% | $11,921,581.55 |
| AKE/USDT:USDT | +11.99% | $20,721,131.44 |
| TRUMPOFFICIAL/USDT:USDT | +11.04% | $56,439,375.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +4.82% | +4.83% |
| BEAT/USDT:USDT | below_1h_threshold | +4.04% | +4.05% |
| LONGXIA/USDT:USDT | below_1h_threshold | +1.28% | +1.29% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +1.07% | +1.08% |
| ICP/USDT:USDT | below_1h_threshold | +0.70% | +0.72% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
