# Decision Report

- generated_at: 2026-08-23T02:46:11.634344+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12436**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.36% / filled 20/20。**
- 全期間 MARKET基準: n=12436, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.36% | **+1.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.36% | **+1.36%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.51% | **+1.13%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.70% | **+1.11%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.18% | **+1.06%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.63% | **+0.66%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +0.85% | **+0.64%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.51% | **+0.38%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.20% | **+0.13%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | -0.03% | **-0.02%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | -1.93% | **-0.29%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$702.64** / 初期 $100.00 (+602.64%)
- 確定: 4463件 (Win 1366 / Loss 1459 / Flat 1638) / skip 4534件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TUT/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $702.64

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.53** / 初期 $100.00 (+56.53%)
- 確定: 1935件 (Win 533 / Loss 465 / Flat 937) / skip 3912件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0563 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MOVE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $156.53

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.84** / 初期 $100.00 (+16.84%)
- 確定: 1863件 (Win 549 / Loss 706 / Flat 608) / pending 0件 / skip 2044件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000128 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TUT/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $116.84

## 6. Latest Market Context

- 更新: 2026-08-23T02:46:05.135972+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=77176.8
- Funnel: target 1018 → liquid 206 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +44.22% | $45,555,277.43 |
| CATE/USDT:USDT | +28.83% | $14,000,915.38 |
| ZRO/USDT:USDT | +14.97% | $9,989,573.65 |
| PORTAL/USDT:USDT | +13.32% | $3,055,734.86 |
| UAI/USDT:USDT | +12.18% | $3,215,659.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +4.93% | +4.96% |
| TST/USDT:USDT | below_1h_threshold | +4.15% | +4.19% |
| PORTAL/USDT:USDT | below_1h_threshold | +2.37% | +2.41% |
| VELVET/USDT:USDT | below_1h_threshold | +1.92% | +1.95% |
| EUL/USDT:USDT | below_1h_threshold | +1.84% | +1.87% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
