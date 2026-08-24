# Decision Report

- generated_at: 2026-08-24T15:41:43.705865+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12522**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12522, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.39% | **-0.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.63% | **+0.57%** |
| LIMIT_5PCT | 3/20 | 15.0% | +3.30% | **+0.50%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.62% | **+0.43%** |
| LIMIT_BB3S | 3/16 | 18.8% | +2.00% | **+0.37%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.02% | **+0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.54% | **+1.39%** |
| MARKET_LONG | 20/20 | 100.0% | +0.78% | **+0.78%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.83% | **+0.54%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.81% | **+0.28%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 191件 (TP 73 / SL 113 / EXP 5)
- 最新: ON/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$703.82** / 初期 $100.00 (+603.82%)
- 確定: 4510件 (Win 1375 / Loss 1477 / Flat 1658) / skip 4573件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $703.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.71** / 初期 $100.00 (+56.71%)
- 確定: 1972件 (Win 536 / Loss 470 / Flat 966) / skip 3961件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PORTAL/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $156.71

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.65** / 初期 $100.00 (+15.65%)
- 確定: 1905件 (Win 559 / Loss 722 / Flat 624) / pending 5件 / skip 2084件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000280 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PONS/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.65

## 6. Latest Market Context

- 更新: 2026-08-24T15:41:34.625779+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=79579.9
- Funnel: target 1022 → liquid 176 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PONS/USDT:USDT | +79.31% | $1,635,883.47 |
| CASHCAT/USDT:USDT | +53.51% | $1,640,738.68 |
| PROM/USDT:USDT | +31.12% | $13,623,741.75 |
| SUPER/USDT:USDT | +25.18% | $3,962,728.85 |
| UAI/USDT:USDT | +24.07% | $15,007,040.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_relative_strength | +5.11% | +4.99% |
| PONS/USDT:USDT | below_1h_threshold | +4.43% | +4.30% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +3.98% | +3.85% |
| BASECAT/USDT:USDT | below_1h_threshold | +3.69% | +3.56% |
| MONAD/USDT:USDT | below_1h_threshold | +3.26% | +3.14% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
