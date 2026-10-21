# Decision Report

- generated_at: 2026-10-21T04:01:14.290680+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17093**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.92% / filled 20/20。**
- 全期間 MARKET基準: n=17093, expectancy=+0.02%
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
| LIMIT_2PCT | 15/20 | 75.0% | +1.26% | **+0.95%** |
| MARKET | 20/20 | 100.0% | +0.92% | **+0.92%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +3.77% | **+3.77%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.90% | **+1.05%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.58% | **+0.71%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.02% | **+0.66%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.89% | **+0.53%** |

## 2. $100 Live Portfolio

- 残高: **$121.48** / 初期 $100.00 (+21.48%)
- 確定トレード: 249件 (TP 92 / SL 150 / EXP 7)
- 最新: ICNT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.48
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,352.02** / 初期 $100.00 (+1252.02%)
- 確定: 6489件 (Win 1890 / Loss 2071 / Flat 2528) / skip 7165件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SMCISTOCK/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.60% 残高後 $1,352.02

## 4. Robust Adaptive DryRun ($100)

- 残高: **$280.10** / 初期 $100.00 (+180.10%)
- 確定: 3818件 (Win 1050 / Loss 892 / Flat 1876) / skip 6686件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $280.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5252件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000182 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-21T04:01:04.971858+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=82717.8
- Funnel: target 1083 → liquid 163 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOOD/USDT:USDT | +31.46% | $2,297,169.95 |
| IOST/USDT:USDT | +27.47% | $1,836,250.65 |
| ICNT/USDT:USDT | +25.44% | $4,144,257.77 |
| SMCISTOCK/USDT:USDT | +17.81% | $1,333,565.39 |
| AKE/USDT:USDT | +11.36% | $7,091,508.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +0.44% | +0.42% |
| AKE/USDT:USDT | below_1h_threshold | +0.32% | +0.30% |
| LONGXIA/USDT:USDT | below_1h_threshold | +0.23% | +0.21% |
| DNA/USDT:USDT | below_1h_threshold | +0.08% | +0.06% |
| COMP/USDT:USDT | below_1h_threshold | +0.08% | +0.05% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
