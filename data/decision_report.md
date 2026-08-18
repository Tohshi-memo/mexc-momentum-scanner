# Decision Report

- generated_at: 2026-08-18T06:56:31.640623+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11887**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.30% / filled 20/20。**
- 全期間 MARKET基準: n=11887, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.30% | **+0.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.88% | **+1.15%** |
| LIMIT_ATR | 6/20 | 30.0% | +2.95% | **+0.88%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.02% | **+0.76%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.90% | **+0.72%** |
| LIMIT_BB3S | 2/20 | 10.0% | +6.60% | **+0.66%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.79% | **+0.90%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.40% | **+0.84%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.82% | **+0.82%** |
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.58% | **+0.39%** |

## 2. $100 Live Portfolio

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定トレード: 187件 (TP 72 / SL 110 / EXP 5)
- 最新: HEMI/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.41
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$612.41** / 初期 $100.00 (+512.41%)
- 確定: 4188件 (Win 1293 / Loss 1366 / Flat 1529) / skip 4260件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACE/USDT:USDT `LIMIT_FIB1272` SL_HIT account +0.13% 残高後 $612.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.25** / 初期 $100.00 (+55.25%)
- 確定: 1819件 (Win 502 / Loss 427 / Flat 890) / skip 3479件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0031 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $155.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.26** / 初期 $100.00 (+17.26%)
- 確定: 1698件 (Win 505 / Loss 643 / Flat 550) / pending 4件 / skip 1656件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000126 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ACE/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $117.26

## 6. Latest Market Context

- 更新: 2026-08-18T06:56:19.028177+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=64259.9
- Funnel: target 992 → liquid 183 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RED/USDT:USDT | +22.36% | $2,062,729.78 |
| PRL/USDT:USDT | +20.66% | $2,666,508.35 |
| CYS/USDT:USDT | +10.81% | $17,633,026.84 |
| VVV/USDT:USDT | +9.06% | $3,593,530.63 |
| PIEVERSE/USDT:USDT | +9.00% | $3,101,800.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIEVERSE/USDT:USDT | below_1h_threshold | +2.24% | +2.16% |
| H/USDT:USDT | below_1h_threshold | +1.85% | +1.76% |
| MONAD/USDT:USDT | below_1h_threshold | +1.81% | +1.72% |
| VVV/USDT:USDT | below_1h_threshold | +1.68% | +1.60% |
| HYPE/USDT:USDT | below_1h_threshold | +1.22% | +1.13% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
