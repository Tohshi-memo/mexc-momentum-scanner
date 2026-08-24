# Decision Report

- generated_at: 2026-08-24T02:01:21.800157+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12486**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.06% / filled 20/20。**
- 全期間 MARKET基準: n=12486, expectancy=+0.01%
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
| LIMIT_ATR | 13/20 | 65.0% | +3.16% | **+2.05%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.23% | **+1.90%** |
| LIMIT_BB3S | 6/18 | 33.3% | +3.54% | **+1.18%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.29% | **+0.84%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +1.56% | **+0.86%** |
| LIMIT_FIB1272_LONG | 17/20 | 85.0% | +0.90% | **+0.76%** |
| LIMIT_5PCT_LONG | 14/20 | 70.0% | +0.85% | **+0.59%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +0.56% | **+0.34%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 191件 (TP 73 / SL 113 / EXP 5)
- 最新: ON/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$703.82** / 初期 $100.00 (+603.82%)
- 確定: 4509件 (Win 1375 / Loss 1477 / Flat 1657) / skip 4538件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $703.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$157.26** / 初期 $100.00 (+57.26%)
- 確定: 1962件 (Win 536 / Loss 469 / Flat 957) / skip 3935件
- 成長率目線: 平均log +0.000231 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0039 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ZEN/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $157.26

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.75** / 初期 $100.00 (+16.75%)
- 確定: 1873件 (Win 551 / Loss 708 / Flat 614) / pending 2件 / skip 2081件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000187 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $116.75

## 6. Latest Market Context

- 更新: 2026-08-24T02:01:11.322258+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=76881.7
- Funnel: target 1018 → liquid 175 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LIT/USDT:USDT | +12.44% | $10,833,366.28 |
| TUT/USDT:USDT | +6.81% | $52,189,051.66 |
| GRASS/USDT:USDT | +6.64% | $2,840,884.21 |
| 1000RATS/USDT:USDT | +6.13% | $2,453,080.66 |
| STORJ/USDT:USDT | +6.13% | $1,039,204.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXS/USDT:USDT | below_1h_threshold | +1.90% | +1.91% |
| TOKYOELSTOCK/USDT:USDT | below_1h_threshold | +1.76% | +1.78% |
| EUR/USDT:USDT | below_1h_threshold | +0.69% | +0.71% |
| LIT/USDT:USDT | below_1h_threshold | +0.68% | +0.70% |
| GRASS/USDT:USDT | below_1h_threshold | +0.40% | +0.42% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
