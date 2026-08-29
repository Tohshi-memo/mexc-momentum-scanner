# Decision Report

- generated_at: 2026-08-29T07:16:27.084005+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12909**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.29% / filled 20/20。**
- 全期間 MARKET基準: n=12909, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.29% | **+2.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.29% | **+2.29%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.20% | **+1.87%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.25% | **+0.81%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.32% | **+0.73%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.36% | **+2.36%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -0.82% | **-0.16%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | -0.18% | **-0.17%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -2.30% | **-0.35%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$712.40** / 初期 $100.00 (+612.40%)
- 確定: 4680件 (Win 1415 / Loss 1535 / Flat 1730) / skip 4790件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TOAD/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $712.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.51** / 初期 $100.00 (+56.51%)
- 確定: 2003件 (Win 544 / Loss 483 / Flat 976) / skip 4317件
- 成長率目線: 平均log +0.000224 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $156.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.14** / 初期 $100.00 (+16.14%)
- 確定: 2005件 (Win 588 / Loss 771 / Flat 646) / pending 3件 / skip 2371件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000348 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TOAD/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $116.14

## 6. Latest Market Context

- 更新: 2026-08-29T07:16:14.292267+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=77421.1
- Funnel: target 1023 → liquid 144 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TOAD/USDT:USDT | +70.64% | $1,266,622.37 |
| HNT/USDT:USDT | +35.18% | $1,459,600.04 |
| BEAT/USDT:USDT | +25.21% | $13,891,012.22 |
| SKR/USDT:USDT | +17.13% | $1,566,759.00 |
| AKE/USDT:USDT | +12.73% | $20,224,052.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +4.86% | +4.88% |
| NIL/USDT:USDT | below_1h_threshold | +4.48% | +4.50% |
| ONG/USDT:USDT | below_1h_threshold | +1.51% | +1.53% |
| SKR/USDT:USDT | below_1h_threshold | +1.32% | +1.34% |
| DOS/USDT:USDT | below_1h_threshold | +1.17% | +1.19% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
