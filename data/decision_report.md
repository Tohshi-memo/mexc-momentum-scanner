# Decision Report

- generated_at: 2026-08-23T03:21:20.128946+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12437**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.76% / filled 20/20。**
- 全期間 MARKET基準: n=12437, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.76% | **+0.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 14/20 | 70.0% | +1.65% | **+1.16%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.30% | **+1.04%** |
| MARKET | 20/20 | 100.0% | +0.76% | **+0.76%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.63% | **+0.66%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.51% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +1.65% | **+1.24%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.31% | **+0.98%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +1.12% | **+0.73%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.36% | **+0.18%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.08% | **+0.07%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$709.67** / 初期 $100.00 (+609.67%)
- 確定: 4464件 (Win 1367 / Loss 1459 / Flat 1638) / skip 4534件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TUT/USDT:USDT `LIMIT_4PCT_LONG` TP_HIT account +1.00% 残高後 $709.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.53** / 初期 $100.00 (+56.53%)
- 確定: 1935件 (Win 533 / Loss 465 / Flat 937) / skip 3913件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0593 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MOVE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $156.53

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.84** / 初期 $100.00 (+16.84%)
- 確定: 1863件 (Win 549 / Loss 706 / Flat 608) / pending 0件 / skip 2046件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000135 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TUT/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $116.84

## 6. Latest Market Context

- 更新: 2026-08-23T03:21:11.229132+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=77092.0
- Funnel: target 1018 → liquid 207 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +50.73% | $46,931,325.40 |
| ZRO/USDT:USDT | +14.80% | $10,526,752.21 |
| UAI/USDT:USDT | +13.45% | $3,318,368.93 |
| TST/USDT:USDT | +10.46% | $1,016,635.45 |
| PORTAL/USDT:USDT | +9.73% | $3,119,910.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AGI/USDT:USDT | below_1h_threshold | +3.85% | +3.83% |
| HEMI/USDT:USDT | below_1h_threshold | +3.67% | +3.66% |
| TUT/USDT:USDT | below_1h_threshold | +2.77% | +2.75% |
| TOKYOELSTOCK/USDT:USDT | below_1h_threshold | +1.96% | +1.95% |
| ONG/USDT:USDT | below_1h_threshold | +1.56% | +1.54% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
