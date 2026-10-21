# Decision Report

- generated_at: 2026-10-21T04:46:09.364924+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17094**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.92% / filled 20/20。**
- 全期間 MARKET基準: n=17094, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.92% | **+0.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +2.04% | **+1.94%** |
| LIMIT_ATR | 15/20 | 75.0% | +2.23% | **+1.67%** |
| LIMIT_3PCT | 13/20 | 65.0% | +2.33% | **+1.51%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.68% | **+1.35%** |
| MARKET | 20/20 | 100.0% | +0.92% | **+0.92%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +3.77% | **+3.77%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +2.82% | **+1.55%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +2.59% | **+1.16%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.02% | **+0.66%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$121.48** / 初期 $100.00 (+21.48%)
- 確定トレード: 249件 (TP 92 / SL 150 / EXP 7)
- 最新: ICNT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.48
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,352.02** / 初期 $100.00 (+1252.02%)
- 確定: 6489件 (Win 1890 / Loss 2071 / Flat 2528) / skip 7166件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SMCISTOCK/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.60% 残高後 $1,352.02

## 4. Robust Adaptive DryRun ($100)

- 残高: **$280.10** / 初期 $100.00 (+180.10%)
- 確定: 3818件 (Win 1050 / Loss 892 / Flat 1876) / skip 6687件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $280.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5252件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000248 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-21T04:45:59.896102+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=82762.9
- Funnel: target 1084 → liquid 166 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOOD/USDT:USDT | +27.40% | $2,435,916.36 |
| ICNT/USDT:USDT | +27.33% | $4,399,323.10 |
| SMCISTOCK/USDT:USDT | +17.72% | $1,346,745.32 |
| BTW/USDT:USDT | +12.29% | $27,160,205.18 |
| AKE/USDT:USDT | +11.08% | $7,259,415.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DNA/USDT:USDT | below_1h_threshold | +2.25% | +2.17% |
| PYTH/USDT:USDT | below_1h_threshold | +1.68% | +1.60% |
| BTW/USDT:USDT | below_1h_threshold | +1.48% | +1.40% |
| ENA/USDT:USDT | below_1h_threshold | +0.85% | +0.77% |
| W/USDT:USDT | below_1h_threshold | +0.79% | +0.71% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
