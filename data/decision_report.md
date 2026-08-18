# Decision Report

- generated_at: 2026-08-18T17:16:23.288062+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11916**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.02% / filled 20/20。**
- 全期間 MARKET基準: n=11916, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.02% | **+1.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 17/20 | 85.0% | +1.29% | **+1.10%** |
| MARKET | 20/20 | 100.0% | +1.02% | **+1.02%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.92% | **+0.58%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.98% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.84% | **+0.92%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.47% | **+0.89%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.91% | **+0.46%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.19% | **+0.42%** |
| LIMIT_BB3S_LONG | 4/7 | 57.1% | +0.40% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$614.51** / 初期 $100.00 (+514.51%)
- 確定: 4210件 (Win 1295 / Loss 1375 / Flat 1540) / skip 4267件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.19% 残高後 $614.51

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.25** / 初期 $100.00 (+55.25%)
- 確定: 1820件 (Win 502 / Loss 427 / Flat 891) / skip 3507件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0204 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $155.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.31** / 初期 $100.00 (+18.31%)
- 確定: 1722件 (Win 515 / Loss 656 / Flat 551) / pending 2件 / skip 1664件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000251 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $118.31

## 6. Latest Market Context

- 更新: 2026-08-18T17:16:13.399851+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=64760.9
- Funnel: target 993 → liquid 173 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CYS/USDT:USDT | +5.92% | $13,090,778.16 |
| AIO/USDT:USDT | +3.64% | $2,769,878.73 |
| EDEN/USDT:USDT | +3.51% | $4,840,852.65 |
| CHIP/USDT:USDT | +3.26% | $2,179,330.69 |
| BASECAT/USDT:USDT | +2.54% | $1,098,039.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CYS/USDT:USDT | below_1h_threshold | +4.13% | +4.19% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.94% | +2.01% |
| RE/USDT:USDT | below_1h_threshold | +1.93% | +2.00% |
| CHIP/USDT:USDT | below_1h_threshold | +1.18% | +1.24% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +1.05% | +1.12% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
