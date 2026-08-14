# Decision Report

- generated_at: 2026-08-14T14:21:25.584982+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11560**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.46% / filled 20/20。**
- 全期間 MARKET基準: n=11560, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.46% | **+1.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.46% | **+1.46%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.39% | **+1.18%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.46% | **+1.02%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.08% | **+0.97%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.10% | **+0.66%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.33% | **+0.82%** |
| LIMIT_9PCT_LONG | 8/20 | 40.0% | +1.32% | **+0.53%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.80% | **+0.48%** |
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +0.62% | **+0.41%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$623.06** / 初期 $100.00 (+523.06%)
- 確定: 4028件 (Win 1263 / Loss 1325 / Flat 1440) / skip 4093件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AAOISTOCK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $623.06

## 4. Robust Adaptive DryRun ($100)

- 残高: **$149.41** / 初期 $100.00 (+49.41%)
- 確定: 1651件 (Win 471 / Loss 398 / Flat 782) / skip 3320件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0169 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $149.41

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.49** / 初期 $100.00 (+17.49%)
- 確定: 1520件 (Win 460 / Loss 579 / Flat 481) / pending 5件 / skip 1508件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000219 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AAOISTOCK/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $117.49

## 6. Latest Market Context

- 更新: 2026-08-14T14:21:16.452713+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=62575.7
- Funnel: target 985 → liquid 177 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.0 >= 65=1, 4h RSI 91.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACE/USDT:USDT | +138.76% | $38,115,419.58 |
| AKE/USDT:USDT | +74.11% | $68,074,130.64 |
| CAP/USDT:USDT | +36.49% | $5,762,233.98 |
| CROSS/USDT:USDT | +34.84% | $1,848,386.88 |
| VELVET/USDT:USDT | +26.71% | $38,826,256.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| APR/USDT:USDT | below_1h_threshold | +3.88% | +3.98% |
| CAP/USDT:USDT | below_1h_threshold | +3.60% | +3.70% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +3.55% | +3.65% |
| TESLA/USDT:USDT | below_1h_threshold | +2.55% | +2.65% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +2.29% | +2.39% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
