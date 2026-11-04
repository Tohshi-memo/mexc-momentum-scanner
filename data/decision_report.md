# Decision Report

- generated_at: 2026-11-04T05:42:23.799663+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18106**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.06% / filled 20/20。**
- 全期間 MARKET基準: n=18106, expectancy=+0.03%
- 直近20件 MARKET基準: n=20, expectancy=+2.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.06% | **+2.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.06% | **+2.06%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.90% | **+1.71%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.36% | **+1.02%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.99% | **+0.64%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.06% | **+0.64%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +4.21% | **+4.21%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.57% | **+0.57%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.07% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 262件 (TP 96 / SL 158 / EXP 8)
- 最新: SOXS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,506.22** / 初期 $100.00 (+1406.22%)
- 確定: 6927件 (Win 2004 / Loss 2222 / Flat 2701) / skip 7740件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JCT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,506.22

## 4. Robust Adaptive DryRun ($100)

- 残高: **$378.25** / 初期 $100.00 (+278.25%)
- 確定: 4520件 (Win 1211 / Loss 1009 / Flat 2300) / skip 6997件
- 成長率目線: 平均log +0.000294 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0367 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JCT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $378.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6268件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000139 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-04T05:42:12.724226+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.44% price=77700.2
- Funnel: target 1085 → liquid 174 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLANKER/USDT:USDT | +34.56% | $2,176,298.37 |
| BMT/USDT:USDT | +16.82% | $1,461,718.41 |
| LSK/USDT:USDT | +10.38% | $2,130,846.89 |
| IDOL/USDT:USDT | +8.52% | $9,875,641.31 |
| AXIS/USDT:USDT | +5.64% | $1,404,206.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PONS/USDT:USDT | below_1h_threshold | +4.28% | +3.84% |
| SPX/USDT:USDT | below_1h_threshold | +2.52% | +2.08% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +2.48% | +2.03% |
| BMT/USDT:USDT | below_1h_threshold | +2.25% | +1.81% |
| STX/USDT:USDT | below_1h_threshold | +2.15% | +1.71% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
