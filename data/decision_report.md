# Decision Report

- generated_at: 2026-07-12T19:06:12.981093+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8606**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.61% / filled 20/20。**
- 全期間 MARKET基準: n=8606, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.61%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.61% | **+2.61%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +3.28% | **+3.12%** |
| MARKET | 20/20 | 100.0% | +2.61% | **+2.61%** |
| LIMIT_2PCT | 15/20 | 75.0% | +2.64% | **+1.98%** |
| LIMIT_3PCT | 11/20 | 55.0% | +1.64% | **+0.90%** |
| LIMIT_BB3S | 5/13 | 38.5% | +0.67% | **+0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +1.53% | **+1.00%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +1.12% | **+0.73%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.26% | **+0.14%** |

## 2. $100 Live Portfolio

- 残高: **$101.71** / 初期 $100.00 (+1.71%)
- 確定トレード: 90件 (TP 30 / SL 58 / EXP 2)
- 最新: PIPPIN/USDT:USDT SL_HIT PnL -2.19% 残高後 $101.71
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$319.81** / 初期 $100.00 (+219.81%)
- 確定: 2785件 (Win 875 / Loss 922 / Flat 988) / skip 2382件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $319.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 644件 (Win 152 / Loss 159 / Flat 333) / skip 1373件
- 成長率目線: 平均log +0.000077 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VANRY/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $105.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定: 27件 (Win 9 / Loss 18 / Flat 0) / pending 0件 / skip 50件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000260 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $99.00

## 6. Latest Market Context

- 更新: 2026-07-12T19:06:06.769453+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=64159.6
- Funnel: target 863 → liquid 130 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PIPPIN/USDT:USDT | +10.47% | $3,601,466.93 |
| ALLO/USDT:USDT | +4.37% | $15,860,288.95 |
| UB/USDT:USDT | +4.32% | $1,014,012.20 |
| BILL/USDT:USDT | +3.80% | $6,570,044.52 |
| CAP/USDT:USDT | +3.56% | $1,095,109.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +1.53% | +1.47% |
| KORU/USDT:USDT | below_1h_threshold | +0.85% | +0.80% |
| T/USDT:USDT | below_1h_threshold | +0.75% | +0.70% |
| FHE/USDT:USDT | below_1h_threshold | +0.60% | +0.55% |
| BXSTOCK/USDT:USDT | below_1h_threshold | +0.52% | +0.46% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
