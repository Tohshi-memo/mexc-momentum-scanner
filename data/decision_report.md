# Decision Report

- generated_at: 2026-09-19T00:21:23.164642+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14964**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.21% / filled 20/20。**
- 全期間 MARKET基準: n=14964, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.21% | **+0.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| MARKET | 20/20 | 100.0% | +0.21% | **+0.21%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.79% | **+1.52%** |
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +1.49% | **+1.24%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.50% | **+1.00%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.68% | **+0.61%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,207.37** / 初期 $100.00 (+1107.37%)
- 確定: 5621件 (Win 1687 / Loss 1820 / Flat 2114) / skip 5904件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $1,207.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$241.67** / 初期 $100.00 (+141.67%)
- 確定: 3173件 (Win 878 / Loss 757 / Flat 1538) / skip 5202件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1523 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $241.67

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.52** / 初期 $100.00 (+23.52%)
- 確定: 2962件 (Win 879 / Loss 1167 / Flat 916) / pending 0件 / skip 3478件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000515 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $123.52

## 6. Latest Market Context

- 更新: 2026-09-19T00:21:12.499905+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=81002.1
- Funnel: target 1050 → liquid 171 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +81.58% | $34,415,490.79 |
| ONE/USDT:USDT | +23.35% | $27,654,700.21 |
| MAGMA/USDT:USDT | +22.37% | $1,179,931.94 |
| SAGA/USDT:USDT | +20.63% | $4,188,189.46 |
| SYN/USDT:USDT | +20.46% | $6,626,117.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| APT/USDT:USDT | below_1h_threshold | +4.39% | +4.22% |
| 4/USDT:USDT | below_1h_threshold | +3.46% | +3.29% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +2.68% | +2.51% |
| ONE/USDT:USDT | below_1h_threshold | +2.52% | +2.35% |
| CROSS/USDT:USDT | below_1h_threshold | +2.34% | +2.17% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
