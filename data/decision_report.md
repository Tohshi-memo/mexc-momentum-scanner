# Decision Report

- generated_at: 2026-09-10T18:41:28.104631+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14177**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14177, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.01% | **+0.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +3.84% | **+0.96%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| LIMIT_BB3S | 2/13 | 15.4% | +5.50% | **+0.85%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.23% | **+0.55%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +5.42% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/6 | 100.0% | +3.30% | **+3.30%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.11% | **+1.00%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.14% | **+0.57%** |
| MARKET_LONG | 20/20 | 100.0% | +0.47% | **+0.47%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.56% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 208件 (TP 78 / SL 125 / EXP 5)
- 最新: EIGEN/USDT:USDT SL_HIT PnL -3.25% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,068.83** / 初期 $100.00 (+968.83%)
- 確定: 5357件 (Win 1611 / Loss 1730 / Flat 2016) / skip 5381件
- 成長率目線: 平均log +0.000442 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CNPY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,068.83

## 4. Robust Adaptive DryRun ($100)

- 残高: **$208.50** / 初期 $100.00 (+108.50%)
- 確定: 2771件 (Win 766 / Loss 649 / Flat 1356) / skip 4817件
- 成長率目線: 平均log +0.000265 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1085 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CNPY/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $208.50

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.48** / 初期 $100.00 (+22.48%)
- 確定: 2682件 (Win 791 / Loss 1024 / Flat 867) / pending 5件 / skip 2963件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000474 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CNPY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $122.48

## 6. Latest Market Context

- 更新: 2026-09-10T18:41:15.139811+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.26% price=77096.4
- Funnel: target 1067 → liquid 175 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +23.19% | $1,647,116.06 |
| CNPY/USDT:USDT | +15.69% | $1,559,052.09 |
| MEMEROBINHOOD/USDT:USDT | +9.40% | $1,023,695.39 |
| EIGEN/USDT:USDT | +8.57% | $1,813,568.22 |
| PONS/USDT:USDT | +8.52% | $9,030,382.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MEMEROBINHOOD/USDT:USDT | below_1h_threshold | +4.67% | +4.94% |
| BTR/USDT:USDT | below_1h_threshold | +2.33% | +2.59% |
| SNXX/USDT:USDT | below_1h_threshold | +2.08% | +2.34% |
| TUT/USDT:USDT | below_1h_threshold | +1.88% | +2.14% |
| CHIP/USDT:USDT | below_1h_threshold | +1.81% | +2.08% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
