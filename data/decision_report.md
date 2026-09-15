# Decision Report

- generated_at: 2026-09-15T06:26:30.292522+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14570**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14570, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.89% | **+0.75%** |
| LIMIT_5PCT | 12/20 | 60.0% | +0.95% | **+0.57%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.69% | **+0.17%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.67% | **+1.34%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.14% | **+0.97%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.92% | **+0.96%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.54% | **+0.89%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.33% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 213件 (TP 79 / SL 129 / EXP 5)
- 最新: STORJ/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,078.16** / 初期 $100.00 (+978.16%)
- 確定: 5472件 (Win 1641 / Loss 1773 / Flat 2058) / skip 5659件
- 成長率目線: 平均log +0.000435 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LSK/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $1,078.16

## 4. Robust Adaptive DryRun ($100)

- 残高: **$230.23** / 初期 $100.00 (+130.23%)
- 確定: 3011件 (Win 835 / Loss 717 / Flat 1459) / skip 4970件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0713 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $230.23

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.20** / 初期 $100.00 (+24.20%)
- 確定: 2907件 (Win 862 / Loss 1132 / Flat 913) / pending 2件 / skip 3136件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000234 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LONGXIA/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $124.20

## 6. Latest Market Context

- 更新: 2026-09-15T06:26:18.258216+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=77417.4
- Funnel: target 1073 → liquid 159 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SHROOM/USDT:USDT | +58.52% | $1,556,905.22 |
| AIN/USDT:USDT | +52.15% | $9,243,874.08 |
| POWER/USDT:USDT | +51.26% | $9,426,384.50 |
| FF/USDT:USDT | +28.62% | $1,158,380.49 |
| STORJ/USDT:USDT | +15.32% | $1,055,398.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIULAI/USDT:USDT | below_1h_threshold | +3.33% | +3.55% |
| AIN/USDT:USDT | below_1h_threshold | +1.80% | +2.03% |
| RIVER/USDT:USDT | below_1h_threshold | +0.82% | +1.04% |
| STORJ/USDT:USDT | below_1h_threshold | +0.80% | +1.02% |
| MUU/USDT:USDT | below_1h_threshold | +0.60% | +0.82% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
